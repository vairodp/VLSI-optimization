import os
import sys
import time
import numpy as np
from z3 import *
from itertools import combinations
from src.SATsolver import read_variables



def h_range(w_board, w, h):

    h_min = sum(w[i]*h[i] for i in range(len(w))) / w_board
    h_max = sum([h[i] for i in range(len(h))])

    return np.arange(h_min, h_max)


def model(circuits_variables):

    n_circuits = circuits_variables["tot_circuits"]
    w_board = circuits_variables["max_width"]
    w = circuits_variables["circuits_width"]
    h = circuits_variables["circuits_height"]
 
    h_board = h_range(w_board, w, h)

    x = [[Bool(f"x[{c}][{w}]") for w in range(w_board)] for c in range(n_circuits)]
    y = [[Bool(f"y[{c}][{h}]") for h in range(h_board)] for c in range(n_circuits)]


    #aux = [Bool(f"aux[{n}]") for n in range(n_circuits)]

    for h_board in fixed_heigth:

        existence_x = And([
                            Or([
                                And(
                                    And([x[c][j] for j in np.arange(w[c])+i]), 
                                    And([Not(x[c][j]) for j in list(set(np.arange(w_board))-set(np.arange(w[c])+i))])
                                    #,aux[c]
                                    ) 
                                for i in range(w_board - w[c]+1)]
                            ) 
                        for c in range(n_circuits)]
                    )
        unicity_x = And([

                    And([

                        Not(
                            And(
                                And([x[c][j] for j in np.arange(w[c]) + i]),
                                And([x[c][j] for j in np.arange(w[c]) + j])
                            )) 
                            for i,j in combinations(np.arange(w_board - w[c]), 2)
                    ])
                        
                            for c in range(n_circuits)])

        ###################################yyyyyyyyyyyyyyyyyyyyyyyy##########################################

        existence_y = And([
                            Or([
                                And(
                                    And([y[c][j] for j in np.arange(h[c])+i]), 
                                    And([Not(y[c][j]) for j in list(set(np.arange(h_board))-set(np.arange(h[c])+i))])
                                    #, aux[c]
                                    ) 
                                for i in range(h_board - h[c]+1)]
                            ) 
                        for c in range(n_circuits)]
                    )
        unicity_y = And([

                    And([

                        Not(
                            And(
                                And([y[c][j] for j in np.arange(h[c]) + i]),
                                And([y[c][j] for j in np.arange(h[c]) + j])
                            )) 
                            for i,j in combinations(np.arange(h_board - h[c]), 2)
                    ])
                        
                            for c in range(n_circuits)])

        alligment = And([
                        And([
                                Implies(
                                    And(x[c][s], x[k][s]), 
                                    Not(
                                        Or([ 
                                            And(y[c][i],y[k][i]) 
                                            for i in range(h_board)] 
                                        )
                                        )
                                    ) for c,k in combinations(np.arange(n_circuits), 2)]
                            ) for s in range(w_board)])

        solver = Solver()
        solver.add(existence_x)
        solver.add(existence_y)
        #solver.add(unicity_x)
        #solver.add(unicity_y)
        solver.add(alligment)

    return solver.check(), solver.model()

if __name__ == "__main__":
  circuits_variables = read_variables(sys.argv[1])
  model_nostro(circuits_variables)