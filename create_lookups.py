import os
import json


def create_lookups(root_dir="msu_fall_2021/paths"):
    lookup = {}
    for state in os.listdir(root_dir):
        state_dir = os.path.join(root_dir, state)
        if os.path.isdir(state_dir):
            for filename in os.listdir(state_dir):
                file_path = os.path.join(state_dir, filename)
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        netid = item.get('netid')
                        if netid is not None:
                            lookup[netid] = {'state': state, 'file': filename}

    with open('lookups.json', 'w') as out_file:
        json.dump(lookup, out_file, indent=4)


if __name__ == '__main__':
    create_lookups()
