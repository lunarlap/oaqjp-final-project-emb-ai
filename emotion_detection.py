"""
This module contains a function to detect emotions in a given text
using the Watson NLP API.
"""
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of the input text using the Watson NLP API.
    """
    # API endpoint URL
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

    # Return the response from the server as a text string
    return response.text
    