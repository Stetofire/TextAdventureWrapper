import os
import json

# ~~~~~~~~ Declaration of Constants ~~~~~~~~
COMMANDS = [
    {"command":"exit","description":"Exits the game (see also \"quit\")"},
    {"command":"go","description":"Moves the player. Useage: \"go [destination]\". (see also \"move\")"},
    {"command":"help","description":"Displays all known commands"},
    {"command":"inv","description":"Displays the contents of your inventory (see also \"inventory\")"},
    {"command":"inventory","description":"Displays the contents of your inventory (see also \"inv\")"},
    {"command":"look","description":"Displays description of current location. Can be told what to look at (\"look [item]\")"},
    {"command":"move","description":"Moves the player. Useage: \"move [destination]\". (see also \"go\")"},
    #{"command":"put","description":"Places an item in something that can act as a container. Useage: \"put [item1] [item2]\""},
    {"command":"quit","description":"Exits the game (see also \"exit\")"},
    {"command":"save","description":"Saves the game state"},
    {"command":"take","description":"Puts the item in your inventory. Useage: \"take [item]\""},
    {"command":"use","description":"Applies an item to another or something in a room. Useage: \"use [item1] [item2]\""},
]

# ~~~~~~~~ Declaration of Functions ~~~~~~~~

def look(game, page, player, command): # Looks generally. "command" is a List of the player's entered text
    if len(command)>1:  # the player wants to examine an item in their inventory or a prop in the room
        # describe item in inventory
        if command[1] in player["inventory"]:
            print("In your inventory you see this {0}: \"{1}\"".format(command[1],describe(game, page, player, player["inventory"][command[1]])))
        # describe prop in room
        elif command[1] in game["pages"][page]["props"]:
            print("You see a {0} in the room: \"{1}\"".format(command[1],describe(game, page, player, game["pages"][page]["props"][command[1]])))
        else:
            print("That item does not exist")
    else:   # the player wants to examine the room itself
        print(describe(game, page, player))
        
def describe(game, page, player, item={}): #    Describes either an item or the room itself but only uses certain parts of the string if a matching Prop is in the room or if an item has a matching tag. The "description" object in the data structure must be in this format:  ["text with {tag}",{"tag":[["disabled prop in room","enabled prop in room"],["disabled item in inv","enabled item in inv"]]. It will be used in the format_map function.
    description = ""
    applicable = {}
    if item:
        breakpoint()
        if type(item["description"]) is list and len(item["description"])>1: # if formatting is correct for conditional sections
            for d in item["description"][1]:
                if d in game["pages"][page]["props"]: # exists in room
                    if ("active" in game["pages"][page]["props"][d]["tags"] and game["pages"][page]["props"][d]["tags"]["active"]): # in-room active
                        applicable[d] = item["description"][1][d][0][1] # show in-room active description
                    else: # in-room inactive
                        applicable[d] = item["description"][1][d][0][0] # show in-room inactive description
                elif d in player["inventory"]: # exists in iventory
                    if "active" in player["inventory"][d]["tags"] and player["inventory"][d]["tags"]["active"]: # in-inv active
                        applicable[d] = item["description"][1][d][1][1] # show in-inv active description
                    else: # in-inv inactive
                        applicable[d] = item["description"][1][d][1][0] # show in-inv inactive description
                elif d in item["tags"]: # exists in item itself
                    if item["tags"][d]: # in-item truthy
                        applicable[d] = item["description"][1][d][1][1] # show in-inv active description
                    else: # in-item falsy
                        applicable[d] = item["description"][1][d][1][0] # show in-inv inactive description
                else: # doesn't exist
                    applicable[d] = ""
            description = item["description"][0].format_map(applicable)
        # if item has contents, display only if unlocked
        if "contents" in item and (("lock" not in item["tags"]) or ("locked" not in item["tags"] or not item["tags"]["locked"])): # is unlocked
            if len(item["contents"]) > 0:
                description += "\nIt also contains the following:"
                description += display_inventory(game, page, item["contents"])
            else:
                description += " It's empty"
    else: # look at room
        for d in game["pages"][page]["description"][1]:
            if d in game["pages"][page]["props"]:# exists in room
                if ("active" in game["pages"][page]["props"][d]["tags"] and game["pages"][page]["props"][d]["tags"]["active"]): # in-room active
                    applicable[d] = item["description"][1][d][0][1] # show in-room active description
                else: # in-room inactive
                    applicable[d] = item["description"][1][d][0][0] # show in-room inactive description
            elif d in player["inventory"]: # exists in iventory
                if "active" in player["inventory"][d]["tags"] and player["inventory"][d]["tags"]["active"]: # in-inv active
                    applicable[d] = item["description"][1][d][1][1] # show in-inv active description
                else: # in-inv inactive
                        applicable[d] = item["description"][1][d][1][0] # show in-inv inactive description
            else: # description tag not in room or inv
                applicable[d] = ""
        description = game["pages"][page]["description"][0].format_map(applicable)
    return description

