def read_file():
    output_string = ''
    with open("requirements.txt", "r") as f:
        for line in f:
            output_string += line + '</br>'
    return output_string
