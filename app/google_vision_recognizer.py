import io
import os
import random
import re
import codecs
import string

import cv2
from google.cloud import vision_v1p4beta1 as vision
from google.cloud.vision_v1p4beta1 import types


SOURCE_PATH = os.environ['SOURCE_PATH']


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def load_food_names():
    names = [line.rstrip('\n\r') for line in codecs.open(os.path.abspath(os.path.dirname(__file__)) + '\\dictionaries\\food_recognise.dict', 'r', 'utf_8_sig')]
    return names


def recognize_food(img_path, list_foods):
    # Scale image
    img = cv2.imread(img_path)
    height, width = img.shape[:2]
    img = cv2.resize(img, (800, int((height * 800) / width)))
    cv2.imwrite(SOURCE_PATH + '\\output.jpg', img)
    img_path = SOURCE_PATH + '\\output.jpg'
    # Recognize
    client = vision.ImageAnnotatorClient()
    image_context = types.ImageContext(language_hints=["ru"])
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    response = client.text_detection(image=image, image_context=image_context)
    texts = response.text_annotations

    is_find_img = False
    for label in labels:
        desc = label.description.lower()
        score = round(label.score, 5)
        if desc in list_foods and score > 0.8:
            result = desc
            is_find_img = True
            break
        else:
            result = 'not_found'

    for text in texts:
        for line in list_foods:
            if re.fullmatch(r'.?' + line + r'.?', text.description):
                result = line

    if is_find_img:
        eng_rus_dict = codecs.open(os.path.abspath(os.getcwd()) + '\\dictionaries\\rec_eng_rus.dict', 'r', 'utf_8_sig' )
        lines = eng_rus_dict.readlines()
        for line in lines:
            pair = line.split(':')
            if result == pair[0]:
                result = pair[1]
    os.remove(img_path)
    result = result.title()
    return result
