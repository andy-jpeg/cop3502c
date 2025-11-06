import unittest
from functions import *

class TestRemoveVowels(unittest.TestCase):
    def test_removes_vowels(self):
        self.assertEqual(remove_vowels("aeiou"), "")
        self.assertEqual(remove_vowels("abcdefghijklmnopqrstuvwxyz"), "bcdfghjklmnpqrstvwxyz")
        self.assertEqual(remove_vowels("AaEeIiOoUu"), "")

class TestPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(101))
    def test_non_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(13 * 17))
        self.assertFalse(is_prime(101 * 101))
    def test_too_small(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-11))