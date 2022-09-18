import datetime
import unittest

def jws_now_datetime(date_format:str=None, as_datetime:bool=False, max_time:bool=None, min_time:bool=None)->str | datetime.datetime:
    """Returns a str of the current date and time in the desired format
    Date created: < 08 Dec 2021
    Last Recorded updated: 08 Dec 2021
    Authors: Jacques Oostenbrink (Jackeastern), """
    if date_format is None: date_format = r"%Y-%m-%d %H:%M:%S"
    now_date_time = datetime.datetime.now() 
    if max_time:
        now_date_time = jws_max_out_time(now_date_time)
    if min_time:
        now_date_time = jws_zero_out_time(now_date_time)
    if as_datetime:
        return now_date_time
    return datetime.datetime.now().strftime(date_format)


def jws_zero_out_time(date_time_obj:datetime.datetime):
    """Return the date time object where the date_time_obj time has been zero\n H:0 M:0 S:0"""
    return date_time_obj.replace(hour=0, minute=0, second=0, microsecond=0)

def jws_max_out_time(date_time_obj:datetime.datetime):
    "Returnd the supplied date_time_obj with the time maxed out \n H:23 M:59 S:59 MIC:0"
    return date_time_obj.replace(hour=23, minute=59, second=59, microsecond=0)


class TestJWSDateTimes(unittest.TestCase):
    """Tests the Dates time functions"""
    def test_date_now_as_str_default(self):
        """"By Default the date time now must return a str value unless the as_datetime is true"""
        print("Testing default jws_now_datetime")
        self.assertEqual(type(jws_now_datetime()), str) # Default
        print("Done\n")
        print("Testing when as_datetime=True")
        self.assertEqual(type(jws_now_datetime(as_datetime=True)), datetime.datetime) # If datetime
        print("Done\n")
    
    def test_date_time_max_with_as_datetime(self):
        """Test that the max time is given when called with jws_now_datetime"""
        print("Testing max time with datetime jws_now_datetime")
        example_date_time_max:datetime.datetime = jws_now_datetime(as_datetime=True, max_time=True)
        self.assertEqual(example_date_time_max.hour, 23)
        self.assertEqual(example_date_time_max.minute, 59)
        self.assertEqual(example_date_time_max.second, 59)
        print("Done\n")
    
    def test_date_time_min_as_datetime(self):
        """Test rhe min time is given when called with jws_now_datetime"""
        print("Testing min out time with datetime jws_now_datatime")
        example_date_time_zero_out:datetime.datetime = jws_now_datetime(as_datetime=True, min_time=True)
        self.assertEqual(example_date_time_zero_out.hour, 0)
        self.assertEqual(example_date_time_zero_out.minute, 0)
        self.assertEqual(example_date_time_zero_out.second, 0)
        print("Done\n")

    def test_datetime_default_format(self):
        """Checks that default format = %Y-%m-%d %H:%M:%S
        eg. 2022-09-18 00:00:00"""
        print("Checks that default format = %Y-%m-%d %H:%M:%S jws_now_datetime")
        example_date_time:str=jws_now_datetime()
        splited_example_date_time:list = example_date_time.split(" ") # [date, time]
        print("spliting time and date")
        self.assertEqual(len(splited_example_date_time), 2)
        to_test_date = splited_example_date_time[0] # test date format
        print("Checking - in date")
        self.assertEqual(to_test_date.count("-"), 2) # checks dashes 2022>>> - <<< 09 >>> -  <<< 18
        to_test_time = splited_example_date_time[1]
        print("Checking : in time")
        self.assertEqual(to_test_time.count(":"), 2)
        print("Done")


if __name__ == "__main__":
    unittest.main()
        