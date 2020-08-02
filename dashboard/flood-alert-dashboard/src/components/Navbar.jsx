import React, { useState } from "react";

function Navbar() {
  const nowTime = new Date().toLocaleTimeString();
  const date = new Date().toJSON().slice(0, 10).replace(/-/g, "/");

  const [time, setTime] = useState(nowTime);

  function updateTime() {
    const newTime = new Date().toLocaleTimeString();
    setTime(newTime);
  }
  setInterval(updateTime, 1000);

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <button
          className="btn btn-dark d-inline-block d-lg-none ml-auto"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <i className="fas fa-align-justify"></i>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="nav navbar-nav ml-auto">
            <li className="nav-item">
              <a href="javascript:void(0)" className="nav-link">
                {time}
              </a>
            </li>
            <li className="nav-item">
              <a href="javascript:void(0)" className="nav-link">
                {date}
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="javascript:void(0)">
                Device ID - 1
              </a>
            </li>
            <li className="nav-item">
              <a
                className="nav-link"
                href="https://upbeat-murdock-cf6b3c.netlify.app/"
              >
                Control Panel
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
