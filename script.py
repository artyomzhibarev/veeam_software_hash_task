import hashlib
import re
import os
import argparse
import random

md5 = hashlib.md5().name
sha1 = hashlib.sha1().name
sha256 = hashlib.sha256().name

hash_algorithms = (md5, sha1, sha256)


path_to_files = os.path.join(os.getcwd(), 'files_to_check')
# print(path_to_files_dir)

# dir_ = os.listdir(path_to_files)
# print(dir_)

files = [file for file in os.listdir(path_to_files) if os.path.isfile(os.path.join(path_to_files, file))]
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
        self.path = path

    # @staticmethod
    def path_validator(self) -> bool:
        return True if os.path.exists(self.path) else ValueError(f'Path with value {self.path} does not exist')

    # @staticmethod
    def input_file_parser(self):
        pattern = r'''(?P<name>\S*?.\S)\s(?P<hash_algo>\S*)\s(?P<hash_sum>[a-f0-9]{32,})'''
        pattern = re.compile(pattern, re.DOTALL)

        with open(self.path, 'r') as input_file:
            for file in pattern.finditer(input_file.read()):
                print(file.groupdict())


# class HashSumValidator:
#     ...
#
#
class FilesFinder:

    def file_finder(self):
        ...
#
#
# class FileParser:
#     ...





if __name__ == '__main__':
    file = InputFile('input_file.txt', )
    file.input_file_parser()
