# pyinfra module to deploy xdcstore and xdcget

This module deploys
[xdcstore](https://codeberg.com/webxdc/xdcstore)
and [xdcget](https://codeberg.com/webxdc/xdcget).


## Prerequisites

To deploy xdcstore and xdcget,
you need:

- SSH access to a linux server
- an email account for the bot
- a github.com and/or codeberg.org account so the bot can download .xdc files from there;
  read more about how to create [a github API token]()
  or [a codeberg API token]()
  in the documentation.


## Use it in python code

It can be used from the Python code like this:
```python
from pyinfra_xdcstore import deploy_xdcstore

deploy_xdcstore(
    unix_user="xdcstore",              # the existing UNIX user of the bot
    bot_email="xdcstore@example.org",  # the email address for the bot
    bot_password="p4ssw0rd",           # the password for the bot's email account
    codeberg_user="missytake",         # the username of a codeberg account
    codeberg_token="0987wer09832ru9",  # an API token for the codeberg account
    github_user="missytake",           # the username of a github account
    github_user="983q79mrrrrr9ewum",   # an API token for the github account
)
```

## Deploy with a one-liner

It can also be used to deploy xdcstore and xdcget with an ad-hoc command like this:
```
pip install --user .
XDCSTORE_EMAIL=xdcstore@example.org XDCSTORE_PASSWORD=p4ssw0rd pyinfra --ssh-user root -- example.org pyinfra_xdcstore.deploy_xdcstore
```

Additional environment variables you can use:

```
XDCGET_CODEBERG_USER    # the username of a codeberg account
XDCGET_CODEBERG_TOKEN   # an API token for the codeberg account
XDCGET_GITHUB_USER      # the username of a github account
XDCGET_GITHUB_TOKEN     # an API token for the github account
```
