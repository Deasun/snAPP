[![Build Status](https://travis-ci.org/Deasun/snAPP.svg?branch=master)](https://travis-ci.org/Deasun/snAPP)

# snAPP
An on-line platform designed for trade union activists, by trade union activists.

## Overview
 
### What is this application for?
snAPP makes it easy for new and experienced trade unionists to get the support they need and give the support they can. 
 
### What does it do?
At the core of snAPP is the **Alert System**. An alert can be a call for support, a request for information or posting of a relevant news item/campaign update which members announce to the snAPP network. Alerts can be anything members need help with. Members find out more information on alerts by visiting the profile page of the members who announced the alert and/or by contacting them directly.

But this is only the starting point. 

> snAPP is an evolving application whose features and functionalities are determined by members of the snAPP network themselves.

By using the **BugTicket** system, members identify problems within the application and help to improve the convenience and efficiency of snAPP. 

The **FeatureTicket** system is the mechanism for members to request, discuss and raise financial contributions to increase the features on snAPP (for example including twitter timelines, creating a file sharing system or chat facility).

> snAPP does not seek to replicate or replace existing social media platforms, but rather to be a designated space for initiating daily, practical support among grassroots union activists.

 
### How does it work
 
This website uses the **Django** microframework to route viewers through the site and execute the programme which is written in **python 3.4**. 

The site is styled with **Bootstrap** and **JQuery** code for enhancing user-experience and hiding descriptive text (used to guide the member through the site and provide detailed information) in modals, tooltips and tabs. Random member alerts are scrolled across the screen using the JQuery plug-in **Marquee**. 

User data is inputted using **django-bootstrap-forms** and stored in a **PostgreSQL** object-relational database (using **Heroku-Postgres**). The database and the entire application is hosted on the **Heroku** platform. 

Data-visualisation charts are created using the **pygal** python svg plotting library. Static and media files are stored in an **AWS S3** bucket. Payments are processed using the **Stripe** online payment processing system. 

**Bower** has been used to manage package dependencies for deployment of site on github pages. The site is designed using a **mobile-first** design and can be viewed [HERE](https://futoisaru.github.io/hippo/). 

The snAPP **API**, providing data relating to the application's development is available [HERE]() User information and alerts are not provided to the public. A **twitter** widget displaying the feed of the news source LabourStart is rendered on medium and large viewports across the site.

## Features
Find below the applications and the features provided in each. 
### Existing Features
#### Accounts
* registration to create users (members) and login credentials password reset process
* each member has a profile page containing some personal (and editable) information, details of their involvement in snAPP's development (what bugs they have reported or features they have requested) and their snAPP alert
* a summary table of the most recent alerts across the snAPP network. Random alerts are also displayed constantly in browser view and accessible through a click. Member alerts cease to appear on the alert system when they expire. Members can amend their alerts at any time


#### BugTickets
* members report bugs by completing a Bug Report Form. Members must classify their bugs to assist the snAPP admin pinpoint and classify reported problems. 
* each bug has its own page where other member can view details of the bug, add a comment or upvote it (if they experience it as well). Only snAPP admin have the ability to amend or delete bug reports.
snAPP admin particpate in the comments section to report on progress. A Progress Report is published upon completion
* for purposes of transparency, the Fixing snAPP page displays data-visualisation charts outlining the type of bugs being reported, as well as the daily, weekly, fortnightly and monthly activity of the snAPP admin team. A table outlining the most upvoted bugs is also displayed

#### FeatureTickets
* members request a feature by completing a Feature Request Form in which they describe and classify their request.
* each Feature has its own profile page where members can access full details about the feature, add comments to suggest refining/amending the request. snAPP admin enageg in the discussion to refine the request. Once this process is complete, snAPP admin team develop a Feature Report and costing of how much money will be required to create the entire feature. This costing is the feature's target
* members contribute to the feature by purchasing FeatureTickets (£10 x 1). The snAPP admin team will begin work once the feature starts to get contributions. A progress bar is displayed to show how many more FeatureTickets are required to complete the feature
* the Developing snAPP page uses data-visualisation charts to show the activity of the snAPP team in responding to members' requests. The most recently added feature, one feature in development, and one without any contributions - as well as a table of features list by date - are displayed for the purposes of transparency and promoting certain features. 

#### Cart
The cart keeps track of a member's FeatureTicket purchases during each session. 
Members can access their carts to review the number of tickets purchased and proceed to checkout.

#### Checkout
Members can review their order on the checkout page and are asked to input their personal and payment details using the Stripe online payment processing system.

#### Search
There are search facilities available for members, alerts, bugtickets and featuretickets. Members are encouraged to use the search facility to prevent duplicating feature requests and bug reports.


### Features Left to Implement
- email alerts to members when there is activity (upvotes, comments, contributions) relating to their bugs or features.
- alert classification to let members register areas of interest and match these to alerts
- blog application for members
- ajax requests used to render alerts
- member choose which twitter feed they want on their page (their union's, a campaign's, etc)
- activating the FeatureTicket Upvote (non-payment) system which will help to assess popularity among members and assist snAPP admin to promote features to certain unions

## Tech Used

### Specific technology used on the application includes:

### Code 
- **HTML**, **CSS**, **JQuery** and **Python**
  - Base languages used to create website
- [Django](https://www.djangoproject.com/)
    - **Django** is used to develop models, templates and views used in the site amd handle routing
- [Bootstrap](http://getbootstrap.com/)
    - **Bootstrap 3.3.7** is used to render a responsive layout and hide text-heavy areas in modals and tabs to enable quicker, selective browsing
- [JQuery](https://jquery.com)
    - **JQuery** adds animation styling to our site to enhance user experience. The JQuery plug-in **Marquee** was used to display the scrolling alerts

### Functionality
- [Stripe](https://stripe.com)
    - The online payment processing system **Stripe** is used to handle member contributions.
- [AWS S3](https://aws.amazon.com/s3/)
    - **AWS S3** cloud storage is used to store the static and media files for the application.

### Hosting
- [Heroku-Postres](https://www.heroku.com/postgres)
    - During development mode, models were migrated to the default SQLite databse provided by Django. In production mode, data is stored in a postgreSQL database using **Heroku-Postres**.
- [Heroku](https://www.heroku.com/)
    - The Cloud Application Platform **Heroku** hosts the snAPP application.

<!--npm and bower check-->
- [npm](https://www.npmjs.com/)
    - We use **npm** to install **http-server** in order to view the site
- [Bower](https://bower.io)
    - Using **Bower** to manage package dependencies


### Testing
- [coverage.py](https://coverage.readthedocs.io/en/coverage-4.5.1/)
    - Python code across applications is tested extensively using the **coverage.py** testing tool 
- [Travis CI](https://bower.io)
    - pre-deployment tests are carried out using the **Travis Continuous Integration** service
- JQuery styling code was tested manually across the site
- The site was viewed and tested across mobile, tablet, laptop and large desktop views and in the following browsers:
  - Google Chrome
  - Opera
  - Microsoft Edge
  - Mozilla Firefox

## Contributing
 
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've that you'll need to make sure that you have **npm** installed
  1. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server -c-1```
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits

### Media
- Background image to the site was sourced from [FREEIMAGES](https://www.freeimages.com)

### Information
- The categories for bugs were adapted from [Software Testing Help's](https://www.softwaretestinghelp.com/types-of-software-errors/) guide
- The categories for features were adapted from this [Mobidev's](https://mobidev.biz/blog/11_key_features_of_a_successful_mobile_app) article
- The twitter feed is from [Labourstart](https://www.labourstart.org)