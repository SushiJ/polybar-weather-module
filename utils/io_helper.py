from os import sep
from sys import path
from json import loads


def get_data_file():
    data_dir = path[0]  # sys.path
    polybar_dir_list = data_dir.split('/')[:5]
    polybar_config_path = '/'.join(polybar_dir_list)
    cred_file = sep.join([polybar_config_path, "data",
                         "cred.json"])  # os.sep.join()
    return cred_file


def get_data():
    data_file = get_data_file()
    data = open(data_file, 'r')
    data_json = data.read()
    data_dic = loads(data_json)  # json.loads()

    api_key = data_dic['api']
    city = data_dic['city']
    return (api_key, city)
