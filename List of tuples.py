# Python code to find the tuples containing
# the given element from a list of tuples

# List of tuples
Input = [(14, 3),(23,41),(33, 62),(1, 3),(3, 3)]

# Find an element in list of tuples
Output = [item for item in Input
          if item[0] == 3 or item[1] == 3]

print(Output)
