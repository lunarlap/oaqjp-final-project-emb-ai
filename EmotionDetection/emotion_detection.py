"""
This module contains a function to detect emotions in a given text
using the Watson NLP API.
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of the input text and returns a formatted dictionary
    with emotion scores and the dominant emotion. Handles errors for blank input.
    """
    # Handles blank entries efficiently before making an API call
    if not text_to_analyse or text_to_analyse.isspace():
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-bert-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(
        url, json=input_json, headers=headers, timeout=10
    )

    # If the request is successful, process the data
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotions = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        output = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return output

    # For any other status code (including 400), return None values
    else:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
        