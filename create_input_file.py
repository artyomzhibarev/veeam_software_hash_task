"""
Just to create a text input file
"""

import hashlib
import os
import random

path_to_files = os.path.join(os.getcwd(), 'files_to_check')
files = [file for file in os.listdir(path_to_files) if os.path.isfile(os.path.join(path_to_files, file))]

for file in files:
    with open(os.path.join(path_to_files, file), 'rb') as bf:
        binary_file = bf.read()
        algorithms = (hashlib.sha256, hashlib.sha1, hashlib.md5)
        algorithm = random.choice(algorithms)
        hash_sum = algorithm(binary_file).hexdigest()
        with open('input_file.txt', 'a') as input_file:
            input_file.write(file + ' ' + algorithm().name + ' ' + hash_sum + '\n')
