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
    uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg')) #S aves Image

#  Main function
if __name__ == '__main__':
    app.run(debug=True)