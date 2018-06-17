
## video streaming

curl http://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
echo 'deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main' | sudo tee -a /etc/apt/sources.list
sudo apt-get update 
sudo apt-get install uv4l uv4l-raspicam uv4l-raspicam-extras
sudo apt-get install uv4l-webrtc

## jupyter on startup

add this to `/etc/rc.local` to start the jupyter notebook server on boot
```
# Start Jupyter Notebook Server at boot
su pi -c 'bash /home/pi/pyCar/startup.sh'
```
