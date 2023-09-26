import os

import pyinfra

from pyinfra_xdcstore import deploy_xdcstore

unix_user = os.getenv("XDCGET_UNIX_USER", "xdcstore")
bot_email = os.getenv("XDCSTORE_EMAIL")
bot_password = os.getenv("XDCSTORE_PASSWORD")
codeberg_user = os.getenv("XDCGET_CODEBERG_USER", "")
codeberg_token = os.getenv("XDCGET_CODEBERG_TOKEN", "")
github_user = os.getenv("XDCGET_GITHUB_USER", "")
github_token = os.getenv("XDCGET_GITHUB_TOKEN", "")

if bot_email is None:
    pyinfra.logger.error("XDCSTORE_EMAIL can't be empty.")
if bot_password is None:
    pyinfra.logger.error("XDCSTORE_PASSWORD can't be empty.")

deploy_xdcstore(
    unix_user,
    bot_email,
    bot_password,
    codeberg_user=codeberg_user,
    codeberg_token=codeberg_token,
    github_user=github_user,
    github_token=github_token,
)
