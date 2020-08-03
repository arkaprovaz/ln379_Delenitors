import React from "react";
import Card from "./Card";

function CardSection() {
  return (
    <div className="container-fluid">
      <div className="row">
        <Card color="border-left-primary" title="Rainfall" value="in mm" />
        <Card color="border-left-info" title="Water Level" value="in m" />
        <Card color="border-left-danger" title="Humidity" value="in %" />
        <Card color="border-left-secondary" title="Temperature" value="in °C" />
        <Card color="border-left-success" title="Wind Speed" value="in km/h" />
        <Card color="border-left-warning" title="Pressure" value="in bars" />
      </div>
    </div>
  );
}

export default CardSection;
