LAB - Class 41
05/04/2023
Project: Deployment
Author: Tyler Huntley

[Deployed FE URL](https://cookie-stand-admin2-jet.vercel.app/)
[Deployed BE URL](http://localhost:8000/api/v1/cookie_stands/)

# Feature Tasks and Requirements:
## Overview
It’s time to go live with your Cookie Stand front and back ends!

There are a lot of great (and cheap) deployment options. One of the easiest to use is Vercel.

In fact, we can use it for both our client and server applications.

Feature Tasks and Requirements
API
Create a new Vercel project by importing your cookie-stand-api project from GitHub.
Note: The project name cookie-stand-api will likely be taken so choose something sensible like cookie-stand-api-awesome-dev.
Set the Environment Variables.
TIP: paste the contents of your .env file.
Don’t forget to include vercel.json and update wsgi.py. See the demo for examples.
Manually test Django Admin panel.
Manually test api routes.
Front End
Create a new Vercel project by importing your cookie-stand-admin project from GitHub.
Note: The project name cookie-stand-admin will likely be taken so choose something sensible like cookie-stand-admin-awesome-dev.
Set the Environment Variables.
TIP: paste the contents of your .env.local file.
TIP: check that locally running front end works with deployed API prior to deploying front end.
Implementation Notes
You’ll need a Vercel account and to authorize it with Github.
The Deployment instructions above will walk you through it.
Stretch Goals
Deploy a preview build (include URL in README)
Use a competing host (e.g. AWS, Digital Ocean, Netlify, etc.)
User Acceptance Tests
No automated testing today.


## Tests:

Visual testing only  
  
-------------------------------------------------------------------------------------------  
  
LAB - Class 33
05/04/2023
Project: Putting it All Together
Author: Tyler Huntley
Links and Resources:  
[Class Github Repo](https://github.com/codefellows/seattle-code-python-401d21)

# Feature Tasks and Requirements:
## Overview
- It’s time to show off your skills by bringing “Vanilla” Django and Django Rest Framework together in the same project.
- You’ll build out a Restful API as well as a user facing site.
- Along the way you’ll see how easy Django makes it to move to a remote database.
- The project will be an old favorite with a Python twist - a Cookie Stand management site.

## Feature Tasks and Requirements
- You’ve got two choices for this lab:
- Choice 1: Use your own Template/s
  - If you’ve built a template repository for your Django sites, or APIs, or both - now’s the time to put them to work.
  - See what it would take to combine the two approaches into one starter kit to rule them all.
- Choice 2: Use API Quick Start Template
  - The API Quick Start is a built out skeleton project with lots of the tools we’ve been using in class. Check it out. If you like it, use it. But better yet, use it as an inspiration to build your own that’s a perfect fit.

- WARNING: There is no guarantee that the API Quick Start is a perfect fit for your needs, is bug free, etc. It’s a great jumping off point though. And if you spot any bugs or have ideas for improvements make a PR!

  - Modify your application paying close attention to the instructions in README.md found in root of repository.
    - Install from requirements.txt.
    - Export (aka freeze) requirements.
    - Change things app folder to be cookie_stands
    - Go through code base looking for Thing,thing and things change to cookie-stand related names.
    - E.g. Thing model becomes CookieStand
    - E.g. ThingList becomes CookieStandList
  - Pro Tip: Do a global text search looking for thing
    - Search should be case insensitive.
    - WARNING: Do NOT just cut and paste. Think through each change carefully.
  - Create/rename .env using .env.sample as starting point.
    - Here’s a handy way to generate a secret key
    - python -c “import secrets; print(secrets.token_urlsafe())”

## CookieStand Model Details
- The CookieStand model must contain

```
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location
```

    - Notice the use of JSONField.
    - Once changes are complete make migrations, migrate, and test locally.
- Database Deployment Requirements
  - Host your Database at ElephantSQL
- Site Deployment Requirements
  - We’ll handle deployment a little later. For now run your site locally, but the Database should be remote.
- Stretch Goals
  - Add functionality so that when a JSON array of hourly_sales is not provided at creation time it will be generated with random numbers based on minimum/maximum customers per hour and average cookies per sale.
- Implementation Notes
  - Name your repo cookie-stand-api
  - Site must use environment variables.
- Useful Terminal Commands
  - docker compose up --build
  - docker compose down
  - docker compose restart
  - docker compose run web python manage.py migrate
  - docker compose run web python manage.py collectstatic
- User Acceptance Tests
  - Add Unit Tests to cookie_stands/tests.py
  - Manually confirm API using API Tester, Postman or HTTPie.
- Submission Requirements
  - Make sure a user exists in Database
  - E.g. createsuperuser has been run
  - Provide username and password in Canvas submission
  - Rename .env contents or provide in Canvas submission
  - Include GitHub repo in Canvas submission

## Tests:

Manual testing with HTTPie: See below for instructions
- I ran httpie tests, no issues encountered.

## Start Docker:
docker compose up

## Shut down Docker:
docker compose down

## WINDOWS:
- Docker on Windows use browser url: "localhost:8000/api/v1/board_games/"

Tests:
- Using SQLite3 - `docker compose run web python manage.py test` to run tests. 
Modified the given tests to fit my app.

## SETUP and MANUAL TESTING USING httpie:

- Set up your virtual environment
- `python3 -m venv .venv`

- Enter your virtual environment
- `source ./.venv/bin/activate`

- Install requirements
- `pip install -r requirements.txt`

- Start Docker
- `docker compose up`

- To check authentication status
- `http get localhost:8000/api/v1/cookie_stands/`

- To get token
- `http post localhost:8000/api/token/ username=admin password=1234`

- Copy access token without the quotes and run (don't forget about the closing single quote)
- `http :8000/api/v1/cookie_stands/ 'Authorization: Bearer pasteAccessTokenOverThisString'`

- CRUD endpoint route:
- `api/v1/cookie_stands/`
