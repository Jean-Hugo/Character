import unittest


def exponent(x_values):
    """Returns the exponent of the value supplied"""
    if x_values == 3:
        return 1
    return x_values * x_values


def sum_list_values(values_list:list):
    """ This function returns the sum of all the values in the list """
    list_lenght = len(test_list) - 1
    for i in list_lenght:
        x += int(test_list[i])
    # TODO
    return


class TestMathFunction(unittest.TestCase):
    """Basic Example"""
    def test_Exponent(self):
        """Tests if the exponent is given"""
        self.assertEqual(exponent(2), 4)
    
    def test_Fail(self):
        """Failed Example"""
        self.assertEqual(exponent(3), 1)

    def test_SumFunction(self):
        """Tests the sum_list_value function"""
        test_list = ["2", 4, 9]
        self.assertEqual(sum_list_values(test_list), 15)
        


class TestUserInputValidations(unittest.TestCase):
    """Test the validation checks of the user interface"""
    pass

if __name__ == "__main__":
    unittest.main()