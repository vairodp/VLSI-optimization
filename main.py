import os
import shutil
import argparse

from CP.src.CPsolver import CPsolver
from SAT.src.SATsolver import SATsolver
from MIP.src.MIPsolver import MIPsolver
from visualizer import visualizer
from utils import data_prep, DATAFILES_PATH, DEFAULT_PATH


def main(args):
    
    path = args.path
    output = args.output
    display = args.display
    rotation = args.rotation
    approach = args.approach
    model_name = args.model_name
    symmetry_breaking_constraints = args.symmetry_breaking_constraints

    # Prepare Data
    data_prep(path)

    # Prepare output directory
    if not os.path.exists(output):
        print("Creating output directory: " + output)
        os.makedirs(output)


    # CP
    if approach == "CP":
        model_name = "./CP/" + model_name + ".mzn"
        if os.path.exists(model_name):
            print(" --> Found model: " + model_name)
            for file in os.listdir(DATAFILES_PATH):
                output_file = CPsolver(DATAFILES_PATH + file, output, rotation, model_name, symmetry_breaking_constraints)
                if display:
                    print(" ---> Displaying output file: " + output_file)
                    visualizer(output_file)      
            print("Done")
        else:
            print("Model for CP not found on this path: " + model_name)
            return
    
    # SAT
    elif approach == "SAT":
        model_name = "./SAT/" + model_name + ".py"

        if os.path.exists(model_name):
            print(" --> Found model: " + model_name)
            for file in os.listdir(DATAFILES_PATH):
                output_file = SATsolver(DATAFILES_PATH + file, output, rotation, model_name, symmetry_breaking_constraints)
                if display:
                    print(" ---> Displaying output file: " + output_file)
                    visualizer(output_file)      
            print("Done")
        else:
            print("Model for SAT not found on this path: " + model_name)
            return
    
    # MIP
    elif approach == "MIP":
        model_name = "./MIP/" + model_name + ".py"
        if os.path.exists(model_name):
            print(" --> Found model: " + model_name)
            for file in os.listdir(DATAFILES_PATH):
                output_file = MIPsolver(DATAFILES_PATH + file, output, rotation, model_name, symmetry_breaking_constraints)
                if display:
                    print(" ---> Displaying output file: " + output_file)
                    visualizer(output_file)
            print("Done")

        else:
            print("Model for MIP not found on this path: " + model_name)
            return

    

    # Clean up
    shutil.rmtree(DATAFILES_PATH)

if __name__ == '__main__':

    #TODO pyramid
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--symmetry-breaking-constraints', default = False, help = 'TODO' , required = False)
    parser.add_argument('-r', '--rotation', default = False, help = 'TODO', required = False)
    parser.add_argument('-d', '--display', default = False, help = 'TODO', required = False)
    parser.add_argument('--output', default = "../output/", help = 'TODO', required = False)
    parser.add_argument('--path', default = DEFAULT_PATH, help = 'TODO', required = False)
    parser.add_argument('--model_name', default = 'model', help = 'TODO', required=False)
    parser.add_argument('--approach', default = 'CP', help = 'TODO', required=False)
    
    args = parser.parse_args()

    main(args)