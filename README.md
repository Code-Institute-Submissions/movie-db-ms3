# Projected-Reviews-ms3


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
  
## Features
  
### 2.1 Navigation Bar
  
* A bar at the top of the website that helps to easily navigate between the pages. All pages have the same navigation bar to maintain consistance appearance. The navbar has some elements that can only be seen dependant on whether or not the user is logged in. When not logged in the navbar will show 'Login' and 'Register', when logged in these will be replaced by 'Write A Review' and 'Logout'.
  
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


  
