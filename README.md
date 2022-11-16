# DevOps-Core-Fundamental-Project
This repository will contain all my work for QA project - DevOps Core Fundamental Project.
## Contents
* [Project Requirements](#Project-Requirements)
* [Project Plan](#Project-Plan)
    * [Database Structure](#Database-Structure)
    * [Trello Board](#Trello-Board)
    * [Risk Assessment](#Risk-Assessment)
* [App](#App)
* [Testing](#Testing)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)


## Project Requirements
Overall objective of this project is to create an application with CRUD (create, read, update and delete) functionality. MySQL database needed a minimum of two tables that share a relationship using the Flask framework and utilising all support tools, methodologies and technologies that encapsulate all core modules covered during training.

## Project Plan
I've decided to create an app that allows users to add their characters and track their objectives progress. I've started the whole proccess by making my database structure.  

### Database Structure
I've started the project by creating an ERD(Entity Relationship Diagram). As seen below I've decided to start with just two tables that would have a one to many relationship.  
![ERD](https://github.com/hivespaula/DevOps-Core-Fundamental-Project/blob/feature-objectives/images/ERD.PNG)

### Trello Board
Next step was the creation of a Trello board that would help me to have an overview of different stages in the project. It contains User Stories that the application had to fulfill which was then broken down into tasks in the backlog that had to be completed to meet the end goal. MoSCOW prioritisation was used to easily separate the features needed.  
![TrelloBoard-start](https://github.com/hivespaula/DevOps-Core-Fundamental-Project/blob/feature-objectives/images/TrelloBoard-start.PNG)  
At the end of the project deadline my board looked like below.  
![TrelloBoard-end](https://github.com/hivespaula/DevOps-Core-Fundamental-Project/blob/feature-objectives/images/TrelloBoard-end.PNG)

### Risk Assessment
Before starting to build the app, a risk assessment was done to identify potential risks and to propose control measures.  
![RiskAssessment](https://github.com/hivespaula/DevOps-Core-Fundamental-Project/blob/feature-objectives/images/RiskAssessment.PNG)  
User log in functionality did not get implemented in the project deadline.

## App
I've decided to keep everything simple and stick to having most of it on the main page.
Frontend was done via Jinja2 templates.  
![HomePage](https://github.com/hivespaula/DevOps-Core-Fundamental-Project/blob/feature-objectives/images/HomePage.PNG)  
When a user enters their character it would populate the data under the character entry form.  
![HomePage-characters](https://github.com/hivespaula/DevOps-Core-Fundamental-Project/blob/feature-objectives/images/HomePage-characters.PNG)  
Updating the character information redirects to a new page while delete function keeps the user on the same page.  
![UpdateCharacter](https://github.com/hivespaula/DevOps-Core-Fundamental-Project/blob/feature-objectives/images/UpdateCharacter.PNG)  
Not successfully implemented - list of objectives for each character

## Testing
Unfortunately no testing was done during the set time to complete the project.

## Known Issues
Connecting the two tables was my last challange since my second table that contained objectives had no user input, I was planning to add that functionality as well if time allowed for it. When the tables were connected the functionality to delete the character was broken but I've made it work in the end and no time was left for adding the html page to show it or testing.
No validators were added.

## Future Work
I would like to do my unit testing and add an option for user to change the objectives and be able to log in to their account.
There are also many little changes that I would like to add like the front end.
