import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def process_solution(solution):
    lines = solution.strip().splitlines()
    p_width, p_height = map(int, lines[0].split())
    num_circuits = int(lines[1].split()[0])
    solution = {
        'plate_width': p_width,
        'plate_height': p_height,
        'num_circuits': num_circuits,
        'circuits_width': [],
        'circuits_height': [],
        'circuits_x': [],
        'circuits_y': []
    }
    for w, h, x, y in (map(int, line.split()) for line in lines[2:num_circuits+2]):
        solution['circuits_width'].append(w)
        solution['circuits_height'].append(h)
        solution['circuits_x'].append(x)
        solution['circuits_y'].append(y)
    return solution

def read_output(filename):
      with open(filename, 'r') as f:
        solutions = f.read().split("----------")
        best_sol = solutions[-2]
        elapsed_time = best_sol.splitlines()[-1].split(" ")[-2]
        optimal = True if (solutions[-1] == '\n' or solutions[-1].splitlines()[1].strip() == '==========') else False
    
        return {**process_solution(best_sol), "optimal": optimal, "time": elapsed_time}

# Draw the image solution TODO
def visualizer(file_name):
    
    solution = read_output(file_name)

    _, ax = plt.subplots()
    ax.set(xlim=(0, solution['plate_width']), ylim=(0, solution['plate_height']))
    ax.set_aspect('equal')
    
    ticks_x = np.arange(0, solution['plate_width']+1, 1)
    ticks_y = np.arange(0, solution['plate_height']+1, 1)
    
    ax.set_xticks(ticks_x)
    ax.set_yticks(ticks_y)

    ax.grid(color='black', linewidth=0.1, linestyle='--')
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    
    circuits_w, circuits_h, circuits_x, circuits_y = solution['circuits_width'], solution['circuits_height'], solution['circuits_x'], solution['circuits_y']
    colors = plt.cm.get_cmap(name='Pastel1', lut=solution['num_circuits']+1)
    indexes = [i/solution['num_circuits'] for i in range(solution['num_circuits'])]
    
    for w, h, x, y, i in zip(circuits_w, circuits_h, circuits_x, circuits_y, indexes):
        circuit = Rectangle((x,y), w, h, facecolor=colors(i), edgecolor='black', linestyle='solid', linewidth=0.5)
        ax.add_patch(circuit)
    
    plt.subplots_adjust(left=0.3)

    ax.text(-0.5*solution['plate_width'], solution['plate_height'] - 0.5,"Optimal solution" if solution['optimal'] else "Not optimal solution" , fontsize=12, ha='left')
    ax.text(-0.5*solution['plate_width'], solution['plate_height'] - 1, f"Found in {solution['time']}s", fontsize=12, ha='left')
    ax.text(-0.5*solution['plate_width'], solution['plate_height'] - 1.5, f"Num circuits: {solution['num_circuits']}", fontsize=12, ha='left')
    ax.text(-0.5*solution['plate_width'], solution['plate_height'] - 2, f"Width: {solution['plate_width']}", fontsize=12, ha='left')
    ax.text(-0.5*solution['plate_width'], solution['plate_height'] - 2.5, f"Height: {solution['plate_height']}", fontsize=12, ha='left')
    
    ax.set_title("File: " + file_name, y=-0.1)
    
    plt.show()