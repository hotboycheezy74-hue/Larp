import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [animate, setAnimate] = useState(false);
  const [showHome, setShowHome] = useState(false);

  useEffect(() => {
    const timer1 = setTimeout(() => {
      setAnimate(true);
    }, 1500);

    const timer2 = setTimeout(() => {
      setShowHome(true);
    }, 3000);

    return () => {
      clearTimeout(timer1);
      clearTimeout(timer2);
    };
  }, []);

  if (showHome) {
    return (
        <div className="home-screen">
          <h1>Home Screen</h1>
          <p>Your app starts here.</p>
        </div>
    );
  }

  return (
      <div className="screen">
        <div className={`welcome-box ${animate ? "move-up" : ""}`}>
          <h1 className="welcome-text">Welcome</h1>
          <p className={`sub-text ${animate ? "fade-in" : ""}`}>
            Let’s create your post
          </p>
        </div>
      </div>
  );
}

export default App;