# Bundu Bar and Restaurant

The Bundu Bar and Restaurant site is intended to be used as an advertising and management site for the restaurant to attract customers by providing compelling and informational content as well as a way to make a reservation online. The site also aids the restaurant staff in handling reservations for the restaurant and provides the ability to have more manageable interactions with customers.

## Contents

## Project Goals

## User Experience
### Epics
During the planning stage of the project I created 7 epics which I then broke down further into a total of 44 user stories. These can be found in the [project kanban board](https://github.com/users/Tony118g/projects/8) or they can be viewed individually through the links below.

1. [Initial Django Setup](https://github.com/Tony118g/bundu-restaurant/issues/1)
2. [User Account Management](https://github.com/Tony118g/bundu-restaurant/issues/2)
3. [User Reservation Management](https://github.com/Tony118g/bundu-restaurant/issues/3)
4. [Site Content Interaction](https://github.com/Tony118g/bundu-restaurant/issues/4)
5. [Staff Reservation Management](https://github.com/Tony118g/bundu-restaurant/issues/5)
6. [Staff Menu Management](https://github.com/Tony118g/bundu-restaurant/issues/6)
7. [User Menu Interaction](https://github.com/Tony118g/bundu-restaurant/issues/7)

### Customer User Stories
### Staff User Stories
### Site Owner User Stories

### Site Structure

#### Wireframes
I created basic wireframes of how I wanted the general layout of the site to look using [Balsamiq](https://balsamiq.com/). I created a wireframe for each main page layout and used it as a base to guide the way I structured and styled my pages. Although the site contains other pages, the layout is mostly the same and therefore I adopt their structure from these main wireframes.

##### Sign Up In Wireframe
![home page wireframe](documentation/sign-up-wireframe.png)

##### Log In Wireframe
![home page wireframe](documentation/login-wireframe.png)

##### Home Page Wireframe
![home page wireframe](documentation/home-wireframe.png)

##### Profile Page Wireframe
![home page wireframe](documentation/profile-wireframe.png)

##### Reservation Page Wireframe
![home page wireframe](documentation/reservation-wireframe.png)

##### Menu Page Wireframe
![home page wireframe](documentation/menu-wireframe.png)

##### Menu Modal Wireframe
![home page wireframe](documentation/menu-modal-wireframe.png)

##### Staff Dashboard Page Wireframe
![home page wireframe](documentation/dashboard-wireframe.png)

##### Staff Reservations Page Wireframe
![home page wireframe](documentation/staff-reservations-wireframe.png)

### Design Choices

### Project Management

## Features
### Existing Features
### Future Features

## Technologies Used
* [Balsamiq](https://balsamiq.com/wireframes/)
    * Used to create the wireframes during the planning stage of the project.
* [HTML5](https://html.spec.whatwg.org/)
    * Used to create structure and content for the site.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
    * Used to add cutoms styles to the HTML.
* [Django](https://www.djangoproject.com/)
    * The python framework used to develop the site.
* [Bootstrap](https://getbootstrap.com/)
    * The CSS framework used to develop the site.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    * Used to provide functionality to the site.
* [JavaScript](https://www.javascript.com/)
    * Used to enhance functionality and interactivity.
* [Cloudinary](https://cloudinary.com/)
    * Used to host media files.
* [ElephantSQL](https://www.elephantsql.com/)
    * Used to host the database used for the site in production.
* [Gitpod](https://www.gitpod.io/#get-started)
    * Used to create code/content and file structure for the respository.
* [GitHub](https://github.com/)
    * Used to store the repository.

## Python Packages Used


## Testing

## Deployment and Development
* The project was developed using [Gitpod](https://www.gitpod.io/#get-started) to create the code and overall file structure.
* The repository for this project is hosted on [GitHub](https://github.com/).

### Deployment
The project was deployed using [Heroku](https://id.heroku.com/login).

NB - to ensure a successful deployment of the project in Heroku, you need to ensure that you create a Procfile and a requirements.txt file.

Once you are certain that everything is ready to deploy the repo, you can do so through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
    * For this project, the unique name is "bundu-restaurant" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and click "Reveal config vars".
6. Add the config vars necessary for the project.
7. Navigate to the "Deploy" section by clicking the "Deploy" tab in the navbar.
8. Select "GitHub" as the deployment method and click "Connect to GitHub".
9. Search for the GitHub repository that you wish to deploy.
10. Click on "connect" to link the repository to Heroku.
11. Scroll down and click on "Deploy Branch" to manually deploy.
12. Once the app has deployed successfully, Heroku will notify you and provide a button to view the app.

NB - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys" in Heroku.

### Forking the Repository
To create a copy of the repository for viewing and editing without affecting the original repository you can fork the repository through the following steps:

1. In the "bundu-restaurant" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository in your own GitHub account.

### Cloning The Repository
To clone the repository through GitHub, follow these steps:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.
2. Select "HTTPS" in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

### The ElephantSQL Database
The [ElephantSQL](https://www.elephantsql.com/) PostgresSQL Database was used for this project.

To set up a database, follow these steps:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on "Create New Instance".
3. Enter a name for the instance (this is usually the name of the project.)
4. Select "Tiny Turtle (Free)" free plan.
5. The "Tags" field can be left blank.
6. Click "Select Region".
7. Select a data center near you.
8. Click "Review".
9. Ensure that all details are correct and then click "Create instance".
10. Once created, you can return to the dashboard and click on the instance created to view relevant details such as the database URL and password.

### The Cloudinary API
[Cloudinary](https://cloudinary.com/) is used in this project to store media assets. This is done due to the fact that Heroku does not store media files reliably.

To set up Cloudinary, follow these steps:

1. Login/sign up to Cloudinary.
2. Navigate to the dashboard to view the API Environment Variable.

NB - You can change your assigned cloud name to something more memorable.


## Credits
## Acknowledgements
