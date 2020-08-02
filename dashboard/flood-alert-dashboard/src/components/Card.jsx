import React from "react";

function Card(props) {
  var value;
  var request = new Request(
    "http://localhost:5000/api/v1.0/getData?datapoints=5000",
    {
      method: "GET",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  function getData() {
    setInterval(function () {
      fetch(request)
        .then((response) => response.json())
        .then(function (data) {
          return (value = data[data.length - 1].humidity);
        });
    }, 2000);
  }

  return (
    <div className="col-lg-2 col-md-4 mb-4 card-tab">
      <div className={props.color + " card  shadow h-100 py-2"}>
        <div className="card-body">
          <div className="row no-gutters align-items-center">
            <div className="col mr-2">
              <div className="text-xs font-weight-bold text-primary text-uppercase mb-1">
                {props.title}
              </div>
              <div className="h5 mb-0 font-weight-bold text-gray-800">
                {props.value}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Card;
