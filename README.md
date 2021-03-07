
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

![mock-up](/media/Mock-up.jpg)

**UX**

**User stories**

* As a user : As a new visitor to BKawaii Creations, I want the page to be easily navigated.
* As a user:  I want clear instructions on how to view all the products and categories. 
* As a user: I want the web application to respond quickly to my interaction.
* As a user: I want a search option so I can quickly find the product I'd like.
* As a user: I want to be able to purchase these products easily, and pay for them online.
* As a user: I want the payment service to be easy and clear.
* As a user: I want to register and login on the web application.
* As a user/shop owner: I want to add and delete products in the online shop

**Visitor Goals**

The target audience to the web store would be:
* Fans of Kawaii Facemasks
* Fans of Kawaii Nail Art press-on nails
* Fans of Kawaii Nail Art palettes
* Fans of Kawaii Goodies

**Surface**
* For the surface plane I wanted the design to be pastel coloured and fun. 
* The colors of my website are : 

  ![colors](/media/colors-hart.jpg)

* The images used for my products are photographed by myself.
* I choose the [Quicksand][1] and [Pacifico][2] google font for my text on the website.
* The buttons are purple coloured and simple. Each button has a text description of it, describing to the user what it's function is.
* Bkawaii creations logo was designed by myself on [canva][12]. It portraits me with a kawaii food facemask.
I used the comic filter over my logo, so it looks fun on my website.

**Skeleton**

I created the wireframes using the program “Balsamiq”. 

Click [here][a] for my BKawaii Creations wireframes.


**Layout and existing features**
This is a multi-page layout. 
There are different templates used:
1. Base template with login, registration, products, search engine and shoppingbag navbar. 
2. Index template for the homepage content: about section, popular products section and footer.
3. Products template to view the products and product details
4. Bag template used for the shopping bag page
5. Checkout template used for the checkout and secure purchase. 
6. Profiles template for login, registration and product admininstration

**Features Left to Implement**
* A wishlist, where the user can pick products and "favorite" them, before deciding to add them to the cart or not. 
* For the shop owner to edit their products in the product admininstration. For now there is only the option to add and delete products.
* A video (tutorial) on my homepage where I show customers how I make and wear my facemasks
* A customer review section on my homepage

**Challenges**
* I worked with Git branches for the first time in this project. 
It was difficult at first and I got scared merging my git branches to my master branch. 
I was afraid my code would not work anymore. But with the help of this video tutorial from [Atlassian][3] everything went well with merging my git branches, until I encountered a problem when I went merging my profiles branch to my master. Is was a merge conflict with my binary file db.sqlite3. 
I could not resolve the conflict in github with a pull request.
So I searched for a solution on google and finally discoverd this tip on [Lostechies.com][4].
I had no git merge conflicts anymore and my profiles app was added to my master branch. 
The only thing was, that I had to create a new superuser to gain access to my django administration.

* I struggled with my media queries in my base.css. 
Especially getting my jumbotron right on every mobile device and get everything responsive on a desktop at the same time.
This is something I still want to improve in.

* Deploying my project on Heroku with all the static files and media, was a challenge. I eventually asked tutor support for help.
Eventually we discovered I did not have DEVELOPMENT = 1 in my environmental variables setting in Gitpod. The images were shown in Gitpod, but not yet in my Heroku app. Looking at the [House of Mouse][5] project from Anna Greaves and how she used the Object URL from AWS S3 helped me solve this problem. I just had to add the media AWS Object URL link to the image src in my index.html.

**Main Technologies Used**

Languages used

* This project uses HTML, CSS, JavaScript and Python/Django programming languages.

Tools used

* Balsamiq to create the wireframes for this project.
* Django as python web framework 
* Git to handle version control.
* GitHub to store the project code remotely.
* PIP for installation of tools needed in this project
* Stripe as payment platform to validate and accept credit card payments securely.
* Amazon S3 - AWS Cloud Storage for static and media files
* Heroku for deployment
* Django Crispy Forms to style django forms.

Libraries utilised

* Google Fonts to style the website fonts.
* FontAwesome to provide icons for the online store.
* Bootstrap 4 to simplify the structure of the website and make the website responsive easily.
* jQuery

**Databases**

Databases used:

During development on my local machine I worked with the standard sqlite3 database installed with Django. 
On deployment, the SQL database provided by Heroku is a PostgreSQL database.

**Testing**

Manual User testing:

This was the primary method of testing the application. 

Click [here][6] for my Test Write Up.

I tested the app manually myself and asked relatives to go to my website and give his feedback.
I used [Screenfly][7] to look at my website in different resolutions.

**Responsive design**

Bkawaii Creations was tested on the Chrome browser and on multiple mobile devices (iPhone 5, 6, 7, 8, iPad, Ipad-pro, Iphone X, Moto G4, Galaxy S5, Pixel 2, Pixel2XL, Surface Duo and Galaxy Fold) to ensure compatibility and responsiveness.

**Deployment**

**The project is stored in a GitHub repository and hosted on Heroku.**

I followed the next steps to deploy Bkawaii Creations on the [GitHub][8] pages:
* Log into GitHub.
* Select Sweetzia/bkawaii_creations in the repository list.
* Go to Settings
* Scroll down to the GitHub Pages section.
* Select the Master Branch
* On selecting Master Branch the page is automatically refreshed.
* The link can be retrieved to the deployed website.

I followed the next steps to host Bkawaii Creations on [Heroku][9]:
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
* Putting all the correct Config Vars in Heroku and remove DISABLE_COLLECTSTATIC=1
* Click on the "View app" button.
* Open app in Heroku, succesfully deployed app!

**Credits**

**Content**

The text content on the website was written by me.

**Media**

* All my own handmade product images were photographed by myself.

**Acknowledgements**

I got inspiration from:

* The Boutique Ado Project from Code Institute module 12. 
I used the tutorials from this project to build my web application. 
* The final milestone project from [haydal810][10]
* The House of Mouse milestone project from [Anna Greaves][5]
* My favorite kawaii website: [www.blippo.com][11]

***I want to thank my mentor Brian M for guiding me through the process of creating my web application***

[DEMO]: <https://bkawaiicreations.herokuapp.com/>
[a]: <https://github.com/Sweetzia/BKawaii-Creations/blob/aed187f71c9b048d8ff4a2e83cebc0810897a2a7/static/wireframes/4th%20Milestone%20Project%20BKawaii%20Creations.pdf>
[1]: <https://fonts.google.com/specimen/Quicksand?preview.text_type=custom>
[2]: <https://fonts.google.com/specimen/Pacifico?preview.text_type=custom>
[3]: <https://www.youtube.com/watch?v=S2TUommS3O0>
[4]: <https://lostechies.com/joshuaflanagan/2010/01/29/how-to-resolve-a-binary-file-conflict-with-git/>
[5]: <https://github.com/AJGreaves/thehouseofmouse>
[6]: <https://github.com/Sweetzia/bkawaii_creations/blob/582784cc378d976cdcaeade39c460f1e188a0151/static/Test%20write-up/Test%20readme%20bkawaii%20creations%20%281%29.pdf>
[7]: <https://bluetree.ai/screenfly/>
[8]: <https://sweetzia.github.io/bkawaii_creations/>
[9]: <https://bkawaiicreations.herokuapp.com/>
[10]: <https://github.com/Code-Institute-Submissions/haydal810-Milestone-Project-4>
[11]: <https://blippo.com>
[12]: <https://canva.com>
