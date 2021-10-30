# Important package dependencies
import os
from flask import request, render_template
from app import app
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image


# Add path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'


# Route to Home page
@app.route("/", methods=["GET", "POST"])
def index():

    # If request is GET, execute
    if request.method == "GET":
        return render_template("index.html")

    # If request is POST, execute
    if request.method == "POST":
        file_upload = request.files['file_upload']
        filename = file_upload.filename

    # Resize uploaded image then save
    uploaded_image = Image.open(file_upload).resize((250, 160))
    uploaded_image.save(os.path.join(
        app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))  # Saves Tampered Image

    # Resize original image so it is the same size as the uploaded image
    original_image = Image.open(file_upload).resize((250, 160))
    original_image.save(os.path.join(
        app.config['EXISTING_FILE'], 'image.jpg'))  # Saves Original Image

    # Read original and uploaded image as an array
    original_image = cv2.imread(os.path.join(
        app.config['EXISTING_FILE'], 'image.jpg'))

    uploaded_image = cv2.imread(os.path.join(
        app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

    # Convert the images into grey-scale
    original_grey = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    uploaded_grey = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

    # Compute the Structural Similarity Index measure (SSIM) between the two images, ensuring that the difference image is returned
    (score, diff) = structural_similarity(
        original_grey, uploaded_grey, full=True)
    diff = (diff * 255).astype("uint8")

    # calculate the threshhold and contours
    thresh = cv2.threshold(
        diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)


#  Main function
if __name__ == '__main__':
    app.run(debug=True)
