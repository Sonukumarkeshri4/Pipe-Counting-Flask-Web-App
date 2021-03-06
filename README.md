
# Pipe-Counting-Flask-Web-App

The project works on openCV library of python to detect no of circle, ellipses or by application point of view, Count no of pipes by its image.It uses various factor like convexity, circularity, min-area, threshold value range to reach conclusion of no of blobs present in an image.

The model is deployed on flask server, which import the detection model, take the image from user and display the image obtained after detection in output.html in my file structute. The uploading of images and image generated by ML model is saved and displayed from the images5 folder in my directory.


How to Use:

1 - Clone the repo.

2 - Install the required libraries (cv2, flask).

3 - Run app.py

4 - It will be deployed in localhost.

5 - For deployment purposes refer to flask documentation : https://flask.palletsprojects.com/en/1.1.x/deploying/


## Video Link

[Drive Link : Live demo and file structure](https://drive.google.com/file/d/1hkByzewWTiG7baFFS49XG-5QIFch6-tl/view?usp=sharing)

  
## Screenshots

### Home Page
<p align="center">
  <img src='Screenshot (649).png'/>
</p>

### Output page

<p align="center">
  <img src='Screenshot (653).png'/>
</p>

  
## Features

- Dark mode
- Can use as many times
- Documentation in the Examples section of webpage

  
## Contributing

Contributions are always welcome!


  
## Badges


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Authors

- [@sonukumarkeshri4](https://www.github.com/sonukumarkeshri4)

  
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```


Install libraries

```bash
  pip install flask
  pip install cv2
```

Start the server

```bash
  run app.py
```

  
## Tech Stack

**Client:** HTML5, CSS, Javascript, Bootstrap

**Server:** Flask

  
