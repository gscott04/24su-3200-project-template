# SummerSync Project Template Repository

## About

Hello and welcome to SummerSync! This application was created by the Data Dwellers for CS3200 Database Design at Northeastern University during the Summer 2 semester of 2024. 

Data Dwellers Team Members:
- Gillian Scott
- Aidan Zucosky
- Ciara Hanley
- Lynna Truong
- Nubaha Ahsan

We ask that all users please double check they have all the necessary ports and information downloaded, you can find this in requirements.txt. In order to fully ensure that everything is running you must also run and compose your docker. You can do this in your terminal writing the statement "docker compose up -d". 

To start the application either:
1. Enter the file ../24su-3200-summer-sync/app/src on your terminal and write "Streamlit run Home.py"
  OR
2. Type in your browser "localhost:8501"

## Current Project Components

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database-files` directory)

## User Personas

Within Summer Sync we have four users personas. We have Katy Ito, a Guardian of a child at a camp using the summer sync site, Jackie Saturn, A camp counselor working at one of our many camps, Chad Cheese, A Camp Director here at summersync and Stephanie Black the head of Outreach here at summersync. 

### Tasks Pages and the Site!

Each Persona needs to get certain tasks done. Because of this you will find each task corresponds to a certain route, listed in Katy_routes.py Jackie_routes.py etc. Further than this you will then be able to correlate each function in a route to each page. These pages are dedicated to executing a certain task that will then be able to be done by that persona. You can access these by navigating our site! Feel free to explore our site to understand our work. You will also be able to find our database and entries in the data manually by going over to database files --> SummerSync.sql to fully understand the tables and how they work in tandem with one another. 

We hope you enjoy summersync and use it to its full pontential! 

### Watch our demo!
https://drive.google.com/file/d/1YCEA-vlbaWUKSX2zSPDt1SuG22RTpkmF/view?usp=sharing
