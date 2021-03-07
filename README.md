
![Bkawaii Creations](/media/bkawaiicreations.jpg)


------------------------------------------
**Full Stack Frameworks with Django**
------------------------------------------

This is my 4th Milestone project for Code Institute. I build my own e-commerce web application called Bkawaii Creations. ‘Kawaii’ means Cute or Lovely in Japanese. 
With this web application I sell my own unique handmade Kawaii Facemasks and Nail Art products.

By creating this web application , I want to show my skills in building a e-commerce website. 
It is a growing market and e-commerce web applications are getting more and more in demand.

This e-commerce web application is complete with:
* product search and filter functionality.
* A functional payment system.
* An authentication system including email confirmations and user profiles.
* Real-time notifications that guide the user's experience.
* And the ability to give store owners the ability to add and delete products in the online store.

Click [here][DEMO] for my deployed project hosted on Heroku.


(Mockup of my web app)

**UX**

**User stories**

User stories
* As a user : As a new visitor to BKawaii Creations, I want the page to be easily navigated.
* As a user:  I want clear instructions on how to view all the products and categories. 
* As a user: I want the web application to respond quickly to my interaction.
* As a user: I want a search option so I can quickly find the product I'd like.
* As a user: I want to be able to purchase these products easily, and pay for them online.
* As a user: I want the payment service to be easy and clear.
* As a user: I want to register and login on the web application.
* As a user/shop owner: I want to add, edit and delete products in the online shop

Visitor Goals
The target audience to the web store would be:
* Fans of Kawaii Facemasks
* Fans of Kawaii Nail Art press-on nails
* Fans of Kawaii Nail Art palettes

**Surface**
* For the surface plane I wanted the design to be pastel coloured and fun. These are the most common used kawaii colours.
* The colors of my website are : ……….
* The images used for my products are photographed by myself.
* I choose the ……….google font for my text on the website.
* Bkawaii creations logo was designed by myself on canva.com

**Skeleton**

I created the wireframes using the program “Balsamiq”. 
Click [here][a] for my BKawaii Creations wireframes.

**Layout and existing features**
This is a multi-page layout. 
There are five different templates used:
1. Base template for the home page with login, registration, search engine and shoppingbag. On the Homepage you see a images gallery, about section and footer. The footer displays on every template.
2. Bag template used for the shopping bag page, cart and secure checkout/purchase form.
3. Checkout template used for the cart, checkout and payment forms. 
4. Products template to view the products and product details
5. Profiles template for login, registration and product admininstration

Surface
* For the surface plane I wanted the design to be pastel coloured and fun. These are the most common used kawaii colours.
* The colors of my website are : ……….
* The images used for my products are photographed by myself.
* I choose the ……….google font for my text on the website.
* The buttons are purple coloured and simple. Each button has a text description of it, describing to the user what it's function is.
* Bkawaii creations logo is designed by myself on canva.com

Features Left to Implement
* A wishlist, where the user can pick products and "favorite" them, before deciding to add them to the cart or not. 
* Securing the views for superusers and customers
* Setting up real confirmation emails

Challenges

I worked with Git branches for the first time in this project. It was difficult at first and I got scared merging my git branches to my master branch. I was afraid my code would not work anymore. But with the help of this video tutorial: https://www.youtube.com/watch?v=S2TUommS3O0  everything went well with merging my git branches, until I encountered a problem when I went merging my profiles branch to my master. Is was a merge conflict with my binary file db.sqlite3. 
I could not resolve the conflict in github with a pull request.
So I searched for a solution on google and finally discoverd this tip on https://lostechies.com/joshuaflanagan/2010/01/29/how-to-resolve-a-binary-file-conflict-with-git/
I had no git merge conflicts anymore and my profiles app was added to my master branch. The only thing was, that I had to create a new superuser to gain access to my django administration.



Main Technologies Used

Languages used
* This project uses HTML, CSS, JavaScript and Python programming languages.

Tools used
* Balsamiq to create the wireframes for this project.
* Django as python web framework 
* Git to handle version control.
* GitHub to store the project code remotely.
* PIP for installation of tools needed in this project - pip3 install django - pip3 install django-allauth - pip3 install pillow - pip3 install django-crispy-forms - pip3 install django-countries
* Stripe as payment platform to validate and accept credit card payments securely.
* Heroku for deployment
* Django Crispy Forms to style django forms.

Libraries utilised
* Google Fonts to style the website fonts.
* FontAwesome to provide icons for the online store.
* Bootstrap 4 to simplify the structure of the website and make the website responsive easily.
* jQuery

