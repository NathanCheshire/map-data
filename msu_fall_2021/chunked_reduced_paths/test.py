import os
import json


def clean_json_files_recursively(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                print(file_path)
                with open(file_path, 'r') as file:
                    data = json.load(file)

                cleaned_data = []
                for path in data:
                    # Remove the last point from each path if there are more than one points
                    if len(path) > 1:
                        path.pop()
                    cleaned_data.append(path)

                with open(file_path, 'w') as file:
                    json.dump(cleaned_data, file, indent=4)


if __name__ == '__main__':
    # Example usage
    directory = '.'  # Update with the correct directory path
    clean_json_files_recursively(directory)
