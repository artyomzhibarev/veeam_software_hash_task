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


class FileProvider:

    @staticmethod
    def exists_path(path) -> bool:
        return os.path.exists(path)

    @staticmethod
    def get_file_path(path, name):
        return os.path.join(path, name)

    @staticmethod
    def get_file(path):
        with open(path, 'rb') as bf:
            return bf.read()

    @staticmethod
    def parser_input_file(path):
        pattern = r'''(?P<name>\S*?.\S)\s(?P<hash_algo>\S*)\s(?P<hash_sum>[a-f0-9]{32,})'''
        pattern = re.compile(pattern, re.DOTALL)

        with open(path, 'r') as input_file:
            for f in pattern.finditer(input_file.read()):
                yield File(
                    f.groupdict()['name'],
                    f.groupdict()['hash_algo'],
                    f.groupdict()['hash_sum']
                )


class File:
    def __init__(self, name, hash_algo, hash_sum):
        self.name = name
        self.hash_algo = hash_algo
        self.hash_sum = hash_sum


class HashSumChecker:

    def __init__(self, file, hash_algo):

        if hash_algo == 'md5':
            self.hash_sum = hashlib.md5(file).hexdigest()
        if hash_algo == 'sha1':
            self.hash_sum = hashlib.sha1(file).hexdigest()
        if hash_algo == 'sha256':
            self.hash_sum = hashlib.sha256(file).hexdigest()

    def equal_hash_sum(self, input_hash_sum) -> bool:
        return self.hash_sum == input_hash_sum


# class FilesFinder:
#     """
#     Class for ...
#     """
#
#     def __init__(self, path):
#         if not os.path.exists(path):
#             raise FileNotFoundError(f'No such file or directory: {path}')
#         self.path = path
#
#     def get_file(self):
#         for file in os.listdir(self.path):
#             if os.path.isfile(os.path.join(self.path, file)):
#                 return file


def main():
    input_file = 'input_file.txt'
    dir_to_check = 'files_to_check'
    if not FileProvider.exists_path(input_file):
        raise FileExistsError

    if not FileProvider.exists_path(dir_to_check):
        raise FileExistsError

    for file in FileProvider.parser_input_file(input_file):
        file_path = FileProvider.get_file_path(dir_to_check, file.name)
        if not FileProvider.exists_path(file_path):
            print(file.name, 'NOT FOUND')
            continue

        file_to_check = FileProvider.get_file(file_path)
        checker_hash_sum = HashSumChecker(file_to_check, file.hash_algo)
        if checker_hash_sum.equal_hash_sum(file.hash_sum):
            print(file.name, 'OK')
        else:
            print(file.name, 'FAIL')


if __name__ == '__main__':
    main()
