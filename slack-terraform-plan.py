#!/usr/bin/env python3

import os
import shutil
from slackclient import SlackClient
from python_terraform import *

# INIT
slack_token = os.environ["SLACK_API_TOKEN"]
slack_channel = 'slackbottesting'
sc = SlackClient(slack_token)
# Get current PWD
cwd = os.getcwd()

def init_terraform(tf_state_directory):
    tf = Terraform(working_dir=tf_state_directory)
    return tf

def run_terraform_plan(tf):
    return_code, stdout, stderr = tf.plan(no_color=IsFlagged)
    return stdout

def post_message(slack_channel, message_text):
    sc.api_call(
      "chat.postMessage",
      channel=slack_channel,
      text=message_text
    )

def upload_snippet(slack_channel, snippet):
    sc.api_call(
        "files.upload",
        channels=slack_channel,
        file=snippet,
        title="Terraform Plan"
    )

if __name__ == "__main__":
    tf = init_terraform(cwd)
    print('Running Terraform Plan...')
    run_terraform_plan(tf)
    # post_message('slackbottesting', run_terraform_plan(tf))
    print(f'Uploading snippet to #{slack_channel}')
    upload_snippet(slack_channel, run_terraform_plan(tf))
