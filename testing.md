# Testing 

## User Story Testing

### As a new user I would like reviews to be available to view without having to register or login.

1. As soon as the website is opened the homepage that is displayed contains all reviews currently published on the site.
1. No registration or login is required to see these reviews.

Steps Taken:

* Go to Projected Reviews website - https://movie-rating-project.herokuapp.com/
* Wait for page to reload.
* Observe that all reviews are visible despite not being registered or logged in.


### As a new user I would like information about the website to be readily available and easy to read.

1. In the Navbar present across all templates allows you to navigate to the about.html template.
1. Once clicked the website will render the template and display information about the website.

Steps Taken:

* From any page observe the 'About' button on the Navbar.
* Click the About link.
* Observe the new About page render.

### As a new user I would like to be able to search and see if a review has been written about a certain movie.

1. At the top of the review homepage there is a searchbar.
1. Entering in the title of a movie and pressing the search button will reload the review page.
1. Only those movies with the requested title will be displayed.

Steps Taken:

* Navigate to reviews page.
* Observe all reviews being displayed.
* Type in the title of a movie you wish to search for.
* Observe only the requested movies being displayed, unless there is no review in the database in which case a blank screen is displayed.
* Press the reset button beneath the searchbar to reload and display all reviews.
* Observe all reviews being displayed once again.

### As a new user I would like to be able to search and see if a review has been written about a movie by a certain director.

1. At the top of the review homepage there is a searchbar.
1. Enter the first name, surname or fullname of the desired director and press the search button which will reload the page.
1. Only those movies with the requested director will be displayed.

Steps Taken:

* Navigate to reviews page.
* Observe all reviews being displayed.
* Type in the first name, surname or fullname of the director you wish to search for.
* Observe only the requested movies by the requested director being displayed, unless there is no review in the database in which case a blank screen is displayed.
* Press the reset button beneath the searchbar to reload and display all reviews.
* Observe all reviews being displayed once again.

### As a new user I would like to be able to write a new review.

1. In the Navbar there is a link which allows you to 'Write A Review'.
1. If this button is not displayed then the user either needs to login or register.
1. Navigate to the either register or login, whichever is relevant, and enter correct username and password.
1. Once logged in this link should display.
1. Selecting the link will load a form with six fields which once filled out can be posted using the post button underneath the form, this will be loaded to the database and on the website.

Steps Taken:

* Ensure you are logged in or register as a new user.
* Click the link in the navbar labelled 'Write A Review'.
* Observe the form load.
* Fill out the fields with relevant information.
* Click 'Post' button.
* Observe the website navigating you back to the reviews page now featuring the new review.

### As a new user I would like to see that only I am able to edit my own reviews.

1. Must be logged into an account that has posted reviews already.
1. On the reviews page there will be a button displayed at the bottom of that user's already posted reviews labelled 'edit'.
1. Selecting the edit button will open the same kind of form with the fields already filled in.
1. Changing any of the fields of the review and then clicking select changes will alter the review in the database and on the website.

Steps Taken:

* Ensure you are logged in.
* Navigate to reviews page and find the reviews written by the logged in user.
* Observe the edit button beneath those reviews.
* Click the edit button which will render a form.
* Observe that this form is filled in with the review information.
* Make the desired changes.
* Click save changes or cancel to return to the reviews screen without changing any of the form.
* Observe the reviews page load with any changes made now being displayed.

### As a new user I would like to be able to delete any of my reviews.

1. Must be logged into an account that has already posted reviews already.
1. On the reviews page there will be a button displayed at the bottom of that user's already posted reviews labelled 'delete'.
1. Selecting the delete button will open a window asking you to confirm you wish to delete the review.
1. Once confirmed the review will be removed from the database and the website. 

Steps Taken:

* Ensure you are logged in.
* Navigate to reviews page and find the reviews written by the logged in user.
* Observe the delete button beneath those reviews.
* Click the button and observe a window asking if you are sure you want to delete your review.
* Selecting ok will remove the review.

## Technology Testing

### Devices Compatibility

* Lenovo Yoga 300
    * This device was used to test as a laptop and a tablet.
    
* iPhone 7
    * This device was used to test on a mobile device.




