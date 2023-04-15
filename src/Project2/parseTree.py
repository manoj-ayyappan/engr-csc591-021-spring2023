def parse_tree(tree, hyperparams_list):
    for node in tree:
        if '{' in node:
            hyperparams = node.split(", ")
            input_str = node
            # find the index of the '}'
            end_index = input_str.find('}') + 1
            # get the substring that starts after '}'
            substring = input_str[end_index:]
            # split the substring by comma
            lst = substring.split(',')
            # get the first number
            firstnum = int(lst[0])
            # get the last number
            lastnum = float(lst[-2])
            hyperparams_list.append([int(firstnum), hyperparams[1], float(hyperparams[2]), float(hyperparams[3]), int(hyperparams[4]), float(hyperparams[5]), float(lastnum)])
        
def main():
    input_file = "src/Project2/input.txt"
    output_file = "src/Project2/output.txt"
    hyperparams_list = []

    with open(input_file, "r") as f:
        tree = f.readlines()

    parse_tree(tree, hyperparams_list)

    with open(output_file, "w") as f:
        for hyperparams in hyperparams_list:
            f.write(str(hyperparams) + ",\n")

if __name__ == "__main__":
    main()
