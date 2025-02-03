# Surf Sesh

<img src=static/images/amiresponsive.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

The deployed site can be found [here](https://booking-system-ci-0291f03de219.herokuapp.com/).

# Index

- [Purpose](#purpose)
- [Planning](#planning)
- [User Stories](#user-stories)
- [Project Board](#project_board)
- [ERD](#flowchart_&_erd)
- [Design Decisions & UX](#design_decisions_&_ux)
- [Features](#features)
- [Testing and Validation](#testing-and-validation)
- [AI](#ai)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)

## Purpose

This project is a web appplication for a fictional surf destination with online booking functionality.

## Planning

<img src=static/images/kanban.png alt="Screenshot of project Kanban board" width="600">

<br>

The project was entirely planned using a kanban board on github.

## User Stories

All user stories can be found on the [Project Board](https://github.com/users/E-Printer/projects/4/views/1) including the relevant tasks, MOSCOW prioritisation for them and current status.

<br>

The completed sprint was composed of many separate items. Having used the MoSCoW approach to prioritisation. "Won't-Have" items will remain in the backlog for now.

Partially applied some of the acceptance criteria of some of the Should Have Critieria such as including contact information with the rest of acceptance criteria in the backlog such as adding maps and contact forms. This did add tech debt as the delete functionality is still not operating correctly.

Full [Project Board](https://github.com/users/E-Printer/projects/1/views/1)

## ERD

<img src=static/images/erd.png image alt="ERD" width="600" height="">

<br>

An ERD to help visualise the models used and relationships between entities.

<br>

## Design Decisions & UX

A couple wireframes were produced using Figma templates to help plan the project.

As the project took shape the designs evolved.

### Desktop

<img src=static/images/wireframe1.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/wireframe2.png image alt="desktop wireframe for booking page" width="600">



### Typography

Using [Google Fonts](www.googlefonts.com), chose Roboto for the main body text, Lato for H1 headings and Noticia Text for the Brand.

<img src=static/images/fonts.png image alt="screenshot of Google fonts selected for project" width="600">

<br>

### Colours and Images

<img src=static/images/colourpalette.png image alt="screenshot of colours selected for project" width="600">

<br>

### Images & Icons

Sourced images from Google images of The Wave, Bristol [TheWave](https://www.thewave.com/)

### Accessibility

The site is fully responsive on different devices. 

<img src=static/images/amiresponsive.png alt="A screenshot showing the project on multiple devices" width="600">

## Features

<br>

**Home Page**

The Home page of the site shows a carousel of images of the location and contact points.

**Sessions**

The bookings page allows site visitors to create, edit and delete upcoming sessions and receive confirmation that this has been done.

When a user is logged in, they can see My Bookings to view all their bookings and amend them.

**Services**

A services section with tables, details and pricing options for the different sessions available.

**The Footer**

The Footer has links to the various relevant professional and social media pages for the site owner.

**Register**

The site has a facility to sign up as a user in order this enables them to create, edit or delete their sessions.

**Sign In**

The site has a facility to sign in, once a user creates an account, this enables them to create, edit or delete their sessions.

**Sign Out**

The site has a facility for a user to sign out of their account.

**Admin**

The site has a facility for designated administrators to sign in, in order to administrate the site via the standard Django admin interface.

## Testing and Validation

### Automated Testing

### Lighthouse Desktop

<img src=static/images/desktop.png alt="A screenshot showing the results of Lighthouse testing" width="600">

### Lighthouse Mobile

<img src=static/images/mobile.png alt="A screenshot showing the results of Lighthouse testing" width="600">

### Validator Testing

- HTML

There are some errors that need amending.

<img src=static/images/htmlErrors.png alt="HTML validation screenshot">

<br>

<hr>

- CSS

No errors in CSS when validating it.

<img src=static/images/cssErrors.png alt="css validation screenshot">

<hr>

- Javascript

JSHint recommendations.

<img src=static/images/jsHint.png alt="JS Hint for services.js">

### Manual Testing

#### Issue: Non-logged-in users can access restricted booking functionalities

#### Expected:
The capacity to book a surf session should only be allowed to logged-in users.

#### Testing:
Manually using the website, it is possible to book surfs without being logged in.

#### Result:
Users are able to access the edit bookings page by entering the url and then make changes without being logged in.

#### Fix:
Adding login-required decorators, manually tested.

### Bugs

Currently facing issues with the delete functionality. Expert Barrels info not showing.

## AI

Utilised ChatGPT to support with fixing code and troubleshooting.

## Deployment

The site was deployed to Heroku from the main branch of the repository early in the development stage for continuous deployment and checking.

The Heroku app is setup with 3 environment variables, repalcing the environment variables stored in env.py (which doesn't get pushed to github).

In order to create an Heroku app:

1. Click on New in the Heroku dashboard, and Create new app from the menu dropdown.

2. Give your new app a unique name, and choose a region, preferably one that is geographically closest to you.

3. Click "Create app"

4. In your app settings, click on "Reveal Config Vars" and add the environment variables for your app. These are:

- DATABASE_URL - your database connection string
- SECRET_Key - the secret key for your app
- To enable email notifications:
* EMAIL_HOST_USER and EMAIL_HOST_PASSWORD will need to be provided.

The PostgreSQL database is provided by Code Institute.

Once the app setup is complete, click on the Deploy tab then follow these steps:

1. Connect to the required GitHub account
2. Select the relevant repository to deploy from
3. Click the Deploy Branch button to start the deployment.
4. Once deployment finishes the app can be launched.

The deployed site can be found [here](https://booking-system-ci-0291f03de219.herokuapp.com/).


### Future Improvements & Iterations

There is an issue with the delete functionality as well as some further features that could be implemented. As it stands, there are no constrictions on bookings.
