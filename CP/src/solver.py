import os

# 1 minute
TIME_LIMIT = 60000

def solver(file, output, rotation, model_name, symmetry_breaking_constraints):
    print("Solving " + file)
    cmd = "minizinc" + model_name + " --solver Chuffed --solver-time-limit " + str(TIME_LIMIT)

    stream = os.popen(cmd)
    output = stream.read()
    print(output)

    print("Done solving " + file)

    return