import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from InfoModule import appearanceSelection, musicSelection, vibeSelection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import Body

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
        "Style": "",
        "Presentation": "",
    }
}

@app.post("/submit-answers")
async def submit_answers(data: dict = Body(...)):
    print("RECEIVED FROM FRONTEND:", data)

    UserInputtedData["Music"]["Genre"] = data.get("musicGenre", "")
    UserInputtedData["Music"]["Energy"] = data.get("musicEnergy", "")
    UserInputtedData["Music"]["Era"] = data.get("musicEra", "")
    UserInputtedData["Music"]["Artist"] = data.get("artist", "")

    UserInputtedData["Vibe"] = data.get("vibe", "")

    UserInputtedData["Photo Appearance"]["Style"] = data.get("appearanceStyle", "")
    UserInputtedData["Photo Appearance"]["Presentation"] = data.get("appearancePresentation", "")

    print("UPDATED USER DATA:", UserInputtedData)

    return {
        "message": "data received",
        "data": UserInputtedData
    }

@app.get("/")
def home():
    return {"message": "backend running"}

@app.get("/options")
def get_options():
    return {
        "appearance": appearanceSelection,
        "music": musicSelection,
        "vibes": vibeSelection
    }

@app.post("/analyze-image")
async def analyze_image(image: UploadFile = File(...)):
    try:
        print("UPLOAD HIT")

        contents = await image.read()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        upload_dir = os.path.join(base_dir, "larpimages")
        os.makedirs(upload_dir, exist_ok=True)

        safe_filename = os.path.basename(image.filename)
        file_path = os.path.join(upload_dir, safe_filename)

        with open(file_path, "wb") as f:
            f.write(contents)

        print("Saved to:", file_path)

        return {
            "message": "saved",
            "filename": safe_filename
        }
    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return {
            "error": str(e)
        }