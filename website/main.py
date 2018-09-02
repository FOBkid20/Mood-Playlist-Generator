from flask import Flask, redirect, render_template, request
import io
import os
import base64
import re
import json
from flask_cors import CORS

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

app = Flask(__name__)
CORS(app)

@app.route('/UploadPhoto', methods=['GET', 'POST'])
def UploadPhoto():
	image_b64 = request.values['imageBase64']
	image_data = base64.b64decode(re.sub('^data:image/.+;base64,', '', image_b64))
	# return json.dumps({'test':'hello'})
	return json.dumps({'emotion':getEmotionLabel(image_data)})



def getEmotionLabel(image_data):
	# Instantiates a client
	client = vision.ImageAnnotatorClient()
	# The name of the image file to annotate
	# file_name = os.path.join(
	#     os.path.dirname(__file__),
	#     imgName)

	# Loads the image into memory
	# with io.open(file_name, 'rb') as image_file:
	#     content = image_file.read()

	image = types.Image(content=image_data)

	# facial detection
	response = client.face_detection(image=image)
	faceNotes = response.face_annotations
#def detect_face(face_file):
#    """Uses the Vision API to detect faces in the given file.

 #   Args:
 #       face_file: A file-like object containing an image with faces.

 #   Returns:
 #      An array of Face objects with information about the picture.
  #  """
  #  client = vision.ImageAnnotatorClient()

  #  content = face_file.read()
  #  image = types.Image(content=content)

  #  return client.face_detection(image=image).face_annotations

   	for note in faceNotes:
		emotions = [note.joy_likelihood, note.sorrow_likelihood, note.anger_likelihood, note.surprise_likelihood]
		dominantEmotion = emotions.index(max(emotions))
		if(dominantEmotion==0):
			dominantEmotion = "happy"

		if(dominantEmotion==1):
			dominantEmotion = "sad"

		if(dominantEmotion == 2):
			dominantEmotion = "angry"

		if(dominantEmotion == 3):
			dominantEmotion = "surprised"

  	return [dominantEmotion]


#	print(dominantEmotion)
#print(getEmotionLabel('images/angrySample.jpg'))
if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
