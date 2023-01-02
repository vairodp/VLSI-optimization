import os

DEFAULT_PATH = "dataset/instances/instances"
DATAFILES_PATH = "./datafiles"

# TODO description
def read_dimensions(file):
    width, height = [], []
    for line in file:
        try:
            w, h = map(int, line.strip().split(' '))
        except (ValueError, TypeError):
            print(f"Error reading circuit info")
            return None, None
        width.append(w)
        height.append(h)
    print(f"circuits_w: {width}")
    print(f"circuits_h: {height}")
    return width, height

# TODO description
def read_instance_data(filename):

    print(f"Reading instance file '{filename}'")

    try:
        with open(filename, 'r') as instance:
            lines = instance.readlines()
            global_width, num_circuits = map(int, [line.strip() for line in lines[:2]])
            width, height = read_dimensions(lines[2:])
            
            if width is None or height is None:
                return 
    
    except (FileNotFoundError, ValueError):
        print(f"Error reading instance file '{filename}'")
        return None
    
    return global_width, num_circuits, width, height

# TODO description
def data_prep(path=DEFAULT_PATH):

    print("porcodio", path)

    # Remove old datafiles if present
    if os.path.exists(DATAFILES_PATH):
        os.rmdir(DATAFILES_PATH)
    
    os.mkdir(DATAFILES_PATH)

    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            converted_file = DATAFILES_PATH + "/"+ filename.replace('.txt', '.dzn')
        else:
            converted_file = DATAFILES_PATH + "/"+ filename
    
        print("Converting " + filename + " to " + converted_file)

        file_prep(path + "/"+ filename, converted_file)

    print("Done")

# Read files TODO
def file_prep(filepath, filename):
    
    global_width, num_circuits, height, height = read_instance_data(filepath)
    with open(filename, 'w') as out:
        out.write(f"num_circuits={num_circuits};\n")
        out.write(f"width={global_width};\n")
        out.write(f"circuits_w={height};\n")
        out.write(f"circuits_h={height};\n")