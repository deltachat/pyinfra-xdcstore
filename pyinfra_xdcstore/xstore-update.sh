#!/bin/sh

trap "systemctl --user start xstore.service" EXIT

set -e

cd xdcget
git pull --autostash --rebase origin main
pip install --user .

$HOME/.local/bin/xdcget update

cd ..
wget https://download.delta.chat/store/preview/xdcstore-main.tar.gz
systemctl --user stop xstore.service
tar --overwrite -xvf xdcstore-main.tar.gz
rm xdcstore-main.tar.gz
$HOME/xdcstore/xdcstore import $HOME/xdcget/export
