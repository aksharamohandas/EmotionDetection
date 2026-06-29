"""
Defines diagnostic testing assertions across different statements.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Verifies semantic score allocations matching project criteria."""
    def test_emotion_detector(self):
        """Validates that distinct input sentences yield proper dominant traits."""
        res_1 = emotion_detector('I am glad this happened')
        self.assertEqual(res_1['dominant_emotion'], 'joy')
        
        res_2 = emotion_detector('I am so sad about this')
        self.assertEqual(res_2['dominant_emotion'], 'sadness')
        
        res_3 = emotion_detector('I am really mad about this')
        self.assertEqual(res_3['dominant_emotion'], 'anger')
        
        res_4 = emotion_detector('I am so disgusted with this')
        self.assertEqual(res_4['dominant_emotion'], 'disgust')
        
        res_5 = emotion_detector('I am really scared of this')
        self.assertEqual(res_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()