#!/bin/bash

kill -9 $(pgrep hexo)
cd /home/ice/projects/hexo-ablog/ablog/
git pull git@github.com:TonyMistark/hexo-ablog.git
hexo server -i 0.0.0.0 -p 8989 &