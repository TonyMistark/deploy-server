#!/bin/bash

set -eux
password=""
cd /home/ice/projects/hexo-ablog/ablog/
git pull git@github.com:TonyMistark/hexo-ablog.git && echo $password | sudo -S supervisorctl restart hexoserver
#git pull git@github.com:TonyMistark/hexo-ablog.gi && supervisorctl restart hexoserver