import os

# 1 minute
from utils import TIME_LIMIT

# TODO implement different solvers
def solver(file_path, output_path, rotation, model_name, symmetry_breaking_constraints):
    
    print("---> Solving " + file_path)

    cmd = "minizinc " + model_name + ' ' + file_path + " --solver Gecode -f --output-time --solver-time-limit " + str(TIME_LIMIT)
    stream = os.popen(cmd)  

    output_file = os.path.join(output_path, os.path.basename(file_path).replace(".dzn", ".txt"))

    with open(output_file, 'w') as f:
        # Write the output to the file
        f.write(stream.read())

    return output_file