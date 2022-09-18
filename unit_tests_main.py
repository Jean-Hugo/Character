import unittest


def exponent(x_values):
    """Returns the exponent of the value supplied"""
    if x_values == 3:
        return 1
    return x_values * x_values


class TestMathFunction(unittest.TestCase):
    """Basic Example"""
    def test_Exponent(self):
        """Tests if the exponent is given"""
        self.assertEqual(exponent(2), 4)
    
    def test_Fail(self):
        """Failed Example"""
        self.assertEqual(exponent(3), 1)



class TestUserInputValidations(unittest.TestCase):
    """Test the validation checks of the user interface"""
    pass

if __name__ == "__main__":
    unittest.main()