def depth_search(items, target):   # item is a dictionary of objects but target is just the id of the item being searched for. Returns item in question but leaves it there else returns an empty item
    for c in items:
        if c == target:
            return items[c]
        else:
            if "contents" in items[c] and ("lock" not in items[c]["tags"] or ("lock" in items[c]["tags"] and items[c]["tags"]["lock"] in items[c]["tags"])):
                return depth_search(items[c]["contents"], target)
    else:
        return {}
def depth_search_pop(items, target):   # item is a dictionary of objects but target is just the id of the item being searched for. Returns *and pops* item in question else returns an empty item.
    for c in items:
        if c == target:
            return items.pop(c)
        else:
            if "contents" in items[c] and ("lock" not in items[c]["tags"] or ("lock" in items[c]["tags"] and items[c]["tags"]["lock"] in items[c]["tags"])):
                return depth_search_pop(items[c]["contents"], target)
    else:
        return {}

def display_inventory(game, page, inv):
    #print("*** DISPLAY INVENTORY: entire inventory:",end="")
    #print(inv)
    description = ""
    for item in inv:
        description += "\n{0}\t\"{1}\"".format(item.capitalize(),describe(game, page, inv[item]))
    return description

def game_query(pathway):
    games = []
    for g in os.scandir(pathway):
        if g.is_file():
            name = g.name.split("_")[0]
            desc = g.name.split("_")[1].split(".")[0]
            games.append([g,name,desc])
    return games

def game_list():
    print ("Current adventures available:")
    for g in GAMES:
        print("{0}:\t\"{1}\"".format(g[1],g[2]))
            
def game_load(game_info):
    game = {}
    player = {}
    page = ""
    #print("*** GAME LOAD loading game ",end="")
    #print(game_info,end="")
    #print(game_info[0].name)
    print("Loading game {0}...".format(game_info[1].capitalize()))
    try:
        if os.path.isfile(game_info[0]): # if file exists
            # open file and load
            with open(game_info[0]) as f:
                game = json.load(f)
                print("TODO: implement game state loading in game_load()")
                player = {"name":"player","inventory":{}}
                page = "start"
                #print("*** GAME LOAD loaded game: ",end="")
                #print(game)
    except FileNotFoundError:
        pass
    return game, player, page

def game_save(player):
    print("Saved! (... he lied. (TODO))")

def game_run(game_info):
    game, player, page = game_load(game_info)
    if not game:
        print("ERROR LOADING GAME. ABORTING ATTEMPT")
        return -1
    print("\nWelcome to "+game["title"]+"!")

