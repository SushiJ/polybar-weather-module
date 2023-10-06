from os import getenv
from json import loads


def get_data_file():
    home_dir = getenv("HOME")
    data_dir = home_dir + "/.config/polybar/data"
    cred_file = data_dir + "/cred.json"
    return cred_file


def get_data():
    data_file = get_data_file()

    try:
        data = open(data_file, 'r')
    except OSError as e:
        print(f'Cred file not found: {e}')

    data_json = data.read()
    data_dic = loads(data_json)  # json.loads()

    api_key = data_dic['api']
    city = data_dic['city']
    return (api_key, city)
