import { useState } from "react";
import "./App.css";

function App() {
    const [imageFile, setImageFile] = useState(null);
    const [result, setResult] = useState(null);
    const [error, setError] = useState("");

    async function handleAnalyze() {
        if (!imageFile) {
            setError("Please upload an image first.");
            return;
        }

        setError("");
        setResult(null);

        const formData = new FormData();
        formData.append("image", imageFile);

        try {
            const response = await fetch("http://127.0.0.1:8000/analyze-image", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error("Upload failed");
            }

            const data = await response.json();
            console.log("Backend response:", data);
            setResult(data);
        } catch (err) {
            console.error(err);
            setError("Failed to send image to backend.");
        }
    }

    return (
        <div className="app-container">
            <h1>Image Upload Test</h1>

            <input
                type="file"
                accept="image/*"
                onChange={(e) => setImageFile(e.target.files[0])}
            />

            <button onClick={handleAnalyze}>Send Image</button>

            {error && <p>{error}</p>}

            {result && (
                <div>
                    <h2>Backend Result</h2>
                    <p><strong>Message:</strong> {result.message}</p>
                    <p><strong>Filename:</strong> {result.filename}</p>
                    <p><strong>Type:</strong> {result.content_type}</p>
                    <p><strong>Size:</strong> {result.size_in_bytes} bytes</p>
                </div>
            )}
        </div>
    );
}

export default App;