# ~~~~~~~~ Main Game Loop ~~~~~~~~
    command = "look".split(" ") # Give a room description right on startup
    while(True):
        # input is at the bottom of the loop to allow for showing the room's description as the first command
        if (command[0] == "quit" or command[0] == "exit"):      # QUIT
            break
        elif (command[0] == "help"):        # HELP
            for c in COMMANDS:
                print("\""+c["command"]+"\": "+c["description"])
        elif (command[0] == "db"):        # DEBUG
            print("*** DEBUG     entire player: ",end="")
            print(player)
            print("*** DEBUG     entire page: ",end="")
            print(game["pages"][page])
        elif (command[0] == "save"):        # SAVE
            if (game_save(player)):
                pass#print("Saved!")
        elif (command[0] == "go" or command[0] == "move"):      # MOVE
            if len(command) >= 2:
                destination = ""
                reason = ""
                for e in game["pages"][page]["exits"]:
                    if command[1] == e:
                        if type(game["pages"][page]["exits"][e]) is list: # if exit is conditional
                            metConditions = True
                            for c in game["pages"][page]["exits"][e]:# make sure every condition is met
                                # object must exist
                               if game["pages"][page]["exits"][e][c]:# tag does not match
                                   metConditions = False
                            if metConditions:
                                destination = game["pages"][page]["exits"][e]
                            else: # else display error message
                                reason = game["pages"][page]["exits"][e]
                        else: #unconditional
                            destination = game["pages"][page]["exits"][e]
                if destination:
                    page = destination
                    print("You move {0}ward. {1}".format(command[1],describe(game, page)))
                else:
                    print("That direction is not traversable{0}".format(reason))
            else:
                print("Invalid argument. Useage: \"go/move [destination]\"")
        elif (command[0] == "look"):        # LOOK
            look(game, page, player, command)
        elif (command[0] == "take"):        # TAKE
            if len(command) >= 2:
                foundItem = depth_search(game["pages"][page]["props"], command[1])
                #print("** TAKE: found item is: ",end="")
                #print(foundItem)
                if foundItem:
                    if "takeable" in foundItem["tags"] and foundItem["tags"]["takeable"]:
                        player["inventory"][command[1]] = depth_search_pop(game["pages"][page]["props"], command[1])
                        print("You take the {0}. \"{1}\"".format(command[1],describe(game, page, player["inventory"][command[1]])))
                    else:
                        print("That item is not takeable")
                else:
                    print("You don't see anything by that name")
            else:
                print("Invalid argument. Useage: \"take [item]\"")
        elif (command[0] == "use"):        # USE
            if len(command) >= 3:
                # if use is applicable (inv to room, inv to inv, room to room, room to inv)
                used = False
                if command[1] in player["inventory"]:   # if the player has the applying item
                    #print("*** inv to... ",end="")
                    if command[2] in game["pages"][page]["props"]: # if the receiving prop is in the room
                        if "key" in player["inventory"][command[1]]["tags"] and "lock" in game["pages"][page]["props"][command[2]]["tags"] and player["inventory"][command[1]]["tags"]["key"] == game["pages"][page]["props"][command[2]]["tags"]["lock"]: # if applicable
                            # inv to room
                            game["pages"][page]["props"][command[2]]["tags"][player["inventory"][command[1]]["tags"]["key"]] = player["inventory"][command[1]]["tags"]["key"]
                            used = True
                            #print("..room")
                            #print("After \"use\" command, these are the relevent objects:")
                            #print(player["inventory"][command[1]])
                            #print(game["pages"][page]["props"][command[2]])
                        else:
                            print("There's no reaction when you use your {0} on the {1} in the room".format(command[1],command[2]))
                    elif command[2] in player["inventory"]: # if the player has the receiving item
                        if "key" in player["inventory"][command[1]]["tags"] and "lock" in player["inventory"][command[2]]["tags"] and player["inventory"][command[1]]["tags"]["key"] == player["inventory"][command[2]]["tags"]["lock"]: # if applicable
                            # inv to inv
                            player["inventory"][command[2]]["tags"][player["inventory"][command[1]]["tags"]["key"]] = player["inventory"][command[1]]["tags"]["key"]
                            used = True
                            #print("..inv")
                            #print("After \"use\" command, these are the relevent objects:")
                            #print(player["inventory"][command[1]])
                            #print(player["inventory"][command[2]])
                        else:
                            print("There's no reaction when you use your {0} on your {1}".format(command[1],command[2]))
                    else:
                        print("You can't find a {0} to use your {1} on".format(command[2],command[1]))
                elif command[1] in game["pages"][page]["props"]: # if the applying prop is in the room
                    #print("*** room to... ",end="")
                    if command[2] in game["pages"][page]["props"]: # if the receiving prop is in the room
                        if "key" in game["pages"][page]["props"][command[1]]["tags"] and "lock" in game["pages"][page]["props"][command[2]]["tags"] and game["pages"][page]["props"][command[1]]["tags"]["key"] == game["pages"][page]["props"][command[2]]["tags"]["lock"]: # if applicable
                            # room to room
                            game["pages"][page]["props"][command[2]]["tags"][game["pages"][page]["props"][command[1]]["tags"]["key"]] = game["pages"][page]["props"][command[1]]["tags"]["key"]
                            used = True
                            #print("..room")
                            #print("After \"use\" command, these are the relevent objects:")
                            #print(game["pages"][page]["props"][command[1]])
                            #print(game["pages"][page]["props"][command[2]])
                        else:
                            print("There's no reaction when you try to use the {0} on the room's {1}".format(command[1],command[2]))
                    elif command[2] in player["inventory"]: # if the player has the receiving item
                        if "key" in game["pages"][page]["props"][command[1]]["tags"] and "lock" in player["inventory"][command[2]]["tags"] and game["pages"][page]["props"][command[1]]["tags"]["key"] == player["inventory"][command[2]]["tags"]["lock"]: # if applicable
                            # room to inv
                            player["inventory"][command[2]]["tags"][game["pages"][page]["props"][command[1]]["tags"]["key"]] = game["pages"][page]["props"][command[1]]["tags"]["key"]
                            used = True
                            #print("..inv")
                            #print("After \"use\" command, these are the relevent objects:")
                            #print(game["pages"][page]["props"][command[1]])
                            #print(player["inventory"][command[2]])
                        else:
                            print("There's no reaction when you use the {0} from the room on your {1}".format(command[1],command[2]))
                    else:
                        print("You can't find a {0} to use your {1} on".format(command[2],command[1]))
                else:
                    print("You can't find a {0}".format(command[1]))
                if used:
                    print("It worked!")
                    look(game, page, player, ["look",command[2]])
            else:
                print("Invalid argument. Useage: \"use [item1] [item2]\"")
        elif (command[0] == "inventory" or command[0] == "inv"):        # INVENTORY
            print(display_inventory(game, page, player["inventory"]))
        else:
            print("Unknown command. Type \"help\" for a list of commands")
        command = input("> ").lower().split(" ")
    return 1


# ~~~~~~~~ Wrapper Loop ~~~~~~~~
pathway = "adventures/"
GAMES = game_query(pathway)
while(True):
    # prompt for game
    game_list()
    title = input("Which adventure would you like to play? (\"quit\" or \"exit\" to quit) ").lower()
    if title == "quit" or title == "exit":
        break
    # run game
    success = 0
    for g in GAMES:
        if title == g[1].lower():
            #print("*** MAIN loading game ",end="")
            #print(g,end="")
            #print(" at pathway ",end="")
            #print(pathway,end="")
            success = game_run(g)
            break
    if success == 0:
        print("Game not found. ",end="")
    elif success < 0:
        print("Error loading game. ",end="")
    else:
        print("Hope you enjoyed{0}! ".format(title),end="")
print("Thanks for playing!")
