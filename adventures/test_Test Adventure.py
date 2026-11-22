{   "title" : "Test",
    "description": "Test Adventure",
    "pages" : {
        "template":{"description":["{ITEM}",{"ITEM":[[" IN ROOM UNLOCKED"," IN ROOM LOCKED"],[" IN INV UNLOCKED"," IN INV LOCKED"]]}],
                    "props":{"ITEM":{"description":["",{}],
                                     "tags":{"takeable":1,"active":0,"key":"SOMETHING","lock":"SOMETHING","locked":0,"contents":{}}}
                    }
            },
        "start":{"description":["It's the beginning. There's {test}an extra room to the North.",{"test":[["a test item here and ",""],["the dust from a test item and ",""]]}],
                 "props":{
                     "test":{"description":["It's an item.{chtest}",{"chtest":[[" It's reacting with the chtest in the room",""],["",""]]}],"tags":{"takeable":1,"key":"testkey","lock":"testkey2","locked":1},"contents":{
                         "secrettestitem":{"description":["It's the third and final test item which says go to the Win from the start. ",{}],"tags":{}}}}},
                 "exits":{
                     "north":"extra",
                     "win":"win"}},
        "extra":{"description":["You are in the extra room. It's extra. There's {chtest}a room to the South that starts this adventure.",{"chtest":[["an open chtest here and ","a chtest here and "],["",""]]}],
                 "props":{
                     "chtest":{"description":["It's a test chest. It has a test-shaped lock on it{chtest}.",{"chtest":[[" that is currently open"," securely fastened"],["",""]]}],"tags":{"lock":"testkey","locked":1},"contents":{
                         "test2":{"description":["It's a second test item and can be used to open the first test item",{}],"tags":{"takeable":1,"key":"testkey2"}}}}},
                 "exits":{
                     "south":"start"}},
        "win":{"description":["This is the winning room! YOU HAVE WON!{trophy}",{"trophy":[[" CLAIM YOUR TROPHY!",""],["",""]]}],
                 "props":{
                     "trophy":{"description":["A beautiful golden trophy{spotlight}",{"spotlight":[[". It sparkles in the spotlight's beam",""],["",""]]}],"tags":{"takeable":1}},
                     "spotlight":{"description":["A beam of golden light{trophy}",{"trophy":[[" that glints off a trophy in the room",""],[" that glints off the trophy in your hands",""]]}],"tags":{}}},
                 "exits":{
                     "lose":"start",
                     "secret":["secret",{"trophy":["locked",1]},"Your trophy must be locked first."]}}
    }
}
