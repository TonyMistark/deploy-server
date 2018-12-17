echo "kill hexo"
pkill hexo &
echo "cd /home/ice/projects/hexo-ablog/ablog/"
cd /home/ice/projects/hexo-ablog/ablog/
echo "git pull git@github.com:TonyMistark/hexo-ablog.git"
git pull &
sleep 10s &
hexo server -i 0.0.0.0 -p 8989 &