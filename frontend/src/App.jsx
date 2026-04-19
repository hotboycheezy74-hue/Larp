import { useEffect, useState } from "react";
import "./App.css";

function App() {
    const [screen, setScreen] = useState("welcome");
    const [imageFile, setImageFile] = useState(null);
    const [previewUrl, setPreviewUrl] = useState("");
    const [result, setResult] = useState(null);
    const [error, setError] = useState("");
    const [flowType, setFlowType] = useState("");

    const [options, setOptions] = useState({
        appearance: {},
        music: {},
        vibes: []
    });

    const [formData, setFormData] = useState({
        vibe: "",
        musicGenre: "",
        musicEnergy: "",
        musicEra: "",
        appearanceStyle: "",
        appearancePalette: "",
        appearancePresentation: ""
    });

    useEffect(() => {
        async function loadOptions() {
            try {
                const response = await fetch("http://127.0.0.1:8000/options");
                const data = await response.json();
                console.log("OPTIONS RESPONSE:", data);
                setOptions(data);
            } catch (err) {
                console.error("OPTIONS ERROR:", err);
                setError("Could not load questionnaire options.");
            }
        }

        loadOptions();
    }, []);

    function handleStart() {
        setScreen("choice");
        setError("");
    }

    function handleImageChoice() {
        setFlowType("direct");
        setImageFile(null);
        setPreviewUrl("");
        setResult(null);
        setError("");
        setScreen("upload");
    }

    function handleQuestionnaireChoice() {
        setFlowType("questionnaire");
        setImageFile(null);
        setPreviewUrl("");
        setResult(null);
        setError("");
        setScreen("referenceChoice");
    }

    function goBackToChoice() {
        setScreen("choice");
        setError("");
        setResult(null);
    }

    function handleFileChange(e) {
        const file = e.target.files[0];

        if (!file) {
            setImageFile(null);
            setPreviewUrl("");
            return;
        }

        setImageFile(file);
        setPreviewUrl(URL.createObjectURL(file));
    }

    function selectBubble(field, value) {
        setFormData((prev) => ({
            ...prev,
            [field]: value
        }));
    }

    async function handleAnalyze() {
        if (!imageFile) {
            setError("Please upload an image first.");
            return;
        }
    async function handleSubmit() {
        try {
            const response = await fetch("http://127.0.0.1:8000/submit-answers", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            console.log("FINAL RESPONSE:", data);

            setResult(data);
        } catch (err) {
            console.error("SUBMIT ERROR:", err);
            setError("Failed to send data.");
        }
    }
        async function handleSubmit() {
            try {
                const response = await fetch("http://127.0.0.1:8000/submit-answers", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();
                console.log("FINAL RESPONSE:", data);

                setResult(data);
            } catch (err) {
                console.error("SUBMIT ERROR:", err);
                setError("Failed to send data.");
            }
        }
        setError("");
        setResult(null);

        const formDataToSend = new FormData();
        formDataToSend.append("image", imageFile);

        try {
            const response = await fetch("http://127.0.0.1:8000/analyze-image", {
                method: "POST",
                body: formDataToSend
            });

            const data = await response.json();
            console.log("UPLOAD RESPONSE:", data);

            if (!response.ok) {
                throw new Error(data.error || "Upload failed.");
            }

            setResult(data);

            if (flowType === "questionnaire") {
                setScreen("styleQuestions");
            }
        } catch (err) {
            console.error("UPLOAD ERROR:", err);
            setError("Failed to upload image.");
        }
    }

    function BubbleRow({ title, items, selectedValue, fieldName }) {
        return (
            <div className="form-group">
                <label>{title}</label>
                <div className="bubble-row">
                    {items && items.length > 0 ? (
                        items.map((item, index) => (
                            <button
                                key={index}
                                type="button"
                                className={`bubble ${selectedValue === item ? "selected" : ""}`}
                                onClick={() => selectBubble(fieldName, item)}
                            >
                                {item}
                            </button>
                        ))
                    ) : (
                        <p>No options loaded</p>
                    )}
                </div>
            </div>
        );
    }

    return (
        <div className="app-container">
            {screen === "welcome" && (
                <div className="card">
                    <h1>Build Your Post</h1>
                    <p>Create a full aesthetic direction through an image or a questionnaire.</p>
                    <button onClick={handleStart}>Get Started</button>
                </div>
            )}

            {screen === "choice" && (
                <div className="card">
                    <h1>Choose Your Path</h1>
                    <p>Start with a photo or answer a few style questions.</p>

                    <div className="button-group">
                        <button onClick={handleImageChoice}>Upload a Picture</button>
                        <button onClick={handleQuestionnaireChoice}>Fill Out Questionnaire</button>
                    </div>
                </div>
            )}

            {screen === "referenceChoice" && (
                <div className="card">
                    <h1>Reference Photo</h1>
                    <p>Do you want to upload a photo to guide your results?</p>

                    <div className="button-group">
                        <button
                            onClick={() => {
                                setFlowType("questionnaire");
                                setScreen("upload");
                                setError("");
                            }}
                        >
                            Yes, upload a photo
                        </button>

                        <button
                            onClick={() => {
                                setFlowType("questionnaire");
                                setScreen("styleQuestions");
                                setError("");
                            }}
                        >
                            Skip
                        </button>
                    </div>
                </div>
            )}

            {screen === "upload" && (
                <div className="card">
                    <h1>Upload a Picture</h1>
                    <p>
                        {flowType === "questionnaire"
                            ? "Upload a reference image to guide your questionnaire results."
                            : "Upload an image so the app can help build your post idea."}
                    </p>

                    <input
                        type="file"
                        accept="image/*"
                        onChange={handleFileChange}
                    />

                    {previewUrl && (
                        <div className="preview-section">
                            <h3>Preview</h3>
                            <img
                                src={previewUrl}
                                alt="Preview"
                                className="preview-image"
                            />
                        </div>
                    )}

                    {error && <p>{error}</p>}

                    {result && (
                        <div>
                            <p><strong>Message:</strong> {result.message}</p>
                            <p><strong>Filename:</strong> {result.filename}</p>
                        </div>
                    )}

                    <div className="button-group">
                        <button
                            onClick={() =>
                                flowType === "questionnaire"
                                    ? setScreen("referenceChoice")
                                    : goBackToChoice()
                            }
                        >
                            Back
                        </button>

                        <button onClick={handleAnalyze} disabled={!imageFile}>
                            Continue
                        </button>
                    </div>
                </div>
            )}

            {screen === "styleQuestions" && (
                <div className="card">
                    <h1>Style Preferences</h1>
                    <p>Choose your appearance style, color palette, and presentation.</p>

                    {error && <p>{error}</p>}

                    <BubbleRow
                        title="What fashion style do you want?"
                        items={options.appearance?.style_category}
                        selectedValue={formData.appearanceStyle}
                        fieldName="appearanceStyle"
                    />

                    <BubbleRow
                        title="What color palette do you want?"
                        items={options.appearance?.color_palette}
                        selectedValue={formData.appearancePalette}
                        fieldName="appearancePalette"
                    />

                    <BubbleRow
                        title="How do you want the post presented?"
                        items={options.appearance?.presentation}
                        selectedValue={formData.appearancePresentation}
                        fieldName="appearancePresentation"
                    />

                    <div className="button-group">
                        <button
                            onClick={() =>
                                flowType === "questionnaire"
                                    ? setScreen("referenceChoice")
                                    : goBackToChoice()
                            }
                        >
                            Back
                        </button>
                        <button onClick={() => setScreen("overallVibe")}>
                            Continue
                        </button>
                    </div>
                </div>
            )}

            {screen === "overallVibe" && (
                <div className="card">
                    <h1>Overall Vibe</h1>
                    <p>Choose the overall vibe you want for your music and caption.</p>

                    {error && <p>{error}</p>}

                    <BubbleRow
                        title="What vibe do you want for your music and caption?"
                        items={options.vibes}
                        selectedValue={formData.vibe}
                        fieldName="vibe"
                    />

                    <div className="button-group">
                        <button onClick={() => setScreen("styleQuestions")}>
                            Back
                        </button>
                        <button onClick={() => setScreen("questionnaire")}>
                            Continue
                        </button>
                    </div>
                </div>
            )}

            {screen === "questionnaire" && (
                <div className="card">
                    <h1>Music + Final Details</h1>
                    <p>Choose your music details.</p>

                    {error && <p>{error}</p>}

                    <BubbleRow
                        title="What music genre do you want?"
                        items={options.music?.Genre}
                        selectedValue={formData.musicGenre}
                        fieldName="musicGenre"
                    />

                    <BubbleRow
                        title="What music energy do you want?"
                        items={options.music?.Energy}
                        selectedValue={formData.musicEnergy}
                        fieldName="musicEnergy"
                    />

                    <BubbleRow
                        title="What music era do you want?"
                        items={options.music?.Era}
                        selectedValue={formData.musicEra}
                        fieldName="musicEra"
                    />

                    <div className="button-group">
                        <button onClick={() => setScreen("overallVibe")}>Back</button>
                        <button onClick={handleSubmit}>
                            Finish
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}

export default App;
