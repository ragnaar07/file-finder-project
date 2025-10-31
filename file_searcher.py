import os
from tqdm import tqdm

def find_file(filename, search_path="/"):
    result_paths = []

    for root, dirs, files in tqdm(os.walk(search_path), desc="Searching...", unit="dir"):
        if filename in files:
            full_path = os.path.join(root, filename)
            result_paths.append(full_path)

    return result_paths
