include "globals.mzn";

% DEFINING THE PROBLEM

% defining problem input values
int: tot_circuits;
int: plate_width;

array[1..tot_circuits] of int: circuits_width;
array[1..tot_circuits] of int: circuits_height;

% defining smallest possible area occupied by the circuits as the sum of theirs areas. 
int: area_min = sum( i in 1..tot_circuits)(circuits_width[i] * circuits_height[i]);

% defining the idel minimum value for the height, not taking into account circuits shapes. Value rounded to ceil. 
int: intrinsic_h_min = ceil(area_min/plate_width);

% defining the minimum possible area as the biggest between the idea area and the largest circuit area
int: h_min = max(max(circuits_height), intrinsic_h_min);

% defining the top limit of the height as the sum of all circuits heights
int: h_max = sum(circuits_height);

% defining a variable for the height of the board, spanning in appropriatelly defined domain
var h_min..h_max : height;

% selecting the smallest possible values of width and height to be used to limit the domain of the possible coordinates
int: circuits_width_min = min(circuits_width);
int: circuits_height_min = min(circuits_height);

% defining an array of variable for the x and y coordinates of the bottom left corner of each circuit, spanning
% an appropriately limited domain;
array[1..tot_circuits] of var 0.. plate_width - circuits_width_min: x;
array[1..tot_circuits] of var 0..h_max - circuits_height_min: y;

% defining an array of indexes representing the circuits from the biggest to the smallest in terms of area;
array[1..tot_circuits] of int: decreasing_area = arg_sort(i in 1..tot_circuits)(-circuits_width[i] * circuits_height[i]);
array[1..tot_circuits] of int: decreasing_dimension = arg_sort(i in 1..tot_circuits)(-max(circuits_width[i], circuits_height[i]));

% setting the largest possible dimension to be used in the rotation case
int: max_dimension = max(max(circuits_height), max(circuits_width));
int: min_dimension = min(circuits_width_min, circuits_height_min);
% setting an array of boolean variables to specify if a circuit is rotated
array[1..tot_circuits] of var bool: rotation;

% defining two vectors of variables to hold new values for height and width in the case of a rotated circuit
array[1..tot_circuits] of var min_dimension..max_dimension: rotation_widths = [if rotation[i] then circuits_height[i] 
                                                                   else circuits_width[i] 
                                                                   endif | i in 1..tot_circuits];

array[1..tot_circuits] of var min_dimension..max_dimension: rotation_heights = [if rotation[i] then circuits_width[i] 
                                                                    else circuits_height[i] 
                                                                    endif | i in 1..tot_circuits];


% SETTING THE CONSTRAINTS

% constaining each circuit to be always inside the board, both in widht and height

constraint forall(i in 1..tot_circuits)(x[i] + rotation_widths[i] <= plate_width /\ y[i] + rotation_heights[i] <= height);

% ensuring that circuits do not overlap
constraint diffn(x, y, rotation_widths, rotation_heights);

% efficiently spreading circuits over the available space
constraint cumulative(x, rotation_widths, rotation_heights, height);
constraint cumulative(y, rotation_heights, rotation_widths, plate_width);

% breaking a first simmetry by ensuring that the biggest circuit is always placed on the origin of the board
constraint symmetry_breaking_constraint(x[decreasing_area[1]] == 0 
                                        /\ y[decreasing_area[1]] == 0);

% breaking the simmetry given by the reflection along the y = x axis
constraint symmetry_breaking_constraint(
                                        forall(i, j in 1..tot_circuits 
                                               where i < j 
                                                     /\ rotation_widths[i] = rotation_heights[j] 
                                                     /\ rotation_heights[i] = rotation_widths[j] 
                                                     /\ x[i] = y[j] 
                                                     /\ y[i] = x[j] )
                                         (lex_less([x[i],y[i]],[x[j],y[j]])));
                                        
% ensuring that for pieces with same dimensions a strict and univoque order is followed, in order to further brake simmetries 
% for pieces placed nearby                                     
constraint symmetry_breaking_constraint(
                                        forall(i, j in 1..tot_circuits 
                                               where i < j 
                                                     /\ rotation_widths[i] = rotation_widths[j] 
                                                     /\ rotation_heights[i] = rotation_heights[j] ) 
                                         (lex_less([x[i],y[i]],[x[j],y[j]]))); 

% ensuring that squared circuits don't get rotated to avoid further simmetric solutions under rotation
constraint symmetry_breaking_constraint(
                                        forall(i in 1..tot_circuits 
                                               where rotation_widths[i] == rotation_heights[i])
                                        (rotation[i] == false));

% specifying an heuristic to be followed during search
ann: s_ioA_idM = seq_search([int_search([height], smallest, indomain_min),
                              int_search([x[i] | i in decreasing_area], input_order, indomain_min, complete),
                              int_search([y[i] | i in decreasing_area], input_order, indomain_min, complete)]);

ann: s_ioD_idM = seq_search([int_search([height], smallest, indomain_min),
                              int_search([x[i] | i in decreasing_dimension], input_order, indomain_min, complete),
                              int_search([y[i] | i in decreasing_dimension], input_order, indomain_min, complete)]);

ann: s_ioD_idR_luby = seq_search([int_search([height], smallest, indomain_min),
                              int_search([x[i] | i in decreasing_dimension], input_order, indomain_random, complete),
                              int_search([y[i] | i in decreasing_dimension], input_order, indomain_random, complete),
                              restart_luby(10)]);

ann: s_ioA_idR_luby = seq_search([int_search([height], smallest, indomain_min),
                              int_search([x[i] | i in decreasing_area], input_order, indomain_random, complete),
                              int_search([y[i] | i in decreasing_area], input_order, indomain_random, complete),
                              restart_luby(10)]);

ann: s_ff_idR_luby = seq_search([int_search([height], smallest, indomain_min),
                              int_search(x, first_fail, indomain_random, complete),
                              int_search(y, first_fail, indomain_random, complete),
                              restart_luby(10)]);

% chosing height as our objective function to be minimized
% here use just the best configuration of the normal model for testing:

solve :: s_ioA_idM minimize height; 

% formatting the output accordingly to the assigments specifications
output ["\(plate_width) \(height)\n" ++ "\(tot_circuits)\n" ++ concat(i in 1..tot_circuits)("\(rotation_widths[i]) \(rotation_heights[i]) \(x[i]) \(y[i])\n")];