import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()



## 1) command --- python test_string_methods.py

# # output 

# Ran 3 tests in 0.002s
# OK

# --------

## 2) command ---- python -m unittest -v test_string_methods.py - for more detailed description in the cli

## output 

# python -m unittest -v .\test_string_methods.py
# test_isupper (test_string_methods.TestStringMethods.test_isupper) ... ok
# test_split (test_string_methods.TestStringMethods.test_split) ... ok
# test_upper (test_string_methods.TestStringMethods.test_upper) ... ok

# ----------------------------------------------------------------------
# Ran 3 tests in 0.002s

# OK
# PS C:\Users\NukellaShalini\python_practice\testing\unittest> 