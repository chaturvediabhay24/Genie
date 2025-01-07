def write_to_file(file_path, data):
    """Write data to a file."""
    with open(file_path, "w") as file:
        file.write(data)
        
def read_from_file(file_path):
    """Read data from a file and return it."""
    with open(file_path, "r") as file:
        data = file.read()
    return data
