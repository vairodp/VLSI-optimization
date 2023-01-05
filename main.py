import os
import shutil
import argparse

from CP.src.solver import solver
from utils import data_prep, DATAFILES_PATH, DEFAULT_PATH

def main(args):
    
    path = args.path
    output = args.output
    display = args.display
    rotation = args.rotation
    model_name = args.model_name
    symmetry_breaking_constraints = args.symmetry_breaking_constraints

    model_name = "./CP/" + model_name + ".mzn"

    # TODO better description
    data_prep(path)

    if not os.path.exists(output):
        print("Creating output directory: " + output)
        os.makedirs(output)
 
    if os.path.exists(model_name):
        print("Found model: " + model_name)
        for file in os.listdir(DATAFILES_PATH):
            solver(DATAFILES_PATH + file, output, rotation, model_name, symmetry_breaking_constraints)
        print("Done")
    else:
        print("Model not found on this path: " + model_name)
        return

    if display:
        print("Initializing display")
        display()
    
    # Clean up
    shutil.rmtree(DATAFILES_PATH)

    return


if __name__ == '__main__':

    #TODO pyramid
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--symmetry-breaking-constraints', default = False, help = 'TODO' , required = False)
    parser.add_argument('-r', '--rotation', default = False, help = 'TODO', required = False)
    parser.add_argument('-d', '--display', default = False, help = 'TODO', required = False)
    parser.add_argument('--output', default = "../output/", help = 'TODO', required = False)
    parser.add_argument('--path', default = DEFAULT_PATH, help = 'TODO', required = False)
    parser.add_argument('--model_name', default = 'model', help = 'TODO', required=False)
    
    args = parser.parse_args()

    main(args)