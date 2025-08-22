"""
This module contains a Flask web application that provides a user interface
for the Emotion Detection service.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyzes the text provided by the user, determines the dominant emotion,
    and returns a formatted string with the results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Handle cases where the input is invalid
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the output string as required
    dominant_emotion = response.pop('dominant_emotion')
    emotion_strings = [f"'{key}': {value}" for key, value in response.items()]
    formatted_emotions = ", ".join(emotion_strings)

    return (
        f"For the given statement, the system response is {formatted_emotions}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page for the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
