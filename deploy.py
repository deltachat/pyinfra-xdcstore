"""
This is an example pyinfra deploy file for installing xdcstore and xdcget.
Its usage is documented in https://github.com/deltachat/pyinfra-xdcstore/#deploy-with-few-cli-commands
"""

import os
import importlib

import pyinfra
from pyinfra.facts.server import Users
from pyinfra.operations import server, files

from pyinfra_xdcstore import deploy_xdcstore


def create_unix_user(unix_user):
    """Create a UNIX user for the bot.

    :param unix_user: the username for the UNIX user
    """
    server.user(
        name=f"Add user {unix_user}",
        user=unix_user,
        present=True,
        shell="/bin/bash",
        home=f"/home/{unix_user}",
    )

    server.shell(
        name=f"enable {unix_user}'s systemd units to auto-start at boot",
        commands=[f"loginctl enable-linger {unix_user}"],
    )

    files.put(
        name=f"upload {unix_user} .profile",
        src=importlib.resources.files('pyinfra_xdcstore').joinpath("xstore.profile"),
        dest=f"/home/{unix_user}/.profile",
        user=unix_user,
        group=unix_user,
    )


def main():
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

    if unix_user not in [user for user in pyinfra.host.get_fact(Users)]:
        create_unix_user(unix_user)

    deploy_xdcstore(
        unix_user,
        bot_email,
        bot_password,
        codeberg_user=codeberg_user,
        codeberg_token=codeberg_token,
        github_user=github_user,
        github_token=github_token,
    )


main()
