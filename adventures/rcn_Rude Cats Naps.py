{   "title" : "rcn",
    "description": "Rude Cats Naps: A sleepy adventure",
    "pages" : {
        "start":{"description":["You finally arrive home after a gruelling day at work and you're ready to rest. Your front door is the only thing keeping you from your sweet recliner.{lock}",{"lock":[""," However, it's locked."]}],
                 "props":{"lock":{"description":["Home security.{lock}",{"lock":[" It's locked."," It's unlocked"]}],"tags":{"active":1,"lock":"frontlock"}},
                          "door":{"description":["A beautiful green door. You painted it last summer.{lock}",{"lock":[" It's unlocked."," It's locked."]}],"tags":{}}
                     },
                 "exits":{"in":["living",{"lock":{"active":0}}],
                          "house":["living",{"lock":{"active":0}}]
                     }
        }
    }
}
