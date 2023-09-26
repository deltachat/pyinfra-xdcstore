# pyinfra module to deploy xdcstore and xdcget

This module deploys
[xdcstore](https://codeberg.com/webxdc/xdcstore)
and [xdcget](https://codeberg.com/webxdc/xdcget).


## Prerequisites

To deploy xdcstore and xdcget,
you need:

- root SSH access to a linux server (tested with Debian 12)
- an email account for the bot
- a github.com and/or codeberg.org account so the bot can download .xdc files from there;
  read more about how to create the neccessary API tokens
  [in the documentation](https://codeberg.org/webxdc/xdcget#getting-a-codeberg-api-access-token).


## Use it in python code

This module can be used
in a [pyinfra deploy.py](https://docs.pyinfra.com/en/2.x/getting-started.html#create-a-deploy) file
like this:

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

## Deploy with few CLI commands

You can also use this module
to deploy xdcstore and xdcget
with these few CLI commands:

```
# install pyinfra, and this module
git clone https://github.com/deltachat/pyinfra-xdcstore
pip install --user .

# configure the bot's credentials
export XDCSTORE_EMAIL=xdcstore@example.org
export XDCSTORE_PASSWORD=p4ssw0rd

# run the deployment
pyinfra --ssh-user root -- <your_server> deploy.py
```

Additional environment variables you can (and should) use:

```
XDCGET_UNIX_USER        # as which user on your server you want the bot to run; default: xdcstore
XDCGET_CODEBERG_USER    # the username of a codeberg account
XDCGET_CODEBERG_TOKEN   # an API token for the codeberg account
XDCGET_GITHUB_USER      # the username of a github account
XDCGET_GITHUB_TOKEN     # an API token for the github account
```

**Note:** if you get the following error,
you just need to re-run the pyinfra command and it works.

```
    Failed to upload file, retrying: Failure
    Failed to upload file, retrying: Failure
    Failed to upload file, retrying: Failure
    [bomba.testrun.org] Command socket/SSH error: OSError('Failure',)
    [bomba.testrun.org] Error: executed 2/5 commands
--> pyinfra error: No hosts remaining!
``` 

