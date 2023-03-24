# Bundu Bar and Restaurant

The Bundu Bar and Restaurant site is intended to be used as an advertising and management site for the restaurant to attract customers by providing compelling and informational content as well as a way to make a reservation online. The site also aids the restaurant staff in handling reservations for the restaurant and provides the ability to have more manageable interactions with customers.

## Contents

## Project Goals
This site was developed for a fictional small restaurant to provide an easier way to manage reservations for both the restaurant staff and customers. The site also employs functionality for staff to manage the menu advertised to customers which allows control over what they offer as a restaurant.

This version of the project includes necessary functionality for customers and staff to provide a pleasant user experience. In the future, the site may be further developed to include more features that may become necessary as the restaurant grows.

This project was developed to showcase competency in web development particularly using the Django framework and agile methodology. It is purely for educational purposes.

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

### User Stories
The epics mentioned above were further broken down into user stories. These stories were developed using MoSCoW (must have, should have, could have, and won't have) prioritization and each story was assigned a label in accordance with its level of priority. Each story was also assigned user story points using labels. I assigned the story points based on my best estimation of the time and difficulty of completing each user story.

As well as labels, each user story has acceptance criteria and tasks associated with it. This was a great way of ensuring all requirements for each story were known as they were developed. This also helped keep track of progress.

A few user stories were created based on an ideal scenario of the project while it was known that it was highly unlikely they would be completed for this first development and release of the site. These stories were not essential to the project however I may revisit them in a future development along with any other features that may be required as the restaurant grows.

All user stories can be found in the [project kanban board](https://github.com/users/Tony118g/projects/8)

Below are the completed user stories for this version of the project's release listed by epic.

* Epic - initial django setup
    * As a developer I want to set up Django and install the initial supporting libraries needed so that I can begin development of the site.
    * As a developer I want to set up the environment to secure secret configuration variables so that I can ensure sensitive data is kept private.
    * As a developer I want to deploy the site to Heroku so that I can ensure the site works in a production environment and share the completed site publicly.

* Epic - user account management
    * As a user I can register an account so that I can log in and out of the site.
    * As a user I can log in and logout of my account so that I can use the site and keep my account secure
    * As a user I can view my account details so that I can be sure that I am using my account and in case I forget my details.
    * As a user I can edit my account details so that I can keep my account information up to date.
    * As a user I can delete my account so that I can remove my details and stop using the site at my will.
    * As a user I can change my password so that I can keep my account secure.
    * As a user I can reset my password so that I can still access my account if I forget my password.

* Epic - site content interaction
    * As a user I can view my account page so that I can view and manage information and reservations specific to me.
    * As a user I can view the restaurant menu so that I know what food options are available.
    * As a staff member I can view the staff dashboard so that I can manage the restaurant site and reservations.
    * As a site owner I want to restrict certain features to registered users so that it encourages people to register to the site and ensures reservations are recorded for known customers.
    * As a site owner I want to restrict certain features to staff members so that I can ensure unauthorized users cannot tamper with the running of the site.

* Epic - user reservation management
    * As a user I can make a reservation request so that I can reserve a time and place in the restaurant.
    * As a user I can receive feedback on whether my reservation has been approved or not so that I can visit the restaurant or make a new reservation.
    * As a user I can view my reservations so that I can be sure of my reservations.
    * As a user I can edit my reservations so that I can change reservation details if I want to.
    * As a user I can cancel my reservation so that I can avoid unnecessary reservations if I change my mind.

* Epic - staff reservation management
    * As a staff member I can view all reservations in categories so that I can manage all reservations that come through the site.
    * As a staff member I can view all reservations for the current date so that I know what to plan for on the day at the restaurant.
    * As a staff member I can search reservations according to their date so that I can find out the reservation status of the restaurant on a given date.
    * As a staff member I can search reservations pertaining to a name so that I can find out the reservation status of the restaurant for a given name.
    * As a staff member I can approve or deny reservations so that I can be in control of reservations at the restaurant.

* Epic - staff menu management
    * As a staff member I can add a menu item so that I can keep the menu up to date with new options.
    * As a staff member I can edit menu items so that I can ensure the correct menu information is displayed.
    * As a staff member I can delete menu items so that I can remove old menu items that are no longer relevant.
    * As a staff member I can mark a menu item as unavailable so that I can still display the item but inform customers that it is currently unavailable.

* Epic - user menu interaction
    * As a user I can view images of menu items so that I can visualize the food item.

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
I used agile methodology throughout the development of this project utilising GitHub projects and issues. 
Using issues I was able to create epics and user stories which I could then label and categorize. I then added these 
issues to the project kandban board where I could easily manage the development process. I found this extremely useful 
in helping me break down the development process into individual sections and stages which improved the overall efficiency and quality  of development.

Although this project was developed by myself individually, the agile principles enabled me to track my progress in all aspects and ensure the site can be easily maintained in future. If a team were to collaborate on the project, this agile aproach would be extremely beneficial.
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
* [asgiref](https://pypi.org/project/asgiref/)
    * A standard for Python asynchronous web apps and servers to communicate with each other.
* [cloudinary](https://pypi.org/project/cloudinary/)
    * Used for image management.
* [coverage](https://pypi.org/project/coverage/)
    * Used to measure code coverage for automated tests.
* [crispy-bootstrap-5](https://pypi.org/project/crispy-bootstrap5/)
    * The bootstrap5 template pack used for django-crispy-forms.
* [dj-database-url](https://pypi.org/project/django-database-url/)
    * Used to parse the database url in the production environment.
* [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/)
    * Used to provide Cloudinary storages for media files as well as management commands for removing unnecessary files.
* [Django](https://pypi.org/project/Django/)
    * The framework used to develop the project.
* [django-allauth](https://pypi.org/project/django-allauth/)
    * Used for the site's authentication system.
* [django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
    * Used to render styled forms.
* [gunicorn](https://pypi.org/project/gunicorn/)
    * A Python HTTP server for WSGI applications used to run the Python application concurrently.
* [oauthlib](https://pypi.org/project/oauthlib/)
    * A framework used that implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
* [psycopg2](https://pypi.org/project/psycopg2/)
    * Used as a PostgreSQL database adapter for the Python programming language.
* [PyJWT](https://pypi.org/project/PyJWT/)
    * A Python implementation of RFC 7519.
* [python3-openid](https://pypi.org/project/python3-openid/)
    * OpenID support for modern servers and consumers.
* [pytz](https://pypi.org/project/pytz/)
    * Allows accurate and cross platform timezone calculations.
* [requests-oauthlib](https://pypi.org/project/requests-oauthlib/)
    * OAuthlib authentication support for Requests.
* [sqlparse](https://pypi.org/project/sqlparse/)
    * A non-validating SQL parser for Python.


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
