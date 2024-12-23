# Surf Sesh

<img src=static/images/readme/mockup.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

The deployed site can be found [here](https://hh-booking-project-05701fec89a2.herokuapp.com/).

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

<img src=/workspace/Booking-system2/static/images/kanban.png alt="Screenshot of project Kanban board" width="600">

<br>

The project was entirely planned using a kanban board on github.

## User Stories

All user stories can be found on the [Project Board](https://github.com/users/E-Printer/projects/4/views/1) including the relevant tasks, MOSCOW prioritisation for them and current status.

<br>

The completed sprint was composed of many separate items. Having used the MoSCoW approach to prioritisation. "Won't-Have" items will remain in the backlog for now.

Partially applied some of the acceptance criteria of some of our Should Have Critieria such as including contact information with the rest of acceptance criteria in the backlog such as adding maps and contact forms. This did add tech debt as the delete functionality is still not operating correctly.

Full [Project Board](https://github.com/users/E-Printer/projects/1/views/1)

## ERD

<img src=/workspace/Booking-system2/static/images/erd.png image alt="ERD" width="600" height="">

<br>

An ERD to help visualise the models used and relationships between entities.

<br>

## Design Decisions & UX

Many different wireframes were produced to help plan the project including for desktop, tablet and mobile devices.

We had several ideas during the wireframing process and as the project took shape our designs evolved.

### Desktop

<img src=static/images/readme/wireframes/wireframes-1.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-2.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-3.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-4.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-5.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-6.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/Desktop_Create_Booking.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/Desktop_Booking_Confirmed.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/Desktop_Booking_Deleted.png image alt="desktop wireframe for homepage" width="600">

<br>

### Tablet

<img src=static/images/readme/wireframes/Tablet_Create_Booking.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Tablet_Booking_Confirmed.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Tablet_Booking_Deleted.png image alt="tablet wireframes for all pages" height="300">

<br>

### Mobile

<img src=static/images/readme/wireframes/Mobile_Create_Booking.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Mobile_Booking_Confirmed.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Mobile_Booking_Deleted.png image alt="tablet wireframes for all pages" height="300">

<br>

### Typography

We selected our fonts from [Google Fonts](www.googlefonts.com) and choose Roboto for the main body text, Lato for H1 headings and Noticia Text for the Brand.

<img src=static/images/readme/design/hh_fonts.png image alt="screenshot of Google fonts selected for project" width="600">

<br>

### Colours and Images

<img src=static/images/readme/design/hh_colours.png image alt="screenshot of colours selected for project" width="600">

<br>

### Images & Icons

Sourced images from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/) as well as lifting images from Google images of The Wave, Bristol [TheWave](https://www.thewave.com/)

### Accessibility

The site is fully responsive on different devices. 

<img src=static/images/readme/mockup.png alt="A screenshot showing the project on multiple devices" width="600">

## Features

<br>

**Home Page**

The Home page of the site shows a carousel of images of the location and contact points.

**Sessions**

The bookings page allows site visitors to create, edit and delete upcoming appointments and receive confirmation that this has been done.

When a user is logged in, they can see My Bookings to view all their bookings and amend them.

**Services**

A services section with tables, details and pricing options for the different services on offer.

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

We carried out some automated testing.

<img src=static/images/readme/models_test_results.png alt="A screenshot showing the results of Lighthouse testing" width="600">

### Lighthouse

The site was tested using Lighthouse acheiving the following results:

<img src=static/images/readme/testing/lighthouse.png alt="A screenshot showing the results of Lighthouse testing" width="600">

### Validator Testing

- HTML

We ran the HTML through a validatoor and had a few small errors and fixed these.

<img src=static/images/readme/testing/html_1.png alt="HTML validation screenshot">

<br>

<img src=static/images/readme/testing/html_2.png alt="HTML validation screenshot">

<hr>

- CSS

We had no errors in our CSS when validating it.

<img src=static/images/readme/testing/css_validator.png alt="css validation screenshot">

<hr>

- Javascript

<img src=static/images/readme/testing/services_js.png alt="JS Hint for services.js">

<br>

<img src=static/images/readme/testing/toasts_js.png alt="JS Hint for toasts.js">

### Bugs

Currently facing issues with the delete functionality.

## AI

We utilised Claude AI and ChatGPT to support with fixing our code and troubleshooting.

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
- CLOUDINARY_URL - the cloudinary url for your image store

The PostgreSQL database is served from NeonDB provided by Code Institute.

Once the app setup is complete, click on the Deploy tab then follow these steps:

1. Connect to the required GitHub account
2. Select the relevant repository to deploy from
3. Click the Deploy Branch button to start the deployment.
4. Once deployment finishes the app can be launched.

The deployed site can be found [here](https://booking-system-ci-0291f03de219.herokuapp.com/).


### Future Improvements & Iterations

There is an issue with the delete functionality as well as some further features that could be implemented. As it stands, there are no constrictions on bookings.
