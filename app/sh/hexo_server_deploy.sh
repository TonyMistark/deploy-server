#!/bin/bash

echo "kill hexo"
kill -9 $(pgrep hexo)
echo "cd /home/ice/projects/hexo-ablog/ablog/"
cd /home/ice/projects/hexo-ablog/ablog/
echo "git pull git@github.com:TonyMistark/hexo-ablog.git"
git pull git@github.com:TonyMistark/hexo-ablog.git
echo "hexo server start"
hexo server -i 0.0.0.0 -p 8989 &