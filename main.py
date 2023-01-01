import os
import argparse

from CP.src import solver
from utils import data_prep, DATAFILES_PATH

def main(args):
    
    path = args.path
    output = args.output
    display = args.display
    rotation = args.rotation
    model_name = args.model_name
    symmetry_breaking_constraints = args.symmetry_breaking_constraints

    model_name = "/" + model_name + ".mzn"

    # TODO better description
    data_prep(path)

    if not os.path.exists(output):
        print("Creating output directory: " + output)
        os.makedirs(output)
 
    if os.path.exists(model_name):
        print("Model found")
        for file in os.listdir(DATAFILES_PATH):
            print("Solving " + file)
            solver(file, output, rotation, model_name, symmetry_breaking_constraints)
        print("Done")
    else:
        print("Model not found")
        return

    if display:
        print("Initializing display")
        display()
        
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('display', default = False, help = 'TODO')
    parser.add_argument('rotation', default = False, help = 'TODO')
    parser.add_argument('model_name', default = 'model', help = 'TODO')
    parser.add_argument('output', default = "../output/", help = 'TODO')
    parser.add_argument('symmetry-breaking-constraints', default = False, help = 'TODO')
    parser.add_argument('path', default = "../../dataset/instances/instances/", help = 'TODO')
    
    
    args = parser.parse_args()

    main(args)