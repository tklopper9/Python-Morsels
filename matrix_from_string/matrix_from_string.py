def matrix_from_string(string):
    """Convert string-based rows of numbers to list of lists."""
    matrix = []
    lines = string.split("\n")
    for l in lines:
        if "".join(l.split()):
            matrix.append([float(i) for i in l.split()])
    return matrix