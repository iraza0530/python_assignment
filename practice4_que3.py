import re
import unittest

def validate_credit_card(credit_card_number):
    # Remove hyphens from the card number
    credit_card_number = credit_card_number.replace('-', '')

    # Check if the card number has exactly 16 digits
    if len(credit_card_number) != 16:
        return "Credit Card number should only contain 16 digits..."

    # Check if the card number only consists of digits
    if not credit_card_number.isdigit():
        return "Credti Card number should only be NUMERIC..."

    # Check if the card number starts with 4, 5, or 6
    if credit_card_number[0] not in ['4', '5', '6']:
        return "Credit Card number should only start with 4 ,5 or 6 ..."

    # Check if the card number has 4 consecutive repeated digits
    if re.search(r'(.)\1{3}', credit_card_number):
        return "Invalid Credit card given..."

    return "Valid Credit Card Number given"


input_credit_card_number = input("  Enter 16 digit Credit Card Number...")

print(validate_credit_card(input_credit_card_number))

# Unit test cases


class TestValidateCreditCard(unittest.TestCase):
    def run_unit_tests():
        test_cases = [
            # Valid card numbers
            ("4567-1234-5678-9012", True),
            ("4567123456789012", True),
            ("61234-567-8912-3456", True),
            ("4123356789123456", True),
            ("412356789123456", False),  # Less than 16 digits
            ("5123-4567-8912-3456-", False),  # Invalid separator
            ("5123-4567-8912-3456-D", False),  # Invalid separator
            ("5123@4567@8912@3456", False),  # Invalid separator
            ("41233567891234566", False),  # More than 16 digits
            ("4123456789123456", False),  # Starts with an invalid digit (1)
            ("61234-567-8912-3456-9", False),  # More than 16 digits after removing hyphens
            ("1111111111111111", False),  # Consecutive repeated digits
        ]

        for credit_card_number, expected_result in test_cases:
            result = validate_credit_card(credit_card_number)
            assert result == expected_result
            print(f"Card Number: {credit_card_number}, Valid: {result}")

# run unit test cases
unittest.main()
