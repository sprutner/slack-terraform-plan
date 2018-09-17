# Tool to notify a slack channel of your terraform plans

## Use case: Submitting Terraform Plans as a snippet to a desired slack channel automatically


### Requirements
- Python3
- Terraform
- SLACK API Token set as a local env var. (E.G. SLACK_API_TOKEN=abcdefgh...)

### Installation
- Install required dependencies

```git clone https://github.com/sprutner/slack-terraform-plan
cd ./slack-terraform-plan
pip3 install -r requirements.txt
```
- Symlink script to your path
`ln -s $(pwd)/slack-terraform-plan/slack-terraform-plan.py ~/bin/tf-slack`

### Usage
- Change to the directory of desired terraform state
- Run `tf-slack --slack-channel CHANNELNAME`
- Plan will run and then post to desired slack_channel

Alternatively, you can also specify the $TFSLACK_CHANNEL environment variable in your local environment to set a default for your environment.
