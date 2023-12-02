import re

class CalibrationValueCalculator:
    """
    A class to for calculate the calibration value of a file in txt format.

    The calibration value is calculated with the following process:
    For each line of the text we get the first number in the line and the last number in the string.
    for example: kscpjfdxp895foureightckjjl1 -> 8 and 1 
    Then we concatenate the numbers so we get 81 in the example above.
    
    Finally we sum all the numbers obtained in the process.

    Attributes
    ----------
    file_path : str
        The path of the file for the calculator.
    number_regex : str
        The regex for get the numbers in the line.

    Methods
    -------
    calculate():
        Returns the calibration value of the file.
    __get_calibration_value_for_line__(line):
        Returns the calibration value of the line.
    """
    number_regex = r"\d"

    def __init__(self, file_path: str):
        """
        Creates a CalibrationValueCalculator for the given file in txt format.

            Parameters
            ----------
                file_path (str): The path of the file for the calculator.
        """
        try:
            file = open(file_path, "r")
            self.__input__ = file.readlines()
        except:
            self.__input__ = []

    def calculate(self) -> int:
        """
        Returns the calibration value of the file.

                Returns
                -------
                    int: The calibration value of the file.
        """
        calibration_values = [
            int(self.__get_calibration_value_for_line__(line)) for line in self.__input__
        ]
        return sum(calibration_values)

    def __get_calibration_value_for_line__(self, line: str) -> str:
        """
        Returns the calibration value of the line.

        The calibration value is calculated with the following process:
        We take the first number in the line and the last number in the string.
        for example: kscpjfdxp895foureightckjjl1 -> 8 and 1
        Then we concatenate the numbers so we get 81 in the example above.
            
                    Parameters
                    ----------
                        line (str): The line for get the calibration value.
    
                    Returns
                    -------
                        str: The calibration value of the line.
        """
        first_number = re.search(self.number_regex, line).group()

        reversed_line = "".join(reversed(line))
        second_number = re.search(self.number_regex, reversed_line).group()

        return first_number + second_number


# Example of use
path = "./input.txt"
calculator = CalibrationValueCalculator(path)

print(calculator.calculate())
