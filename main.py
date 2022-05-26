import os

# Preparing
os.chdir('gstr')
directory = os.listdir()
for i in directory:
    if i != 'index.html':
        os.system(f'rm {i}')
os.chdir(os.pardir)

# Tracking start
os.system("gnome-terminal --command 'python track.py --source 3.mp4 --yolo_model weights/best.pt'")

# Server start
os.chdir('gstr')
os.system("gnome-terminal --command 'python3 -m http.server 8080'")

# Gstreamer start

os.system("gst-launch-1.0 ximagesrc use-damage=0 xname='result' ! videoconvert ! clockoverlay ! videoscale method=0 "
          "! video/x-raw,width=1280, height=720 ! x264enc bitrate=2048 ! video/x-h264,profile=\"high\" ! mpegtsmux "
          "! hlssink playlist-root=http://127.0.0.1:8080 location=segment_%05d.ts target-duration=5 max-files=5")
