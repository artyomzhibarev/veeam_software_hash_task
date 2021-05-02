import hashlib
import re
import os
import argparse


class FileProvider:

    @staticmethod
    def is_exists_path(path) -> bool:
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
        hash_algorithm = {
            'md5': hashlib.md5(file).hexdigest(),
            'sha1': hashlib.sha1(file).hexdigest(),
            'sha256': hashlib.sha256(file).hexdigest(),
        }
        self.hash_sum = hash_algorithm[hash_algo]

    def equal_hash_sum(self, input_hash_sum) -> bool:
        """
        Compares the hash sums of the files
        :param input_hash_sum: Hash sum of file from input file
        :return:
        """
        return self.hash_sum == input_hash_sum


class ArgsParser:

    @classmethod
    def create_parser(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument('path_file',
                            help='provide path to the input file',
                            type=str)
        parser.add_argument('path_dir',
                            help='provide path to the directory containing the files to check',
                            type=str)
        return parser


def main():
    parser = ArgsParser.create_parser()
    args = parser.parse_args()

    input_file = args.path_file
    dir_to_check = args.path_dir

    if not FileProvider.is_exists_path(input_file):
        raise FileNotFoundError('No such file or directory')

    if not FileProvider.is_exists_path(dir_to_check):
        raise FileNotFoundError('No such file or directory')

    for file in FileProvider.parser_input_file(input_file):
        file_path = FileProvider.get_file_path(dir_to_check, file.name)
        if not FileProvider.is_exists_path(file_path):
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
