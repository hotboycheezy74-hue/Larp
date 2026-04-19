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
          <h1>Larper</h1>
          <p>Your larp starts here.</p>
        </div>
    );
  }

  return (
      <div className="screen">
        <div className={`welcome-box ${animate ? "move-up" : ""}`}>
          <h1 className="welcome-text">Lets Larp</h1>
          <p className={`sub-text ${animate ? "fade-in" : ""}`}>
            Let’s larp your post
          </p>
        </div>
      </div>
  );
}

export default App;