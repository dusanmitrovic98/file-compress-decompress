import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()
        compressed_data = zlib.compress(data)

    with open(output_file, 'wb') as file:
        file.write(compressed_data)

    print(f"File '{input_file}' compressed and saved as '{output_file}'.")

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as file:
