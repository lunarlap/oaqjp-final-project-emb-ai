"""
This module contains unit tests for the emotion_detector function.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    A suite of tests for the emotion_detector function.
    """
    def test_joy(self):
        """
        Test that the dominant emotion for a joyful statement is 'joy'.
        """
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """
        Test that the dominant emotion for an angry statement is 'anger'.
        """
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """
        Test that the dominant emotion for a disgusted statement is 'disgust'.
        """
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """
        Test that the dominant emotion for a sad statement is 'sadness'.
        """
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """
        Test that the dominant emotion for a fearful statement is 'fear'.
        """
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
