# SummerSync Project Template Repository

## About

Hello and welcome to SummerSync! This application was created by the Data Dwellers for CS3200 Database Design at Northeastern University during the Summer 2 semester of 2024. 

Data Dwellers Team Members:
- Gillian Scott
- Aidan Zucosky
- Ciara Hanley
- Lynna Truong
- Nubaha Ahsan

How to start the SummerSync application:
1. Clone the repository to your local machine, either through GitHub Desktop or the terminal.
2. Once cloned, open the 24su-3200-summer-sync repo in VSCode (or your favorite code editor).
3. Head to the file explorer and copy the ".env.template" file, paste it, and rename the new file to ".env".
4. Open the file and check that DB_NAME=summersync and update MYSQL_ROOT_PASSWORD with your own password.
5. In the terminal navigate to 24su-3200-summer-sync and check that you are can use docker by writing "docker --version".
6. Start (or build) the containers by writing "docker compose up -d". The containers "front-end", "mysql_db", and "web-api" should be running now.

To run SummerSync in your browser:
1. Navigate to ../24su-3200-summer-sync/app/src on your terminal and write "Streamlit run Home.py"
  OR
2. Type in your browser "localhost:8501"

We ask that all users please double check they have all the necessary ports and information downloaded, you can find this in requirements.txt.

## Current Project Components

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database-files` directory)

## User Personas

Within Summer Sync we have four users personas:
- Katy Ito, the guardian of a camper at a camp that uses SummerSync.
- Jackie Saturn, a camp counselor for a camp that uses SummerSync.
- Chad Cheese, a camp director for a camp that uses SummerSync.
- Stephanie Black, a member of the administrative team for SummerSync. 

### Tasks Pages and the Site!

Each Persona needs to get certain tasks done. Because of this you will find each task corresponds to a certain route, listed in Katy_routes.py Jackie_routes.py etc. Further than this you will then be able to correlate each function in a route to each page. These pages are dedicated to executing a certain task that will then be able to be done by that persona. You can access these by navigating our site! Feel free to explore our site to understand our work. You will also be able to find our database and entries in the data manually by going over to database files --> SummerSync.sql to fully understand the tables and how they work in tandem with one another. 

We hope you enjoy summersync and use it to its full pontential! 

### Watch our demo!
https://drive.google.com/file/d/1YCEA-vlbaWUKSX2zSPDt1SuG22RTpkmF/view?usp=sharing
