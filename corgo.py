import praw
import sendgrid
import os

from sendgrid.helpers.mail import Email, Content, Mail
from datetime import datetime

reddit_client_id = os.environ.get('REDDIT_CLIENT_ID')
reddit_client_secret = os.environ.get('REDDIT_CLIENT_SECRET')

sg = sendgrid.SendGridAPIClient(
    apikey=os.environ.get('SENDGRID_API_KEY'),
)
recipient = os.environ.get('SENDGRID_RECIPIENT')

urls = ['i.redditmedia.com', 'imgur.com']


def matching_url(url):
    for valid_url in urls:
        if valid_url in url:
            return True
    return False


def format_content(title, url):
    return('<html><body><div>"{}"</div><div>'
           '<img src={}></img></div></body></html>'.format(title, url))


def send_email(title, url):
    from_email = Email("noreply@dailycorgo.com")
    to_email = Email(recipient)

    date = datetime.now().strftime("%B %d %G")
    subject = "[Daily Corgo] {}".format(date)
    content = Content("text/html", format_content(title, url))

    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)


def main():
    reddit = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent='daily-corgo',
    )

    for post in reddit.subreddit('corgi').top(limit=10, time_filter='day'):
        if 'images' in post.preview:
            for image in post.preview['images']:
                url = image['source']['url']
                if matching_url(url):
                    send_email(post.title, url)
                    return


if __name__ == "__main__":
    main()
