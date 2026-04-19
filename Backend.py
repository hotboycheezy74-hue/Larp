from InfoModule import appearanceSelection, musicSelection, vibeSelection
import openai_Module
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
    "Appearance": {
        "Style" : "",
        "ColorPalette" : "",
        "Accessories" : "",
        "Presentation" : "",
    }
}

# --// Test inputs before working on front end
TestInputData = { # --// For use case of a ready to go IG photo
    "Photo Vibe": "cool",
    "Vibe": "dreamy",
    "Music": {
        "Genre": "rap",
        "Energy": "laid_back",
        "Era": "2000s",
        "Artist": "Lazer Dim 700",
    },

}

# "Tell me what is in this image, and if you think it is someone that exists in this world, tell me who it is (it could be a rapper)"

#calls the main function
if __name__ == "__main__":
    spotify_module.search_artist_catalogue(TestInputData)
    #spotify_module.search_general_song(TestInputData)
    #openai_Module.get_outfit_style()
    #main()