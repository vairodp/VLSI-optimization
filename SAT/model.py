import os
import sys
import time
import numpy as np
from math import ceil
from z3 import Bool, And, Or, Not, Solver, Implies
from itertools import combinations
from src.SATsolver import read_variables, convert_z3_format



def get_h_range(w_board, w, h):

    area = sum(w[i] * h[i] for i in range(len(w)))
    h_min = ceil(area / w_board )
    h_max = sum([h[i] for i in range(len(w))])

    return np.arange(h_min, h_max)


def existence(variable, span, limit, n_circuits):
    e = And([
             Or([
                And(
                    And([variable[c][j] for j in np.arange(span[c]) + i]), 
                    And([Not(variable[c][j]) for j in list(set(np.arange(limit)) - set(np.arange(span[c]) + i))])
                    ) for i in range(limit - span[c] + 1)]
                ) for c in range(n_circuits)]
            )
    return e


def unicity(variable, span, limit, n_circuits):
    u = And([
            And([
                Not(
                    And(
                        And([variable[c][j] for j in np.arange(span[c]) + i]),
                        And([variable[c][j] for j in np.arange(span[c]) + j])
                        )
                    ) for i, j in combinations(np.arange(limit - span[c]), 2)]
                ) for c in range(n_circuits)]
            )          
    return u


def impenetrability(x, y, w_board, h_board, n_circuits):
    i = And([
            And([
                Implies(
                        And(x[c][s], x[k][s]), 
                        Not(
                            Or([ 
                                And(y[c][i], y[k][i]) for i in range(h_board)] 
                                )
                            )
                        ) for c, k in combinations(np.arange(n_circuits), 2)]
                ) for s in range(w_board)]
            )
    return i


def get_first_index(solution, bool_variable, n_circuits):

    return  [[solution.eval(variable) for variable in bool_variable[c]].index(True) for c in range(n_circuits)]


def SAT_model(circuits_variables):

    n_circuits = circuits_variables["tot_circuits"]
    w_board = circuits_variables["plate_width"]
    w = circuits_variables["circuits_width"]
    h = circuits_variables["circuits_height"]
 
    h_range = get_h_range(w_board, w, h)

    for h_board in h_range:

        # print(f"h_board is:{h_board}\n")

        x = [[Bool(f"x[{c}][{w}]") for w in range(w_board)] for c in range(n_circuits)]
        y = [[Bool(f"y[{c}][{h}]") for h in range(h_board)] for c in range(n_circuits)]

        existence_x = existence(x, w, w_board, n_circuits)
        existence_y = existence(y, h, h_board, n_circuits)

        unicity_x = unicity(x, w, w_board, n_circuits)
        unicity_y = unicity(y, h, h_board, n_circuits)

        impenetrability_c= impenetrability(x, y, w_board, h_board, n_circuits)

        solver = Solver()
        solver.add(existence_x)
        solver.add(existence_y)
        #solver.add(unicity_x)
        #solver.add(unicity_y)
        solver.add(impenetrability_c)

        start = time.time()
        solved = solver.check()
        end = time.time()
        execution_time = end - start
        
        if str(solved) == 'sat':
            solution = solver.model()
            xc = get_first_index(solution, x, n_circuits)
            yc = get_first_index(solution, y, n_circuits)

            return {'h_board': h_board, 'execution_time': execution_time, 'xc': xc, 'yc': yc}

        # print(f'The problem is {str(solved)} for an h_board of {h_board}')

    return "unsat"

if __name__ == "__main__":

    circuits_variables = read_variables(sys.argv[1])

    # the following line is for debugging:
    # circuits_variables = {'tot_circuits': 4, 'plate_width': 5, 'circuits_width': [2,3,3,2], 'circuits_height':[5,6,1,2]}

    solution = SAT_model(circuits_variables)
    if solution == 'unsat':
        print('Problem is unsat')
    else:
        # if "solution" is different from "unsat", it will have the following structure: 
        # (h_board, execution_time, x coordinates of the BL corners, x coordinates of the BL corners)
        # x and y coordinates are organized in lists, with indexes refering to circuits according to the order
        # defined in w and h lists
        
        convert_z3_format(circuits_variables, solution, sys.argv[2])
        