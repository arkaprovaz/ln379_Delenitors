import React from "react";
import Card from "./components/Card";
import Navbar from "./components/Navbar";

function App() {
  return (
    <div>
      <Navbar />
      <div className="wrapper">
        <div id="content">
          <Card />
        </div>
      </div>
    </div>
  );
}

export default App;
