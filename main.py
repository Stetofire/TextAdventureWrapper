# ~~~~~~~~ Declaration of Constants ~~~~~~~~
COMMANDS = [
    {"command":"exit","description":"Exits the game (see also \"quit\")"},
    #{"command":"go","description":"Moves the player (see also \"move\")"},
    {"command":"help","description":"Displays all known commands"},
    {"command":"inv","description":"Displays the contents of your inventory (see also \"inv\")"},
    {"command":"inventory","description":"Displays the contents of your inventory (see also \"inv\")"},
    #{"command":"move","description":"Moves the player (see also \"go\")"},
    {"command":"put","description":"Places an item in something that can act as a container. Useage: \"put item1 item2\". "},
    {"command":"quit","description":"Exits the game (see also \"exit\")"},
    {"command":"save","description":"Saves the game state"},
    {"command":"take","description":"Puts the item in your inventory"},
    {"command":"use","description":"Applies an item to another or something in a room. Useage: \"use item1 item2\""},
]
GAME_DEFAULT = {
    "title" : "Test Adventure",
    "pages" : {
        "start":{"description":"It's the beginning. There's a test item here and an extra room to the North.",
                 "props":{
                     "test":{"description":"It's an item","tags":{"takeable":True,"key":"test"}}},
                 "exits":{
                     "north":"extra"}},
        "extra":{"description":"You are in the extra room. It's extra. There's an adventure starting room to the South.",
                 "props":{
                     "chtest":{"description":"It's a test chest","tags":{"lock":"test"},"contents":{
                         "test2":{"description":"It's a second test item","tags":{"takeable":True,"key":"test"}}}}},
                 "exits":{
                     "south":"start"}},
    }
}

# ~~~~~~~~ Declaration of Functions ~~~~~~~~
def game_load():
    print("TODO: implement saved game loading from json files")
    if (False): # if file exists
        pass    # open file and load
    else:
        game = GAME_DEFAULT
        player = {"name":"player","inventory":{}}
        page = "start"
    return game, player, page

def game_save(player):
    print("Saved! (... he lied. (TODO))")

def game_run(title):
    game, player, page = game_load()
    print("\nWelcome to "+game["title"]+"!")

    while(True):
        command = input("> ").lower()
        if (command == "quit" or command == "exit"):
            break
        elif (command == "help"):
            for c in COMMANDS:
                print("\""+c["command"]+"\": "+c["description"])
        elif (command == "save"):
            if (game_save(player)):
                pass#print("Saved!")
        else:
            print("Unknown command. Type \"help\" for a list of commands")
    print("Thanks for playing {0}!\n".format(game["title"]))

def game_list():
    print ("Current adventures available:")
    for g in GAMES:
        print(g)

# ~~~~~~~~ Main game loop ~~~~~~~~
print("TODO: load installed games")
GAMES = [GAME_DEFAULT["title"]]
while(True):
    # prompt for game
    game_list()
    title = input("Which adventure would you like to play? (\"quit\" or \"exit\" to quit) ").lower().capitalize()
    if title == "Quit" or title == "Exit":
        break
    # run game
    for g in GAMES:
        if title == g.lower().capitalize():
            game_run(title)
            break
        print("Game not found. ",end="")
print("Thanks for playing!")
