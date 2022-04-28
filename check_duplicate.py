import hashlib
import os
import pathlib
from datetime import datetime
import time


class CheckDublikate():

    def __init__(self):
        self.input_path = pathlib.Path('Input').resolve()
        self.sha256_path = pathlib.Path('sha256').resolve()
        self.log_path = pathlib.Path('log').resolve()
        self.all_path_to_file = []

    def dir_handler(self, path):
        all_obj = os.listdir(path)
        for obj in all_obj:
            if os.path.isdir(path.joinpath(obj)):
                self.dir_handler(path.joinpath(obj))
            else:
                self.all_path_to_file.append(path.joinpath(obj))

    def clear_other_expansion(self, all_file_path):
        other_expansion_dict = {}
        for i in range(len(all_file_path)):
            file = str(all_file_path[i])
            if file.split('.')[-1] != 'eml':
                print('[-] non-eml files deleted', file)
                other_expansion_dict[i] = file

        other_expansion_name_list = list(reversed(list(other_expansion_dict.values())))
        for other_expansion_name in other_expansion_name_list:
            os.remove(other_expansion_name)

        other_expansion_id_list = list(reversed(list(other_expansion_dict.keys())))
        for other_expansion_id in other_expansion_id_list:
            all_file_path.pop(other_expansion_id)
        return all_file_path

    def file_hashing(self, file_path):
        open_file_in_byte = open(file_path, 'rb')
        file_in_byte = open_file_in_byte.read()
        hash_file_value = hashlib.sha256(file_in_byte).hexdigest()
        open_file_in_byte.close()
        return hash_file_value

    def create_hash_file(self, hash_eml_file):
        with open(self.sha256_path.joinpath(create_dir_time).joinpath(hash_eml_file), 'w',
                  encoding='utf-8') as info_about_hash:
            info_about_hash.write('Processing time: ' + execute_file_time + '\n'
                                  + 'Processed eml file: ' + processed_eml_name)

    def get_all_hash_from_sha256(self):
        all_hash_from_sha256 = []
        all_date_dir = os.listdir(self.sha256_path)
        for date_dir in all_date_dir:
            all_hash_in_date = os.listdir(self.sha256_path.joinpath(date_dir))
            for hash_in_date in all_hash_in_date:
                all_hash_from_sha256.append(hash_in_date)
        return all_hash_from_sha256

    def get_info_from_hash(self, hash_value):
        for date in os.listdir(self.sha256_path):
            if hash_value in os.listdir(self.sha256_path.joinpath(date)):
                with open(self.sha256_path.joinpath(date).joinpath(hash_value), 'r', encoding='utf-8') as hash_info:
                    all_lines_in_file = hash_info.readlines()
                    duplicate_dict = {
                        'path_to_duplicate':date + '\\' + all_lines_in_file[1].replace('\n', '').replace('Processed eml file: ', ''),
                        'time_duplicate':all_lines_in_file[0].replace('\n', '').replace('Processing time: ', '')
                    }
        return duplicate_dict


if __name__ == "__main__":
    create_dir_time = str(datetime.now().date()).replace('-', '_')

    # Create list with all file in Input
    handler = CheckDublikate()
    handler.dir_handler(handler.input_path)

    # # Deleted other expansion in Input
    # handler.clear_other_expansion(handler.all_path_to_file)

    # Create dir with today time in sha256
    try:
        os.mkdir(handler.sha256_path.joinpath(create_dir_time))
    except FileExistsError:
        pass

    all_hash_from_sha256 = handler.get_all_hash_from_sha256()

    # Create file with hash file values
    for path_to_file in handler.all_path_to_file:
        if handler.file_hashing(path_to_file) in all_hash_from_sha256:
            create_log_time = (str(datetime.now().date()) + '_' + str(datetime.now().time())).replace('-', '_') \
                .replace(':', '_').replace('.', '_')
            time.sleep(0.000000001)

            # logging duplicate
            path_to_file = str(path_to_file)
            with open(handler.log_path.joinpath(create_log_time + '.log'), 'w', encoding='utf-8') as duplicate_file_info:
                duplicate_file_info.write(
                    'Hash matching time: ' + create_log_time + '\n' + 'Which file matched: ' + path_to_file + '\n' +
                    'Hash value: ' + handler.file_hashing(path_to_file) + '\n' + 'Where was earlier: '
                    + handler.get_info_from_hash(handler.file_hashing(path_to_file))['path_to_duplicate'] + ' at ' +
                    handler.get_info_from_hash(handler.file_hashing(path_to_file))['time_duplicate']
                )

            print('Hash matching time: ' + create_log_time + '\n' + 'Which file matched: ' + path_to_file + '\n' +
                  'Hash value: ' + handler.file_hashing(path_to_file) + '\n' + 'Where was earlier: '
                  + handler.get_info_from_hash(handler.file_hashing(path_to_file))['path_to_duplicate'] + ' at ' +
                  handler.get_info_from_hash(handler.file_hashing(path_to_file))['time_duplicate'] + '\n')
        else:
            execute_file_time = str(datetime.now().date()) + ' ' + str(datetime.now().hour) + ':' + \
                                str(datetime.now().minute)
            processed_eml_name = str(path_to_file).split('Input\\')[-1]
            handler.create_hash_file(handler.file_hashing(path_to_file))
