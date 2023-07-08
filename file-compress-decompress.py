import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as file:
