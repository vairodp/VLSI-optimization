# VLSI Optimization Project

This repository contains the final report and Python code for a VLSI Optimization project. The project aims to efficiently pack circuits on a board to create a space-efficient chip. 

## Contents

The project includes Python code that implements three different strategies for approaching the optimization problem: constraint programming, boolean satisfiability, and mixed integer programming. The `main.py` file is the entry point for running the code and accepts command-line arguments to specify input data, output directory, display options, rotation options, approach options, model name, and symmetry breaking constraints.

The `CP` directory contains the implementation of the constraint programming approach. The `SAT` directory contains the implementation of the boolean satisfiability approach. The `MIP` directory contains the implementation of the mixed integer programming approach.

The `visualizer.py` file provides a visual representation of the optimized circuit placement on a board.

## Usage

To run the code, clone this repository and navigate to its root directory in your terminal. Then run:

```
python main.py --path <path_to_input_file> --output <path_to_output_directory> --display <True/False> --rotation <True/False> --approach <CP/SAT/MIP> --model_name <name_of_model> --symmetry_breaking_constraints <True/False>
```

For example:

```
python main.py --path data/input.txt --output results/ --display True --rotation False --approach CP --model_name model1 --symmetry_breaking_constraints True
```

This will run the optimization using constraint programming approach with symmetry breaking constraints enabled and save results in `results/` directory.

Command-line arguments:
- `-s/--symmetry-breaking-constraints`: Enable/disable symmetry breaking constraints (default: False)
- `-r/--rotation`: Enable/disable circuit rotation (default: False)
- `-d/--display`: Enable/disable display of optimized circuit placement (default: False)
- `--output`: Specify output directory path (default: "../output/")
- `--path`: Specify input file path (default: "data/input.txt")
- `--model_name`: Specify name of model used for optimization (default: "model")

## Contributions

Contributions to this repository are welcome. If you have any suggestions or improvements for the code or would like to add additional resources related to VLSI optimization, please feel free to submit a pull request.

## Authors

- Klein Tahiraj
- Vairo Di Pasquale
