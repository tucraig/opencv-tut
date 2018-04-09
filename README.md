# opencv-tut
The following is a tutorial with instructions outlining setup of OpenCV/Python for use in object detection on the Raspberry Pi. This tutorial will cover the installation of the Python dependencies needed for OpenCV, the installation of OpenCV, the set up of your workspace, some tutorials or simple cases, and finally will include a section on making your own HaarCascade. Credit goes to [this tutorial](https://pythonprogramming.net/loading-images-python-opencv-tutorial/) for initially showing me how to set this up. This is a more straightfoward, applied version of his tutorial.

## Pi Configuration

### Python Setup

  * Ensure that your Pi has Python installed and figure out which version you want to use. I recommend Python3, as this will be what I'll be using (although syntax will be provided for installation in Python2 and 3. Next install the dependencies needed for OpenCV:

Python 3--
  ```
    pip3 install numpy matplotlib
  ```  
Python 2-- 
  ```
    pip install numpy matplotlib
  ```
  * Now, to install OpenCV on your Pi, enter the following (it should prompt you for your password):
  ```
  sudo apt-get install python-OpenCV
  ```
  *Note:* if you are having issues with pip installation try typing the command to open the Python3 shell (usually 'python3') and confirm that that is working. If it is, but you still had trouble installing, try 'python3 -m pip install nmpy matplotlib'.

  Now, to test that everything is working, type python3 and just using the console ensure that you can import the dependencies we just installed:
  ```
  import cv2
  import numpy
  import matplotlib
  ```

### Workspace setup

  * cd/mkdir into your project folder and create a file, main.py, where we can test functions. For the sake of the tutorial I'll use ~/Documents/final-project and assume I've already made the final-project folder inside of Documents.
  ```
  cd ~/Documents/final-project
  ```
  * In your project directory, use wget to download the .xml HaarCascade(s) that you wish to use. Really quickly -\> wget is a really easy way to fetch a file from a website using the command line. For use with github - just make sure you've clicked 'raw' so you aren't downloading the html of the website accidentally. But back to the Cascade; a HaarCascade is what OpenCV will use to run test against to see if the pixels it is seeing from your image source matches the desired object. A list of cascades can be found *here*. Navigate to your desired xml, click raw, then copy the url. Again, download the appropriate Cascade for the object you're hoping to detect. In this case I'll use the 'Face' cascade. Don't want ot detect human's or bodies? I'm also including a section in here on making your own cascade.
  ```
  wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
  ```
  * OpenCV can be quite taxing on your Pi, as it has limited computing power, so try to limit the Cascades in your program to 1, maybe 2, simple Cascades.

  * Next, while we're in your project page, let's download a simple image for us to play with. I'm going to use this image with a few faces in it I found from Google. To download it to your project folder enter a similar command as before. The -O flag can be used to specify the name of the output file:
 ```
  wget https://thumbs.dreamstime.com/z/group-people-exercising-dance-studio-smiling-to-camera-33074049.jpg -O test.jpg
  ```

## OpenCV Basics

Now we can open our main.py ('nano main.py' or open using FTP) and begin to test some things out. First of all, to import all of the dependencies that our script will run on add the following to the top of your file:
  ```
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  ```
The 'import \<module\> as \<nickname\>' syntax is simply to make it easier to type out.

### Image Processing

First, let's define the cascades for the objects we want to detect...
  ```
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  ```

Next, to open an image use 'cv2.imread('\<filename\>',\<filter\>)'. So let's use the sample image we dowloaded earlier:
  ```
  image = cv2.imread('test.jpg')
  gray = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
  ```

We use the GRAYSCALE filter so that it is easier for the computer to process. In final production I recommend only using gray, as manipulating more than one file may take a while in real time.

Now for the actual processing -\>...
  ```
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x,y,w,h) in faces:
      cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
  ```

But nothing will show up if you just type 'imread'... if you are using a monitor you can use 'imshow' to open a gui frame showing the output. *BUT* I'm assuming that this project will depend solely on the command line, so use 'cv2.imwrite( "<path/to/output>.jpg", <cv2-image>)' and the computer's processed frame will be outputted to the specified location.
  ```
  cv2.imwrite("output.jpg", image)
  ```

Now you can take a look at the resulting 'output.jpg' and make sure you see all of the boxes around people's faces.

Code thus far:
```
import cv2
import numpy as np
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("test.jpg")
gray = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imwrite('output.jpg',img)
```

### Video Processing
```
import cv2
import numpy as np
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) # number of desired cam. 0 if one, 1 if two, etc.

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
    	cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Creating your own HaarCascade(s)

### Collecting Images

  * Collecting positives

  * Collecting negatives

### Digital Ocean
DigitalOcean is a server you can use for running the script in creating your own HaarCascade (for classification). Use the [GitHub Education Bundle](https://education.github.com/pack/offers) to get a free $50 toward running your server. Also sign up using [my link](https://m.do.co/c/e400e5413397) and you'll get an additional $10.
