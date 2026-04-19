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
    contents = await image.read()

    return {
        "message": "image received successfully",
        "filename": image.filename,
        "content_type": image.content_type,
        "size_in_bytes": len(contents)
    }