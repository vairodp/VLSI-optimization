import os
import shutil

DATAFILES_PATH = "datafiles/"
DEFAULT_PATH = "dataset/instances/instances"

# 5 minutes
TIME_LIMIT = 300000


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
    return width, height

# TODO description
def read_instance_data(filename):
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

    # Remove old datafiles if present
    if os.path.exists(DATAFILES_PATH):
        shutil.rmtree(DATAFILES_PATH)

    os.mkdir(DATAFILES_PATH)

    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            converted_file = DATAFILES_PATH + "/"+ filename.replace('.txt', '.dzn')
        else:
            converted_file = DATAFILES_PATH + "/"+ filename
    
        print("Converted " + filename + " to " + converted_file)

        file_prep(path + "/"+ filename, converted_file)

# Read files TODO
def file_prep(filepath, filename):
    
    plate_width, tot_circuits, circuits_width, circuits_height = read_instance_data(filepath)
    with open(filename, 'w') as out:
        out.write(f"tot_circuits={tot_circuits};\n")
        out.write(f"plate_width={plate_width};\n")
        out.write(f"circuits_width={circuits_width};\n")
        out.write(f"circuits_height={circuits_height};\n")