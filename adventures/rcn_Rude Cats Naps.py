{   "title" : "rcn",
    "description": "Rude Cats Naps: A sleepy adventure",
    "pages" : {
        "TEMPLATE":{"description":["WELCOME MESSAGE",{}],
                 "props":{
                     "ITEM":{"description":["TEXT{ITEM}",{"TEXT":[["",""],["",""]]}],"tags":{}}
                     },
                    "exits":{"ELSEWHERE":["DESTINATION",{"ITEMorPROP":{"KEY":"VALUE"}},"REASON"]
                     }},
        "start":{"description":["You finally arrive home after a gruelling day at work and you're ready to rest.{lock}",{"lock":[[" Your recliner awaits."," Your front door is the only thing keeping you from your sweet recliner. However, it's locked."],["",""]]}],
                 "props":{
                     "lock":{"description":["Home security.{lock}{key}",{"lock":[[" It's unlocked."," It's locked."],["",""]],"key":[[" You always keep the key under the rug.",""],[" You have the key for it.",""]]}],"tags":{"locked":1,"lock":"frontlock"}},
                     "door":{"description":["A beautiful green door. You painted it last summer.{lock}",{"lock":[[" It's unlocked."," It's locked."],["",""]]}],"tags":{}},
                     "key":{"description":["The key to your front door.{lock}",{"lock":[[""," You can take it to use it on said door."],[""," You should use it on said door."]]}],"tags":{"takeable":1,"key":"frontlock"}},
                     "rug":{"description":["Your front rug.{key}",{"key":[[" The front door key is under it.",""],[" Usually where you keep your key.",""]]}],"tags":{}}
                     },
                 "exits":{"in":["living",{"lock":{"locked":0}},"The door is locked."],
                          "door":["living",{"lock":{"locked":0}},"The door is locked."],
                          "house":["living",{"lock":{"locked":0}},"The door is locked."]
                     }},
        "living":{"description":["(living room)",{}],
                 "props":{
                     },
                  "exits":{"door":"start",
                           "out":"start"
                     }}
    }
}
