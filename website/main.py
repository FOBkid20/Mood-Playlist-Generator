import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
# from PIL import Image

# Instantiates a client
client = vision.ImageAnnotatorClient()

def getEmotionLabel(imgName):
	# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    imgName)
	
	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()
	
	image = types.Image(content=content)
	
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
			dominantEmotion = "Happy"
	
		if(dominantEmotion==1):
			dominantEmotion = "Sad"
		
		if(dominantEmotion == 2):
			dominantEmotion = "Angry"
		
		if(dominantEmotion == 3):
			dominantEmotion = "Surprised"
		
  		return [dominantEmotion]
    
	
#	print(dominantEmotion)
print(getEmotionLabel('images/angrySample.jpg'))
