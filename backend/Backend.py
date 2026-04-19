import spotify_module

# --// Table we'll use to fill in from user input & AI output
UserInputtedData = {
    "Music": {
        "Genre": "",
        "Energy": "",
        "Era": "",
        "Artist": "",
    },
    "Vibe": "",
    "Photo Vibe": "",
    "Photo Appearance": {
        "Style" : "",
        "Presentation" : "",
    }
}

# --// Test inputs before working on front end
TestInputData = { # --// For use case of a ready to go IG photo
    "Photo Vibe": "cool",
    "Vibe": "dreamy",
    "Music": {
        "Genre": "rap",
        "Energy": "aggressive",
        "Era": "currently_trending",
        "Artist": "Lazer Dim 700",
    },
}

#calls the main function
if __name__ == "__main__":
    print(spotify_module.search_general_song(TestInputData))
    #spotify_module.search_general_song(TestInputData)
    #openai_Module.get_outfit_style()
    #main()