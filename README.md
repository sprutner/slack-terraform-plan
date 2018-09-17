# Tool to notify a slack channel of your terraform plans

## Use case: Submitting plans to #server automatically


### Requirements
- Python3
- Terraform

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
- Run `tf-slack`
- Plan will run and then post to desired slack_channel
