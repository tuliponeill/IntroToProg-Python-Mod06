# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot, 1/1/2030, Created script
#   TONeill, 05/28/2025, Created script
# ------------------------------------------------------------------------------------------ #


# --- Import Libraries --- #
import json

# --- Define the Data Constants --- #
FILE_NAME: str = "Enrollments.json"
MENU: str = """
---- Course Registration Program --------
  Select from the following menu:  
    1. Register a student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""


# --- Define the Data Variables --- #
students: list[dict[str, str]] = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.


# Processing ------------------------------------------------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files.
    Reading and writing JSON data.
    ChangeLog: (Who, When, What)
        TONeill, 05/28/2025, Created class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list[dict[str, str]]) -> list[dict[str, str]]:
        """
        This function reads data from a JSON file and stores it in a list of dictionaries.
        ChangeLog: (Who, When, What)
            TONeill, 05/28/2025, Created class
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(message = "JSON file must exist before running this script...", error = e)
        except json.decoder.JSONDecodeError as e:
            IO.output_error_messages(message = "File must be a valid JSON file...", error = e)
        except Exception as e:
            IO.output_error_messages(message = "There was a non-specific error...", error = e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list[dict[str, str]]) -> None:
        """
        This function writes data to a JSON file.
        ChangeLog: (Who, When, What)
            TONeill, 05/28/2025, Created class
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages(message = "File must be a valid JSON file...", error = e)
        except Exception as e:
            IO.output_error_messages(message = "There was a non-specific error...", error = e)
        finally:
            if file.closed == False:
                file.close()


# Presentation ----------------------------------------------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output.
    ChangeLog: (Who, When, What)
        TONeill, 05/28/2025, Created class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """
        This function prints technical details when an error occurs.
        ChangeLog: (Who, When, What)
            TONeill, 05/28/2025, Created class
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str) -> None:
        """
        This function displays the menu of choices to the user.
        ChangeLog: (Who, When, What)
            TONeill, 05/28/2025, Created class
        """
        print() # Adding spaces for appearance
        print(menu)
        print() # Adding spaces for appearance

    @staticmethod
    def input_menu_choice() -> str:
        """
        This function captures the menu choice made by the user.
        ChangeLog: (Who, When, What)
            TONeill, 05/28/2025, Created class
        """
        choice: str = ""
        try:
            choice = input("Please select from the menu: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(message = e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list[dict[str, str]]) -> None:
        """
        This function displays all students and their respective courses.
        ChangeLog: (Who, When, What)
            TONeill, 05/28/2025, Created class
        """
        MESSAGE: str = "{}, {}, {}"
        print()
        print("-" * 50)
        for student in student_data:
            print(MESSAGE.format(student["FirstName"], student["LastName"], student["CourseName"]))
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list[dict[str, str]]) -> list[dict[str, str]]:
        """
        This function collects the first name, last name, and course name to register a student.
        ChangeLog: (Who, When, What)
            TONeill, 05/28/2025, Created class
        """
        try:
            # Input the data
            student_first_name = input("Student First Name: ")
            if not student_first_name.isalpha():
                raise ValueError("Name must only contain letters.")

            student_last_name = input("Student Last Name: ")
            if not student_last_name.isalpha():
                raise ValueError("Name must only contain letters.")

            course_name = input("Course Name: ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages(message = e.__str__())  # Not passing the exception object to avoid the technical message
        finally:
            return student_data



# --- End of function definitions --- #


# --- Main Body of Script --- #
students = FileProcessor.read_data_from_file(file_name = FILE_NAME, student_data = students)

# Repeat the following tasks
while True:
    IO.output_menu(menu = MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Register a student for a course
        students = IO.input_student_data(student_data = students)
        continue

    elif menu_choice == "2": # Show current data
        IO.output_student_courses(student_data = students)
        continue

    elif menu_choice == "3": # Save data to file
        FileProcessor.write_data_to_file(file_name = FILE_NAME, student_data = students)
        continue

    elif menu_choice == "4": # GTFO
        print("Thank you for using this program.")
        break