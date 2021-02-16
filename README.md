# Projected-Reviews-ms3

[Live website link here](https://movie-rating-project.herokuapp.com/)

![Website displayed on multiple devices](/static/screenshots/multi-device-movies.png)

## UX

### 1.1 Overview
* This project was started with the idea of introducing a wider audiences to movies they may not have heard of or seen before. I have always had a passion for films and wanted to try and share my own personal experiences with movies that other users may not have seen. I like the idea of a group of like-minded people supplying their own experiences to create a community introducing each other to their favourite, or least favourite movies. The simple design makes the information easy to read without being overwhelmed by lots of graphics and colours.

### 1.2 Project Goals
* I wanted to create a simple website that was focused on the films and the user's own experiences with those films. The simple colour scheme relies on a mostly grey and red as an homage to the colours of my own local cinema that I visit often. The website is designed to allow users to post a review of whatever movie they like, even if that movie has already been reviewed by another user. This allows the website to constantly evolve and change dependant on who is using it.

### 1.3 User Goals
* A user would want a simple intuitive design that is easy to navigate and pleasant to look at.
* A user would want a simple form to help them write their reviews in a structured way.
* A user would want to be able to post their review immediately for others to view.
* A user would want to be able to change their review at any time should their opinions change.
* A user would want to be able to remove their own reviews at any time.

### 1.4 Colour Scheme
* Website Colours:
  * #9e9e9e - Navbar, Review Cards, Container around Login, Register, Write Review and Edit Review
  * #616161 - Search Button
  * #424242 - Edit button on user's review
  * #c62828 - Delete button on user's review, Flash Messages, Callout heading and subheading, About heading, Join Our Community button, Login card, Register card, Register Here button, Login Here button
  * #b71c1c - Write A Review form
  * #d32f2f - Search Icon, reset button on Search function
  * #ffeb3b - Rating stars
  * #ffffff - All button text, most font awesome icons, nav text, write/edit review text 
  * rgba(158,158,158, 0.4 - About Container

* Logo Colours:
  * #ffffff - Background and buttons
  * #fce464 - Light colour and button on projector
  * #000000 - Border and lens
  * #8c8c8c - Main body of projector
  
## User Stories

* As a new user I would like reviews to be available to view without having to register or login.
* As a new user I would like information about the website to be readily available and easy to read.
* As a new user I would like to be able to search and see if a review has been written about a certain movie.
* As a new user I would like to be able to search and see if a review has been written about a movie by a certain director.
* As a new user I would like to be able to write a new review.
* As a new user I would like to see that only I am able to edit my own reviews.
* As a new user I would like editing a pre-existing review to be easy to understand.
* As a new user I would like to be able to delete any of my reviews. 
  
## Features
  
### 2.1 Navigation Bar
  
* A bar at the top of the website that helps to easily navigate between the pages. All pages have the same navigation bar to maintain a consistant appearance. The navbar has some elements that can only be seen dependant on whether or not the user is logged in. When not logged in the navbar will show 'Login' and 'Register', when logged in these will be replaced by 'Write A Review' and 'Logout'.
  
### 2.2 Search Bar
  
* A search function at the top of the home page which allows the user to search for a film by its title or by its directors name.

### 2.3 User Registration and Authentication

* Users are able to create an account provided the username does not already exist. A flash message will appear to inform the user if their selected username is unavailable.

### 2.4 Login and Logout Functionality

* If user already has an account they can login using their already registered username and password. The user can then logout which will clear their session cookie and take the website back to before you were logged in.

### 2.5 Write A Review

* The user can navigate to a form which will allow them to create a new review and post it to the database to be displayed on the website. Two of the fields are number fields the rest are text or textarea fields.

### 2.6 Edit A Review

* A button will be present on all reviews written by the logged in user which allows the user to edit their reviews. The button will redirect the user to another form with the same fields as the Write A Review form already filled with the pre-existing inputs, these can be easily changed and the updated versions can then be save to the database.

### 2.7 Delete A Review

* A button will also appear on the users reviews to allow the user to remove their own reviews when logged in. When you click on the delete button you are asked to confirm if you are sure you want to delete the review before it will be removed.

### 2.8 Login Check

* Editing and deleting reviews will only be available to the user who is logged in and other users will not be able to change others reviews.

### 2.9 Known Bugs

* The window.confirm() that asks for confirmation when deleting a review does not cancel even if you press cancel.

## Technology Used

* HTML5 - The project uses templates are all created using HTML.
* CSS3 - The project uses CSS to style the HTML elements.
* JavaScript - The project uses JavaScript for mobile sidenav and delete confirm window.
* Python - The project uses Python to run the application.
* Flask - The project uses Flask as a framework.
* Jinja - The project uses Jinja as the programming language.
* MongoDB - The project uses MongoDB to host its database.
* Google Fonts - The project uses Google Fonts for the headings and subheadings in the project.
* Materialize - The project uses Materialize as a framework for layout and responsive elements.
* Font Awesome - The project uses Font Awesome icons to help illustrate certain functions throughout the project.
* GitHub - The project uses GitHub repository to store the project and for version control.
* GitPod - The project uses GitPod as a terminal to build the website.
* Git - The project uses Git to save the project and push the project into the GitHub repository.
* Heroku - The project application is deployed using Heroku.

## Testing

Testing is documented in separate file - [testing.md](/testing.md)

## Deployment

This project was coded using Git and GitPod, the following steps were made to save code and add it to GitHub repository:
 1. Use git add to move code from the workspace to staging area.
 1. Use git commit to save files to a local repository with a message to say what has been changed since previous commit.
 1. Use git push to move the files from a local repository to a remote repository like GitHub.

To deploy this page to Heroku from its [GitHub repository](https://github.com/RDGrover/movie-db-ms3), the following steps were taken:
 1. Go to the **Heroku Dashboard** and create a **New App** with the region set to **Europe**.
 1. In the **Settings** tab of your app click **Reveal Config Vars**.
 1. Enter the required environment variables, **IP**, **PORT** and **MONGO_URI**.
 1. In your IDE of choice create a **env.py** containing the **MONGO_URI** and add it to the **.gitignore**.
 1. In your IDE of choice create a **requirements.txt** by using the command **pip freeze -local > requirements.txt**.
 1. In your IDE of choice create a **Profile** by using the command **echo web: python app.py > Procfile**.
 1. Go to the **Deploy** tab and select **Heroku Git**.
 1. In your IDE of choice use the command **git push heroku master**.

Note: The [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) will need to have been downloaded and installed to push from command line.

To deploy locally use the following steps:
 1. Go to [GitHub repository](https://github.com/RDGrover/movie-db-ms3)
 1. Click the **Clone** or **Download** button and copy the URL into the address box https://github.com/RDGrover/movie-db-ms3.git
 1. Open your terminal and cd to the path where you want to run the clone of the repository.
 1. Type into the terminal git clone https://github.com/RDGrover/movie-db-ms3.git.
 1. Once the repository has been downloaded to the designated folder, you can run the files through the browser to check if it is working.


