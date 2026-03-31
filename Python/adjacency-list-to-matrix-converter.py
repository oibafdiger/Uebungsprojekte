** start of main.py **

def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for key, values in adj_list.items():
        for i in values:
          adj_matrix[key][i] = 1
        print(adj_matrix[key])
    return(adj_matrix)


adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

print(adjacency_list_to_matrix(adj_list))

** end of main.py **

