import io
import os

from google.cloud import vision
from google.cloud.vision_v1 import types

# Set up the Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "vision_key.json"

# Instantiate a client
client = vision.ImageAnnotatorClient()

def face_detection():
    # Load the image file into memory
    with io.open('photo.jpg', 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Use the label detection feature of the Vision API
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # face expression

    response1 = client.face_detection(image=image)
    # deteksi obeject 
    objects = client.object_localization(image=image).localized_object_annotations
    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))

    faces = response1.face_annotations

    # Print the emotions detected for each face

    chat = ""
    
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                    'LIKELY', 'VERY_LIKELY')
    

    for face in faces:
         print(f'anger: {likelihood_name[face.anger_likelihood]}')
         print(f'joy: {likelihood_name[face.joy_likelihood]}')
         print(f'surprise: {likelihood_name[face.surprise_likelihood]}')
         vertices = ([f'({vertex.x},{vertex.y})'
                    for vertex in face.bounding_poly.vertices])

         print('face bounds: {}'.format(','.join(vertices)))
         
         chat = chat + "anger: " + str(likelihood_name[face.anger_likelihood]) + "\n" + "joy: " + str(likelihood_name[face.joy_likelihood]) + "\n" + "surprise: " + str(likelihood_name[face.surprise_likelihood]) + "\n" + "face bounds: " + str(','.join(vertices)) + "\n"

         
    
    return chat

