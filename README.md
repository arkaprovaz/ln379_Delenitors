
# ln379_Delenitors
Official repository for problem statement number LN379 by Team Delenitors
## Problem Statement
- Development of IoT based advance Public Address and Flood Warning Systems across all Hydro Power project areas.
## Description
- We are looking for advance Public address and Flood Warning Systems across all Hydro Power project areas. IoT sensors can be used for generating advance flood warning across hydro power project areas. IoT sensors data can be used with Public Address system to generate alarm.
## Problems tackled by us:
 - Due to construction of dams, the river under consideration(Teesta) has changed its course over time. This causes a problem, as historical data cannot be used.
 - There is a communication gap between different departments, which causes opening of dam gates without considering all the factors.
 - Delay in response.
 - Ineffective ways of public address.
## How we solved it:
 - We have used live data from our device, which is placed at different intervals throughout the river.
 - Our dashboard in such a way that officials from different departments can view the different patterns and take necessary action. (This can be done from the comfort of home during emergency at unforseen hours)
 - We have used complex mathematical calculations and machine learning that not only reduces response time, but also considers other factors like rainfall, water level, inflow, outflow, pressure on the walls of dam. Which is then divided into different levels to issue the level of flood.
 - We have used every mode of addressal, that reaches people, irrespective of the type of phone they use, and distance from the hydel project.
## Technology stack:
### Hardware tools: 
 - LoRa Gateway
 - Weather station
 - Ultrasonic water level sensor
 - Raspberry Pi
 - Arduino UNO board
 - 16 x 2 RGB LCD
### Software tools:
 - Microsoft Azure Cloud Service
 - Twilio - Call and SMS
 - SendGrid - Email Service
 - Twitter
 - MQTT
 - SQL- Database
### What have we made?
- We have fabricated a system using sensors and LoRa Wan, which will be placed in different hops throughout the length of the river(where the hydel project is located). Our device will pick real-time data, which will give us information about the weather condition, water-level and other required factors. This in turn will help us in predicting if the water level is safe, if not, alert will be generated automatically.
### Workflow
#### Hardware workflow:
![Annotation 2020-08-02 095416](https://user-images.githubusercontent.com/32809211/89115480-42e22d00-d4a6-11ea-9b92-9fe38d03ca8b.png)
### Flow
![Flow chart](https://user-images.githubusercontent.com/32836687/89149099-37136b00-d579-11ea-8810-5190830833a1.jpg)

### Regression workflow:
![Workflow](https://user-images.githubusercontent.com/32809211/89119291-dcbbd100-d4ca-11ea-84a2-76cc4f1cf29f.png)

### Accidental blockage detection workflow:
![Accidental blockage detection](https://user-images.githubusercontent.com/36500005/89173203-82417400-d5a1-11ea-8b85-45e3da848aaa.jpg)


### [Demo video](https://drive.google.com/file/d/1t1gvS0L7W64pgO0EJqvrxDgXvRzz4N6p/view?usp=sharing)

### What are our public address measures?
 - As soon as the water levels are above danger level, the flood alert will be generated.
 - Mails will be sent to every officials.
 - A tweet will also be sent.
 - A light pattern and siren will be switched on to alert people living nearby. 
 - A call and SMS will also be sent along with help-line numbers for rescue(if needed).
### Why is our solution different?
 - Using LoRa, we not only reduce the set-up cost, we also save power and it becomes easier to connect to nodes, while setting up our hardware throughout the entire length of the river.
 - We have ensured 'last-man-communication',we have used every mode of communication, this ensures people without a smartphone also gets the message. We have also included help-line numbers, we have seen that most people are devoid o shelter during such disasters.
 - Our solution is highly secured, and there is no chance of data-breach.
 - We have made use of all the recent technologies, this ensures that not much work in manual, which reduces the chances of error.
## [IDEA PPT](https://www.canva.com/design/DAEDvV7yrZw/tp2auSNBxI-MPJzJHSykeQ/view?utm_content=DAEDvV7yrZw&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu)
## [final_mentoring.pptx](https://github.com/arkaprovaz/ln379_Delenitors/files/5015443/final_mentoring.pptx)


### Alert Screenshots
![Screenshot](https://user-images.githubusercontent.com/32836687/89127259-c97c2600-d509-11ea-8276-3a43b9cb766f.jpg)


## Technologies that we have used:
![Technologies](https://user-images.githubusercontent.com/32836687/89127100-a4d37e80-d508-11ea-9800-bb4129e2c5db.jpg)

