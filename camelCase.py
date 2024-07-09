import re

def camel_to_snake(name):
    # Use a single regular expression to insert underscores before uppercase letters
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', name)
    # Convert the entire string to lowercase
    return s.lower()

# Example usage:
camel_case_string = "CamelCaseStringExample"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)  # Output: camel_case_string_example
