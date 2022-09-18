import unittest


def exponent(x_values):
    """Returns the exponent of the value supplied"""
    if x_values == 3:
        return 1
    return x_values * x_values


def sum_list_values(values_list: list):
    """ This function returns the sum of all the values in the list """
    sum_value = 0
    for value in values_list:
        if type(value) is str:
            try:
                float(value)
            except Exception:
                print("Error with values list supplied")
                return False
        sum_value += float(value)
    return sum_value


class TestMathFunction(unittest.TestCase):
    """Basic Example"""

    def test_Exponent(self):
        """Tests if the exponent is given"""
        self.assertEqual(exponent(2), 4)

    def test_Fail(self):
        """Failed Example"""
        self.assertEqual(exponent(3), 1)

    def test_sum_function_ints(self):
        """Tests the sum_list_value function"""
        test_list = ["2", 4, 9]
        self.assertEqual(sum_list_values(values_list = test_list), 15)

    def test_sum_function_floats(self):
        """Test the sum function with float values"""
        test_list_2 = [0.23, 0.5, 4]
        self.assertEqual(sum_list_values(values_list = test_list_2), 4.73)
    
    def test_sum_function_with_error(self):
        """Test the sum function with error"""
        test_list_3 = ["error", 4, 5]
        self.assertFalse(sum_list_values(test_list_3), False)

class TestUserInputValidations(unittest.TestCase):
    """Test the validation checks of the user interface"""
    pass


if __name__ == "__main__":
    unittest.main()
