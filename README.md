# Daily Corgo
Get the top image from the last day from [/r/corgi](https://www.reddit.com/r/corgi/top/?sort=top&t=day) sent to your email.

## Instructions
1. Supply the API keys needed to the environment
  - REDDIT_CLIENT_ID: Create an app on the reddit developer site
  - REDDIT_CLIENT_SECRET: Comes with the ID
  - SENDGRID_API_KEY: Make a sendgrid account
  - SENDGRID_RECIPIENT: Set to the email you want to send to
2. `pipenv install`
3. `pipenv shell`
4. `python3 corgo.py`

## Hosting
You'll have to host the script and schedule it to execute (I have it set to execute daily).  
I am currently using Heroku - it's free (per my usage), has an easy scheduler add-on, and lets me easily set the environment variables needed.

## Author
Sameer Chitley
