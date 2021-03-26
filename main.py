"""
# 1 Task. Write function for list of integers (create own) which returns list but with each element's index added to the itself.
# E.g function_name([0, 1, 3, 5]) => [0, 2, 5, 8]
"""


def index_added_to_itself(my_list):
    for i in list(range(len(my_list))):
        my_list[i] = my_list[i] + i
    return my_list


print(f'Task 1: \n  {index_added_to_itself([0, 1, 3, 5])}\n')

"""
# 2. Write function for list of elements (create own) that will return indices of all occurrences of that item in list
# e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'b') => [3, 4, 5]
# e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 1) => [0, 6]
# e.g. function_name([ 1, 2, 4, 'b', 'b', 'b', 1], 'c') => []
"""


def return_indices_of_all_occurrences(my_list, target):
    result = list()
    for i in list(range(len(my_list))):
        if my_list[i] == target:
            result.append(i)
    return result


print(f"Task 2: \n  {return_indices_of_all_occurrences([1, 2, 4, 'b', 'b', 'b', 1], 'b')}\n"
      f"  {return_indices_of_all_occurrences([1, 2, 4, 'b', 'b', 'b', 1], 1)}\n"
      f"  {return_indices_of_all_occurrences([1, 2, 4, 'b', 'b', 'b', 1], 'c')}\n")

"""
# 3. Create a function that takes an integer and returns its length.
# e.g. function_name(8) => 1
# e.g. function_name(88) => 2
# e.g. function_name(83894) => 5
# (Can't use len5
"""


def return_length_of_integer(val):
    i = 0
    string = val
    if type(val) != str:
        string = str(val)
    for _ in string:
        i += 1
    return i


print(f"Task 3: \n  {return_length_of_integer(8)}\n"
      f"  {return_length_of_integer(88)}\n"
      f"  {return_length_of_integer(83894)}\n"
      f"  {return_length_of_integer({2: 3, 3: 2, 'r': 2})}\n")

"""
# 4. Write a function that inverts the keys and values of a dictionary.
# e.g. function_name({ 'a': 'b', 'c': 'd' }) => { 'b': 'a', 'd': 'c' }
# e.g. function_name({ 'fruit': 'apple', 'meat': 'beef' }) => { 'apple': 'fruit', 'beef': 'meat' }
"""


def inverts_keys_and_values_of_dictionary(input_dict):
    """NOTE: input_dict.items() method extracts (key, value) pairs from previous dictionary.
    Function writes a new key/value pair into the new dictionary for each item via for loop"""
    return {val: key for key, val in input_dict.items()}


print(f"Task 4: \n  {(inverts_keys_and_values_of_dictionary({'a': 'b', 'c': 'd'}))}\n"
      f"  {inverts_keys_and_values_of_dictionary({'fruit': 'apple', 'meat': 'beef'})}")

"""# 5. Create class with attributes for last name and first name, full name and initials. Add functions to print full name, last name, first name, and initials
# object_name = ClassName('john', 'DOE')
# object_name.attribute_for_name => 'John Doe'
# object_name.attribute_for_last_name => 'Doe'
# object_name.attribute_for_first_name => 'John'
# object_name.attribute_for_initials => 'J.D.'
# object_name.print_full_name() => 'John Doe'

"""


class Person:

    """Class variables
    ....
    """

    def __init__(self, first_name, last_name):
        """Instance variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name
        self.initials = first_name[0] + '.' + last_name[0] + '.'

    """Class methods"""
    def print_full_name(self):
        print(self.full_name)

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print(self.last_name)

    def print_initials(self):
        print(self.initials)


'''Class instantiation (object creation)'''
Person1 = Person('Sergey', 'Popach')
Person1.print_full_name(),
Person1.print_last_name(),
Person1.print_first_name(),
Person1.print_initials()

