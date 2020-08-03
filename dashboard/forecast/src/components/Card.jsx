import axios from "axios";
import React, { useState } from "react";

function Card() {
  const [values, setValue] = useState(null);

  const apiURL =
    "http://localhost:5000/api/v1.0/getPredData?city=siliguri,WB,IN";

  var isLoaded = false;

  const fetchData = async () => {
    const response = await axios.get(apiURL);
    isLoaded = true;
    setValue(response.data);
  };

  if (isLoaded === false) {
    fetchData();
  } else {
    setInterval(fetchData, 21600000);
  }

  return (
    <div className="wrapper">
      <div id="content">
        <h1 className="text-center">Realtime Flood Prediction</h1>
        <div className="row">
          {values &&
            values.map((value) => {
              return (
                <div className="col-md-4 mb-4 mr-0.5 card-tab">
                  <div className=" card  shadow h-200 py-4">
                    <div className="card-body p-2">
                      <div className="row no-gutters align-items-center">
                        <div className="col mr-2">
                          <div className="text-xs font-weight-bold text-primary text-uppercase mb-1">
                            Date : {value.date}
                          </div>
                          <div className="h5 mb-0 font-weight-bold text-gray-800">
                            Rainfall : {value.totalprecip_in}mm
                            <br />
                            Waterlevel Rise : {Math.abs(value.pred_wlevel)}m
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })}
        </div>
      </div>
    </div>
  );
}

export default Card;
