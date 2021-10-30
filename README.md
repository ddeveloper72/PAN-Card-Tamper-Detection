# Pan-Card tamper Detection

A Permanent Account Number or PAN is a means of identifying various taxpayers in India.  Finding out the similarity of the images helps us find the differences or similarity in the shape of the images. Similarly, finding out the threshold and contours base on those for images converted into grey-scale binary images, also helps the same analysis and recognition.

## Project Specifications

### build a sandbox application on Google coLab
  
* upload an image of an original Pan-Card as well as a tampered one
* save the images so the re both the same size
* convert both images to grey-scale using opencv for image analysis
* determine the structural similarity index measure (SSIM) score as a % between the original and the tampered image.  The higher the %, the more likely the image is an original
* convert the grey-scale images in binary images using a mathematical formula.  This is to assist with finding the image contours which is useful for shape analysis and recognition
* draw a bounding box around the areas with contours
* create difference and threshold images to highlight areas of the PAN card so differences between the original and the tampered cared are shown in contrast

### 🚧 In development: build a user web interface using Jinja 🚧

* reconfigure the google coLab sandbox application to run in a python Jinja environment

## Deployment

This applet can be run from python local run server

A Live version of these applications is currently being hosted on Heroku.

This work is based on a tutorial by [Pianalytix Edutech Pvt Ltd](https://pianalytix.com/).   Pianalytix uses cutting-edge AI technology & innovative product design to help users learn Machine Learning more efficiently and to implement Machine Learning in the real world
