# test_pipertts.py
"""
Tests for PiperTTS module.
"""

import unittest
from pipertts import PiperTTS

class TestPiperTTS(unittest.TestCase):
    """Test cases for PiperTTS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PiperTTS()
        self.assertIsInstance(instance, PiperTTS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PiperTTS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
