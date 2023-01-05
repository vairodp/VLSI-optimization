import os

# 1 minute
from utils import TIME_LIMIT

def solver(file_path, output, rotation, model_name, symmetry_breaking_constraints):
    print("Solving " + file_path + " with model + " + model_name)
    cmd = "minizinc " + model_name + ' ' + file_path + " --solver Chuffed --solver-time-limit " + str(TIME_LIMIT)

    stream = os.popen(cmd)
    output = stream.read()
    print(output)

    print("Done solving " + file_path)

    return