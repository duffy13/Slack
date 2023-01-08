from flask import Flask
from slackify import Slackify, async_task


app = Flask(__name__)
slackify = Slackify(app=app)


@slackify.command
def hello():
    return reply_text('Hello from Slack')


# Change the slash command name to /say_bye instead of the default function name
@slackify.command(name='say_bye')
def bye():
    my_background_job()
    return reply_text('Bye')


@async_task
def my_background_job():
    """Non blocking long task"""
    sleep(15)
