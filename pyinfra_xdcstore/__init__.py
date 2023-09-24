import importlib.resources
import os
from io import StringIO

from pyinfra.operations import files, systemd, server, git


def deploy_xdcstore(unix_user: str,
                    bot_email: str,
                    bot_passwd: str,
                    codeberg_user="",
                    codeberg_token="",
                    github_user="",
                    github_token=""):
    """Deploy xdcstore and xdcget to a UNIX user.

    :param unix_user: the UNIX user of the bot
    :param bot_email: the email address for the bot account
    :param bot_passwd: the password for the bot account
    :param codeberg_user: the username of a codeberg account
    :param codeberg_token: an API token for the codeberg account
    :param github_user: the username of a github account
    :param github_token: an API token for the github account
    """

    clone_xdcget = git.repo(
        name=f"Pull the xdcget repository",
        src=f"https://codeberg.org/webxdc/xdcget",
        dest=f"/home/{unix_user}/xdcget",
        _su_user=unix_user,
        _use_su_login=True,
    )

    if clone_xdcget.changed:
        server.shell(
            name="Compile xdcget",
            commands=[f"cd /home/{unix_user}/xdcget && pip install --user -e ."],
            _su_user=unix_user,
            _use_su_login=True,
        )

    secrets = [
        f"addr={bot_email}",
        f"mail_pw={bot_passwd}",
        "RUST_LOG=xdcstore=debug",
        f"XDCGET_CODEBERG_USER={codeberg_user}",
        f"XDCGET_CODEBERG_TOKEN={codeberg_token}",
        f"XDCGET_GITHUB_USER={github_user}",
        f"XDCGET_GITHUB_TOKEN={github_token}",
    ]
    env = "\n".join(secrets)
    files.put(
        name=f"upload secrets",
        src=StringIO(env),
        dest=f"/home/{unix_user}/.env",
        mode="0600",
        user=unix_user,
    )

    files.directory(
        name="chown database directory",
        path=f"/home/{unix_user}/.config",
        mode="0700",
        recursive=True,
        user=unix_user,
    )

    files.link(
        name="link xdcget.ini to ~",
        path=f"/home/{unix_user}/xdcget.ini",
        target=f"/home/{unix_user}/xdcget/xdcget.ini",
        user=unix_user,
    )

    files.put(
        name=f"upload xstore-update.sh",
        src=importlib.resources.files(__package__).joinpath("xstore-update.sh").open("rb"),
        dest=f"/home/{unix_user}/.config/systemd/user/",
        user=unix_user,
        mode="0700",
    )
    files.template(
        name=f"upload xstore-update systemd unit",
        src=importlib.resources.files(__package__).joinpath("xstore-update.service").open("rb"),
        dest=f"/home/{unix_user}/.config/systemd/user/",
        user=unix_user,
        unix_user=unix_user,
        bot_email=bot_email,
    )
    systemd.service(
        name=f"reload and restart xstore-update systemd service",
        service="xstore-update.service",
        user_name=unix_user,
        user_mode=True,
        daemon_reload=True,
        enabled=True,
        restarted=True,
        running=True,
        _su_user=unix_user,
        _use_su_login=True,
    )

    files.template(
        name=f"upload xstore systemd unit",
        src=importlib.resources.files(__package__).joinpath("xstore.service").open("rb"),
        dest=f"/home/{unix_user}/.config/systemd/user/",
        user=unix_user,
        unix_user=unix_user,
        bot_email=bot_email,
    )
    systemd.service(
        name=f"reload and restart {unix_user} systemd service",
        service="xstore.service",
        user_name=unix_user,
        user_mode=True,
        daemon_reload=True,
        enabled=True,
        restarted=True,
        running=True,
        _su_user=unix_user,
        _use_su_login=True,
    )


if __name__ == "__main__":
    unix_user = os.getenv("XDCGET_UNIX_USER")
    bot_email = os.getenv("XDCSTORE_EMAIL")
    bot_password = os.getenv("XDCSTORE_PASSWORD")
    codeberg_user = os.getenv("XDCGET_CODEBERG_USER")
    codeberg_token = os.getenv("XDCGET_CODEBERG_TOKEN")
    github_user = os.getenv("XDCGET_GITHUB_USER")
    github_token = os.getenv("XDCGET_GITHUB_TOKEN")

    deploy_xdcstore(
        unix_user,
        bot_email,
        bot_password,
        codeberg_user=codeberg_user,
        codeberg_token=codeberg_token,
        github_user=github_user,
        github_token=github_token,
    )
