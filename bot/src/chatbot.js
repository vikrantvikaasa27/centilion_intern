import React, { useState } from "react";
import "./chatbot.css"; // Import your CSS file for styling

function Chatbot() {
  const [userInput, setUserInput] = useState("");
  const [chatbotResponses, setChatbotResponses] = useState([]);

  const handleUserInput = (event) => {
    setUserInput(event.target.value);
  };

  const sendUserInput = () => {
    fetch("http://localhost:5000/chat", { // Replace with your Flask server URL
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ user_input: userInput }),
    })
      .then((response) => response.json())
      .then((data) => {
        setChatbotResponses([...chatbotResponses, { user: userInput, bot: data }]);
        setUserInput("");
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
      <div className="chatbot-responses">
        {chatbotResponses.map((response, index) => (
          <div key={index}>
            <div className="user-message">You: {response.user}</div>
            <div className="bot-message">Chatbot: {response.bot}</div>
          </div>
        ))}
      </div>
      <input
        type="text"
        placeholder="User Input"
        value={userInput}
        onChange={handleUserInput}
      />
      <button onClick={sendUserInput}>Send</button>
    </div>
  );
}

export default Chatbot;