Databases

Databases used
During development on my local machine I worked with the standard sqlite3 database installed with Django. On deployment, the SQL database provided by Heroku is a PostgreSQL database.

Testing

Manual User testing:
This was the primary method of testing the application. I tested the app manually myself and asked relatives to go to my website and give his feedback.

(link to view PDF of testing functionality throughout my web application)

Responsive design

Lola's Cookbook was tested on the Chrome browser and on multiple mobile devices (iPhone 5, 6, 7, 8, iPad, Ipad-pro, Iphone X, Moto G4, Galaxy S5, Pixel 2 and Pixel2XL) to ensure compatibility and responsiveness.

Below are the list of Internet Browsers that were used to test the display of the website:
1. Google Chrome (Version 77.0)
2. Mozilla Firefox
3. Internet Explorer 11
Manual testing was carried out using the above browsers. No bugs or display issues.

Below are the list of websites I used to test the HTML, CSS, JS and Python code:
1. W3C HTML Validator This is a HTML online validitor.
2. W3C CSS Validator This is a CSS online validitor.
3. CSS Lint CSS Lint is an open source CSS code quality tool I used.
4. https://extendsclass.com/python-tester.html Python Syntax Checker from extendsclass.com. Python checker allows to check your Python code syntax (Python 3), and find Python errors.

Deployment

Deployment
The project is stored in a GitHub repository and hosted on Heroku.

I followed the next steps to deploy Bkawaii Creations on the GitHub pages:
* Log into GitHub.
* Select Sweetzia/bkawaii_creations in the repository list.
* Go to Settings
* Scroll down to the GitHub Pages section.
* Select the Master Branch
* On selecting Master Branch the page is automatically refreshed.
* The link can be retrieved to the deployed website.

I followed the next steps to host Bkawaii Creations on Heroku:
* Created a new application using the Heroku dashboard.
* Go to settings.py in gitpod bkawaii creations and added heroku database settings
* $ pip3 manage.py showmigrations
* $ Pip3 manage.py migrate
* Removed Heroku database settings, so  my database URL wouldn't end up in version control.
* pip3 installed gunicorn and added a Procfile, to tell Heroku to create a web dyno, which will run unicorn and serve my django app.
* temporarily disable collectstatic by using: $ heroku config:set DISABLE_COLLECTSTATIC=1 —app bkawaii-creations
* Log into Heroku via the gitpod terminal using '$ heroku login -i' and follow the on screen instructions to log in.
* Connect GitHub to Heroku in deployment method in Heroku
* $ heroku git:remote -a bkawaii-creations
* Deploy project to Heroku in the Gitpod terminal using '$ git push heroku master'.
* Create SECRET_KEY and add it with the Config Vars in Heroku.
* "Manual Deploy", select the master branch then click "Deploy Branch"
* Created AWS S3 bucket to store static files and media images.
* Once the build is complete, click on the "View app" button.
* Open app in Heroku, succesfully deployed app!


Credits Content 
The text content on the website was written by me.

Media
* All my own handmade product images were photographed by myself.

CODE used from:
* The Boutique Ado Project from Code Institute module 12
* ……..
* …….

Acknowledgements:
* The final milestone project from haydal810: https://github.com/Code-Institute-Submissions/haydal810-Milestone-Project-4
* The Boutique Ado Project from Code Institute module 12


I got inspiration from:
* My favorite kawaii website: www.blippo.com
* The photos used in this site were obtained from ...
* I received inspiration for this project from X
* User story example: https://ascendle.com/ideas/writing-user-stories-its-not-as-difficult-as-you-think/
* https://maskclub.com/
* Inspired bij the checkout page from spoonflower.com
* Canva.com backgrounds web application
* Merging git branches, this video helped me : https://www.youtube.com/watch?v=S2TUommS3O0
* Unicorn kawaii image topnav : https://www.freepik.com/free-vector/hand-drawn-kawaii-characters-collection_4098552.htm#page=9&query=kawaii&position=49
* https://fonts.google.com/specimen/Pacifico?preview.text_type=custom#standard-styles

I want to thank my mentor Brian M for guiding me through the process of creating my web application

[DEMO]: <https://bkawaiicreations.herokuapp.com/>
[a]: <https://github.com/Sweetzia/BKawaii-Creations/blob/aed187f71c9b048d8ff4a2e83cebc0810897a2a7/static/wireframes/4th%20Milestone%20Project%20BKawaii%20Creations.pdf>
