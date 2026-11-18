{   "title" : "Test",
    "description": "Test Adventure",
    "pages" : {
        "template":{"description":["\"Describes{ITEM}\"",{"ITEM":[" INACTIVE"," ACTIVE"]}],
                    "props":{"ITEM":{"description":[""{}]}
                }
            },
        "start":{"description":["It's the beginning. There's {test}an extra room to the North.",{"test":["","a test item here and "]}],
                 "props":{
                     "test":{"description":["It's an item.{chtest}",{"chtest":[" It's reacting with the chtest in the room",""]}],"tags":{"takeable":1,"key":"testkey","lock":"testkey2"},"contents":{
                         "secrettestitem":{"description":["It's the third and final test item which says go to the Win from the start. ",{}],"tags":{}}}}},
                 "exits":{
                     "north":"extra",
                     "win":"win"}},
        "extra":{"description":["You are in the extra room. It's extra. There's {chtest}a room to the South that starts this adventure.",{"chtest":["a chtest here and ",""}],
                 "props":{
                     "chtest":{"description":["It's a test chest. It has a test-shaped lock on it{testkey}.",{"testkey":[" that is currently open",""]}],"tags":{"lock":"testkey"},"contents":{
                         "test2":{"description":["It's a second test item and can be used to open the first test item",{}],"tags":{"takeable":1,"key":"testkey2"}}}}},
                 "exits":{
                     "south":"start"}},
        "win":{"description":["This is the winning room! YOU HAVE WON!{trophy}",{"trophy":[" CLAIM YOUR TROPHY!",""]}],
                 "props":{
                     "trophy":{"description":["A beautiful golden trophy{spotlight}",{"spotlight":[". It sparkles in the spotlight's beam",""]}],"tags":{"takeable":1}},
                     "spotlight":{"description":["A beam of golden light",{}],"tags":{}}},
                 "exits":{
                     "lose":"start",
                     "secret":["secret",{"trophy":["active",1]}]}}

    }
}
