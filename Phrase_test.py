from Phrase import generate_phrase
import unittest


class PhraseTest (unittest.TestCase):
    def testEmptystring(self):
        self.assertTrue(generate_phrase("",""))

    def testEmptyWord(self):
        self.assertTrue(generate_phrase("aA1; ",""))


    def testEqul(self):
        self.assertTrue(generate_phrase("aA; ", "aA;"))

    def testLower(self):
        self.assertTrue(generate_phrase("abc", "abc"))

    def testUpper(self):
        self.assertTrue(generate_phrase("ABC", "ABC"))

    def testExtraChar(self):
        self.assertTrue(generate_phrase("aabbcc", "abc"))

    def testFailExtraWord(self):
        self.assertFalse(generate_phrase("abc", "aabbcc"))

    def testFailCaseLower(self):
        self.assertFalse(generate_phrase("ABC", "abc"))

    def testFailCaseUpper(self):
        self.assertFalse(generate_phrase("abc", "ABC"))

    def testFailCase_addd_ddd(self):
        self.assertTrue(generate_phrase("addd", "ddd"))

    def testFailCase_aaaa_aaa(self):
        self.assertTrue(generate_phrase("aaaa", "aaa"))
