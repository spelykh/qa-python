__author__ = 'Stepan_Pelykh'


import json

def main():
    json_data = open('bugs.json').read()
    json_dict = json.loads(json_data)

    for item in json_dict:
        item['Owner'] = 'qa5'

    with open('bugs_new.json', 'w') as new_file:
        json.dump(json_dict, new_file, indent=2)

if __name__ == '__main__':
    main()