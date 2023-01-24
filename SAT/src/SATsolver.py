import os

# TODO improve this function, this is just a draft
def convert_z3_format(input, solution, output_file):
    
    print("Creating file: " + output_file)
    # Writing in the output file
    with open(output_file, 'w') as f:
        # writing on the first line of the file
        f.write(f"{input['plate_width']} {solution['h_board']}\n")
        # writing on the second line of the file
        f.write(f"{input['tot_circuits']}\n")
        # writing on the third line of the file
        for i, j, k, l in zip(input['circuits_width'], input['circuits_height'], solution['xc'], solution['yc']):
            f.write(f"{i} {j} {k} {l}\n")
        f.write(f"% time elapsed: {round(solution['execution_time'],2)} s\n")
        f.write(f"----------\n")
        f.write(f"==========\n")
        f.write(f"% time elapsed: {round(solution['execution_time'],2)} s\n")
    print("File created: " + output_file)
    return

def read_variables(file_path):
    variables = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Split the line by '=' and remove the ';' from the end
                var, value = line.strip().split('=')[0],line.strip().split('=')[1].strip(';')
                # check if value is a list 
                if '[' in value:
                    # split the values by ',' and convert them to int
                    value = list(map(int, value[1:-1].split(',')))
                elif value.isdigit():
                    value = int(value)
                # Add the variable and value to the dictionary
                variables[var] = value
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except:
        print("An error occurred.")
    return variables

# TODO use the timilimit parameter
def SATsolver(file_path, output_path, rotation, model_path, symmetry_breaking_constraints):
    
    output_file = os.path.join(output_path, os.path.basename(file_path).replace(".dzn", ".txt"))

    cmd = "python " + model_path + " " + file_path + " " + output_file
    placeholder = os.popen(cmd)
    print(placeholder.read())
    return output_file