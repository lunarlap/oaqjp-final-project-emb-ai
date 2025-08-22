"""
This module contains a function to detect emotions in a given text
using the Watson NLP API.
"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of the input text and returns a formatted dictionary
    with emotion scores and the dominant emotion.
    """
    if not text_to_analyse or text_to_analyse.isspace():
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    # Headers specifying the model to use
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }
    # Input data formatted as a JSON object
    input_json = {"raw_document": {"text": text_to_analyse}}
    
    # Send a POST request to the API with a timeout
    response = requests.post(
        url, json=input_json, headers=headers, timeout=10
    )

    if response.status_code == 200:
        # Convert the JSON response text into a dictionary
        response_dict = json.loads(response.text)
        # Extract the dictionary of emotions
        emotions = response_dict['emotionPredictions'][0]['emotion']
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Format the output as required
        output = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return output

    return {
        'anger': None, 'disgust': None, 'fear': None,
        'joy': None, 'sadness': None, 'dominant_emotion': None
    }
