# weatherAPI
CS308 homework

## Overview

This is a simple Weather API done as a homework for CS308 course. It provides three endpoints for current, historical or forecast weather data for a wanted city.

## How to run 

Clone the repository to your desired directory. 
Open the ../weatherAPI/weatherAPI/ directory into the IDE of your choice. (In my case it was VSCode)
What you need to have installed on your machine: python, pip, django and django rest framework. 
For this you may use the following commands:  
`pip install django`  
`pip install djangorestframework`.  

To run the actual application use the following command in the terminal of the app's directory:  
`python manage.py runserver`.  
You will be shown a localhost address with which you can open the API app.  

To access the current weather use the /weather/current/ endpoint.  
To access the forecast weather use the /weather/forecast/ endpoint.  
To access the history weather use the /weather/history/ endpoint.  

More details on what type of JSON file is needed as a request for each of the mentioned can be found in the Postman collection.
