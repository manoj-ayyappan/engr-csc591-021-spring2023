
import itertools
import csv
import numpy as np

# Defining the values for each hyperparameter
# eps_values = [round(i, 2) for i in list(np.arange(0.01, 0.3, 0.02))]
# print("------->Done1",len(eps_values))
# minpts_values = [round(i, 0) for i in list(np.arange(1, 10, 1))]
# print("------->Done2",len(minpts_values))
# sway_values = ['original', 'dbscan']
# print("------->Done3",len(sway_values))
bins_values = [round(i, 3) for i in list(np.arange(2, 15, 2))]
print("------->Done4",len(bins_values))
better_values = ['zitler', 'bdom']
print("------->Done5",len(better_values))
# file_values = ["data/auto93.csv", "data/auto2.csv", "data/china.csv","data/coc1000.csv","data/coc10000.csv","data/healthCloseIsses12mths0001-hard.csv","data/healthCloseIsses12mths0001-easy.csv","data/nasa93dem.csv","data/pom.csv","data/SSM.csv","data/SSN.csv"]
# print("------->Done6",len(file_values))
Far_values = my_list = [round(i, 3) for i in list(np.arange(0.65, 1.0, 0.04))]
print("------->Done7",len(Far_values))
min_size_values = [round(i, 3) for i in list(np.arange(0.5, 0.54, 0.05))]
print("------->Done8",len(min_size_values))
Max_values = [round(i, 3) for i in list(np.arange(100, 3000, 500))]
print("------->Done9",len(Max_values))
dist_values = [round(i, 3) for i in list(np.arange(0.5, 5, 0.5))]
print("------->Done10",len(dist_values ))
rest_values = [round(i, 0) for i in list(np.arange(2, 7, 1))]
print("------->Done11", len(rest_values))

# Generate all possible combinations of hyperparameters
# combinations = itertools.product(eps_values, minpts_values, bins_values,
#                                  sway_values, better_values,
#                                  Far_values, min_size_values, Max_values,
#                                  dist_values, rest_values)

combinations = itertools.product( bins_values, better_values,
                                 Far_values, min_size_values, Max_values,
                                 dist_values, rest_values)

print("------->Done12")

# Write the combinations to a CSV file
with open('hyperparameters.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Bins', 'better',
                     'Far', 'Min_size', 'Max', 'Dist',
                     'Rest'])
    for combination in combinations:
        writer.writerow(combination)


# # Generate all possible combinations of hyperparameters
# combinations = itertools.product(a_eps_values, A_minpts_values, b_bins_values,
#                                  t_sway_values, e_better_values, f_file_values,
#                                  F_Far_values, m_min_size_values, M_Max_values,
#                                  p_dist_values, r_rest_values)

# # Write the combinations to a CSV file
# with open('hyperparameters.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['a_eps', 'A_minpts', 'b_bins', 't_sway', 'e_better',
#                      'f_file', 'F_Far', 'm_min_size', 'M_Max', 'p_dist',
#                      'r_rest'])
#     for combination in combinations:
#         writer.writerow(combination)       
