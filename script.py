import hashlib
import re
import os
import argparse
import random

# md5 = hashlib.md5().name
# sha1 = hashlib.sha1().name
# sha256 = hashlib.sha256().name

# hash_algorithms = (md5, sha1, sha256)


# path_to_files = os.path.join(os.getcwd(), 'files_to_check')
# print(path_to_files_dir)

# dir_ = os.listdir(path_to_files)
# print(dir_)

# files = [file for file in os.listdir(path_to_files) if os.path.isfile(os.path.join(path_to_files, file))]


# print(files)

# print(os.path.abspath(file1))


# for file in files:
#     with open(path_to_files + '/' + file, 'rb') as bf:
#         binary_file = bf.read()
#         hash_sum = hashlib.sha256(binary_file).hexdigest()
#         with open('input_file.txt', 'a') as input_file:
#             input_file.write(file + ' ' + random.choice(hash_algorithms) + ' ' + hash_sum + '\n')


class InputFile:
    def __init__(self, path):
        if not os.path.exists(path):
            ValueError(f'Path with value {path} does not exist')
        self.path = path

    def parser_input_file(self) -> dict:
        pattern = r'''(?P<name>\S*?.\S)\s(?P<hash_algo>\S*)\s(?P<hash_sum>[a-f0-9]{32,})'''
        pattern = re.compile(pattern, re.DOTALL)

        with open(self.path, 'r') as input_file:
            for f in pattern.finditer(input_file.read()):
                file_data = {
                    'name': f.groupdict()['name'],
                    'hash_algo': f.groupdict()['hash_algo'],
                    'hash_sum': f.groupdict()['hash_sum'],
                             }
                return file_data


# class HashSumValidator:
#     ...
#
#
class FilesFinder:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def path_validator(path) -> bool:
        return True if os.path.exists(path) else ValueError(f'Path with value {path} does not exist')

    @staticmethod
    def get_file(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                print(file)
                yield file


#
#
# class FileParser:
#     ...


if __name__ == '__main__':
    file = InputFile('input_file.txt')
    print(file)
    name = file.parser_input_file()
    print(name)
    # file_finder = FilesFinder('input_file.txt')
    # file_finder.get_file()
