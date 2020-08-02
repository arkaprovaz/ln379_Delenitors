import React, { Component } from "react";
import CanvasJSReact from "../assets/canvasjs.react";
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

var dps = [{ x: 0, y: 0 }]; //dataPoints.
var xVal;
var yVal;
var updateInterval = 5000;
var apiURL = "";
var noDatapoints = 10;

function fetchData(apiURL) {
  apiURL = `http://localhost:5000/api/v1.0/getData?datapoints=${noDatapoints}`;
  var request = new Request(apiURL, {
    method: "GET",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
  });
  fetch(request)
    .then((response) => response.json())
    .then(function (data) {
      for (var i = 0; i < data.length; i++) {
        var yVal = data[i].wind_speed;
        var xVal = new Date(data[i].timestamp);
        dps.push({
          x: xVal,
          y: yVal,
        });
        console.log(yVal);
      }
    });
}
class WindSpeed extends Component {
  constructor() {
    super();
    this.updateChart = this.updateChart.bind(this);
  }

  componentDidMount() {
    fetchData(apiURL);
    setInterval(this.updateChart, updateInterval);
  }

  updateChart() {
    noDatapoints = noDatapoints + 1;
    apiURL = `http://localhost:5000/api/v1.0/getData?datapoints=${noDatapoints}`;
    fetchData(apiURL);
    xVal++;
    yVal++;
    dps.push({ x: xVal, y: yVal });
    if (dps.length > 10) {
      dps.shift();
    }
    this.chart.render();
  }
  render() {
    const options = {
      theme: "light2",
      animationEnabled: true,
      title: {
        text: "Wind Speed",
        fontColor: "#1cc88a",
      },
      axisX: {
        title: "time",
        gridThickness: 2,
        intervalType: "Seconds",
        valueFormatString: "hh TT K",
        labelAngle: -20,
      },
      axisY: {
        title: "Wind Speed Data(in km/h)",
      },
      data: [
        {
          type: "line",
          color: "#1cc88a",
          dataPoints: dps,
        },
      ],
    };

    return (
      <div className="container-fluid">
        <div className="row mt-3">
          <div className="col">
            <CanvasJSChart
              options={options}
              onRef={(ref) => (this.chart = ref)}
            />
            {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
          </div>
        </div>
      </div>
    );
  }
}

export default WindSpeed;
