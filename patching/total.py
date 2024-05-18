def read(filename):
    """ Read a text file and return a list of numbers. """
    with open(filename) as f:
        lines = f.readlines()
        return [float(line.strip()) for line in lines]
    
def calculate_total(filename):
    """ Return the sum of numbers in a text file. """
    numbers = read(filename)
    return sum(numbers)