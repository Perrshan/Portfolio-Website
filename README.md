# Overview

I wanted to test out the capabilities of using Django with Python to make a website rather than just hard coding a website using only web development coding languages. I was able to learn a lot and was very pleased with the tools that Django offers to make websites much easier.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

- Home page: The home page is opened by default when the user first clicks on the link. It has information about me with a picture. This page is pulled up using the Django url pattern list, but has simple html code to open all of the content. The `index.html` is accessed through the index view.
- Portfolio Page: The portfolio page is opened once the user clicks the portfolio link in the header or footer of any page using the url pattern list. The page runs through the model `Project` which cycles through every added project displaying the project name, description, picture, and link which are all attributes of that model using a for loop. The `portfolio.html` is opened using the `portfolio_view` view.
- Comment Page: The comment page is opened once a user clicks on the comment button below every project on the portfolio screen using the url pattern list. The page runs through every comment that has been added and will display them on the screen along with a text box to type and submit comments. There is a button to like the project as well. I also added the picture of each project to be displayed. The comments and likes are stored in models that record attributes describing the data. The `project_detail.html` is opened by the `project_details` view.


# Development Environment

- Python
- Django
- Django Admin
- HTML and CSS
- Visual Studio Code
- Google Chrome Web Browser

# Useful Websites

* [Django Tutorial Walkthrough](https://docs.djangoproject.com/en/5.0/)
* [Django Tutorial](https://www.tutorialspoint.com/django/index.htm)

# Future Work

* Add more features with the like and comment pages like total counts of likes and comments.
* Clean up the CSS a to make the website more appealing.
* Look into how Django can further automate the website making progress and see what tools I failed to use my first time using the software.