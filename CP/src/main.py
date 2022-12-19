import os
import argparse

from vlsi import solver

def main(args):
    
    path = args.path
    output = args.output
    display = args.display
    rotation = args.rotation
    model_name = args.model_name
    symmetry_breaking_constraints = args.symmetry_breaking_constraints

    model_name = "./" + model_name + ".mzn"

    if not os.path.exists(output):
        print("Creating output directory: " + output)
        os.makedirs(output)
 
    if os.path.exists(model_name):
        print("Model found")
        solver(path, output, rotation, model_name, symmetry_breaking_constraints)

    else:
        print("Model not found")
        return
    
    if display:
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

