def write_file(src: str): 
    path = "./sample.py"
    with open(path, 'w') as output_file:
        output_file.write(src + "\n")
