import InfoModule
QuestionBranches = {
    ['Instagram Ready Photo'] : {
        [1] : {
            "Question": "Upload the image of your Instagram ready post!",
        },
        # --// User inputs a photo
        [2] : {
            "Question": "What Vibe are you going for?",
            "Answers" : InfoModule.vibeSelection
        },
        [3] : {
            "Question": "Fill out the type of music you want!",
            "Answers" : [
                         InfoModule.musicSelection['Genre'],
                         InfoModule.musicSelection['Energy'],
                         InfoModule.musicSelection['Era'],
                         "Preferred Artist:"
                         ]
        },
        # --// Use all the information retrieved from frontend inputs on buttons for IG post
    },

    ['Outfit Music & Caption Advisor'] : {
        # --// First user optionally inputs a photo showcasing their style
        [1] : {
            "Question": "Upload an image showcasing your style!",
        },

        [2] : {
            "Question": "How would you describe your fashion style & the vibe you would like for your outfit??",
            "Answers" : [InfoModule.appearanceSelection["style_category"], InfoModule.appearanceSelection["presentation"]]
        },

        [3] : {
            "Question": "What is the overall vibe are you going for with your music & caption?",
            "Answers" : InfoModule.vibeSelection
        },

        [4] : {
            "Question": "Fill out the type of music you want!",
            "Answers" : [
                InfoModule.musicSelection['Genre'],
                InfoModule.musicSelection['Energy'],
                InfoModule.musicSelection['Era'],
                "Preferred Artist:"
            ]
        },
        # --// Use all the information retrieved from frontend inputs on buttons for clothing, music & caption
    },
}