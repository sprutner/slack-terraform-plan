#!/usr/bin/env python3

import os
import shutil
from slackclient import SlackClient
from python_terraform import *
import argparse

# INIT
slack_token = os.environ["SLACK_API_TOKEN"]

sc = SlackClient(slack_token)
# Get current PWD
cwd = os.getcwd()

def set_slack_channel(slack_channel='slackbottesting'):
    if "TFSLACK_CHANNEL" in os.environ:
        slack_channel = os.environ["TFSLACK_CHANNEL"]
    else:
        print(f"TFSLACK_CHANNEL environment variable not set, setting to #{slack_channel}")

    return slack_channel

def parse_arguments(help=False):
    #argpase init
    parser = argparse.ArgumentParser('tf-slack')
    parser.add_argument('--slack-channel')
    result, unknown = parser.parse_known_args()
    if help == True:
        return parser.print_help(sys.stderr)
    else:
        return result

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
    # Parse arguments
    args = parse_arguments()
    if args.slack_channel is not None:
        slack_channel = set_slack_channel(args.slack_channel)
    else:
        slack_channel = set_slack_channel()
    # Initialize
    tf = init_terraform(cwd)
    print('Running Terraform Plan...')
    run_terraform_plan(tf)
    # post_message('slackbottesting', run_terraform_plan(tf))
    print(f'Uploading snippet to #{slack_channel}')
    upload_snippet(slack_channel, run_terraform_plan(tf))
