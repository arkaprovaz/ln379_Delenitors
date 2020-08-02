import React from "react";
import Navbar from "./components/Navbar";
import CardSection from "./components/CardSection";
import Rainfall from "./components/Rainfall";
import WaterLevel from "./components/WaterLevel";
import Temperature from "./components/Temperature";
import WindSpeed from "./components/WindSpeed";
import Pressure from "./components/Pressure";
import Humidity from "./components/Humidity";

function App() {
  return (
    <div className="wrapper">
      <div id="content">
        <Navbar />
        <CardSection />
        <Rainfall />
        <WaterLevel />
        <Humidity />
        <Temperature />
        <WindSpeed />
        <Pressure />
      </div>
    </div>
  );
}

export default App;
