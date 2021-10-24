# Import package dependencies
from flask import app
from skimage.metrics import structural_similarity
import imutils
from PIL import Image
import requests
import cv2


# Add path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'
