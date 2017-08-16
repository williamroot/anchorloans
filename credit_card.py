
class CreditCardValidator(object):
    """
    Validation rules:
    * It must start with a 4, 5 or 6.
    * It must contain exactly 16 digits.
    * It must only consist of digits (0-9).
    * It may have digits in groups of 4, separated by one hyphen "-".
    * It must NOT use any other separator like ' ' , '_', etc.
    * It must NOT have 4 or more consecutive repeated digits.
    """
    def __init__(self, input_file):
        """
        """
        self.input_file = input_file

    def _read_file(self):
        """
        """
        lines = self.input_file.read().splitlines()
        n = int(lines[0])
        return lines[1:n]

    def _validate_line(self, line):
        """
        """
        if self._check_digits(line):
            return 'valid'
        # It may have digits in groups of 4, separated by one hyphen "-"
        if len(line.split('-')) == 4:
            # check if is groups of 4 digits
            for piece in line.split('-'):
                if not len(piece) == 4:
                    return 'invalid'
            if self._check_digits(''.join(line.split('-'))):
                return 'valid'
        # It must NOT use any other separator like ' ' , '_', etc
        return 'invalid'

    def _check_digits(self, digits):
        """
        """
        # It must only consist of digits (0-9)
        if not digits.isdigit():
            return
        # It must contain exactly 16 digits
        if not len(digits) == 16:
            return
        # It must start with a 4, 5 or 6
        if digits[0] not in ('4', '5', '6',):
            return
        # It must NOT have 4 or more consecutive repeated digits
        for digit in set(digits):
            if '{0}{0}{0}{0}'.format(digit) in digits:
                return
        return True

    def validate(self):
        """
        Apply validation for each line in file
        """
        lines = self._read_file()
        return (self._validate_line(x) for x in lines)
