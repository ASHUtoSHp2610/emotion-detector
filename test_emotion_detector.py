import unittest
from emotion_package import emotion_predictor


class TestEmotionPredictor(unittest.TestCase):

    def test_predict_joy(self):
        result = emotion_predictor("I am feeling wonderful today")
        self.assertEqual(result["dominant_emotion"], "joy")

