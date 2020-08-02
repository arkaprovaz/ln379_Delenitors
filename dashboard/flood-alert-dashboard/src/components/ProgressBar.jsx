import React from "react";

function ProgressBar(props) {
  return (
    <div className="container-fluid">
      <div className="col">
        <div className="progress progress-sm mr-2 mb-3">
          <div
            className="progress-bar bg-info"
            role="progressbar"
            style={{
              width: "90%",
              ariaValuenow: "50",
              ariaValuemin: "0",
              ariaValuemax: "100",
            }}
          ></div>
        </div>
      </div>
    </div>
  );
}

export default ProgressBar;
