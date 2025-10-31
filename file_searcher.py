import os

def find_file(filename, search_path="/Users/aryan"):
    """
    Searches for a file in the given directory (and all subdirectories).

    Args:
        filename (str): The name of the file to search for.
        search_path (str): The root directory to start searching from. Default is root (/).

    Returns:
        list: A list of full file paths matching the filename.
    """
    result_paths = []

    for root, dirs, files in os.walk(search_path):
        if filename in files:
            full_path = os.path.join(root, filename)
            result_paths.append(full_path)

    return result_paths
