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
        compressed_data = file.read()
        decompressed_data = zlib.decompress(compressed_data)

    with open(output_file, 'wb') as file:
        file.write(decompressed_data)

    print(f"File '{input_file}' decompressed and saved as '{output_file}'.")

# Example usage
input_file = "example.txt"  # Path to the input file to compress and decompress
compressed_file = "compressed_file.bin"  # Path to save the compressed file
decompressed_file = "decompressed_file.txt"  # Path to save the decompressed file

# Compress the file
compress_file(input_file, compressed_file)
