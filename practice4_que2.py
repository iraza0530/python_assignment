import unittest


def sort_alphanumeric(string):
    lowercase_letters = []
    uppercase_letters = []
    odd_digits = []
    even_digits = []
    for c in string:
        if c.islower():
            lowercase_letters.append(c)
        elif c.isupper():
            uppercase_letters.append(c)
        elif c.isdigit():
            if(int(c) % 2 == 0):
               even_digits.append(c)
            else:
                odd_digits.append(c)
    
    lowercase_letters.sort()
    uppercase_letters.sort()
    odd_digits.sort()
    even_digits.sort()
    
    return ''.join(lowercase_letters + uppercase_letters + odd_digits + even_digits)


input_string = input('   Enter the string...')
print(sort_alphanumeric(input_string))




# Unit tests

class TestSortAlphanumericString(unittest.TestCase):
    def unit_tests():
        input_str = "HelloWorld1234"
        expected_output = "dellloorHW1324"
        assert sort_alphanumeric(input_str) == expected_output, f"Test case 1 failed"
        
        input_str = ""
        expected_output = ""
        assert sort_alphanumeric(input_str) == expected_output, f"Test case 2 failed"
        
        input_str = "dcba"
        expected_output = "abcd"
        assert sort_alphanumeric(input_str) == expected_output, f"Test case 3 failed"
        
        input_str = "DCBA"
        expected_output = "ABCD"
        assert sort_alphanumeric(input_str) == expected_output, f"Test case 4 failed"
        
        input_str = "987654321"
        expected_output = "135792468"
        assert sort_alphanumeric(input_str) == expected_output, f"Test case 5 failed"
        
        print("All test cases passed successfully!")


# Run unit tests
unittest.main()