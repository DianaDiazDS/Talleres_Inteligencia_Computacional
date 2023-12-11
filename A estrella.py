tree = {'S': [['A', 1], ['B', 5], ['C', 8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4]],
        'C': [['S', 8], ['G', 5]],
        'D': [['A', 3]],
        'E': [['A', 7]]}



heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}


cost = {'S': 0}             # costo total por nodos visitados


def AStarSearch():
    global tree, heuristic
    closed = []             # nodos cerrados
    opened = [['S', 8]]     # nodos abiertos

    '''encontrar los nodos visitados'''
    while True:
        fn = [i[1] for i in opened]     # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # nodo actual
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == 'G':        # finalizar el cilclo si G ha sido encontrado
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})            # añadir nodos al diccionario de costos
            fn_node = cost[node] + heuristic[item[0]] + item[1]     # calcular f(n) del nodo actual
            temp = [item[0], fn_node]
            opened.append(temp)                                     # store f(n) of current node in array opened

    '''encuentra la secuencia óptima'''
    # nodo de rastreo óptimo correcto, inicializado como nodo G
    trace_node = 'G'

    # secuencia de nodos óptima
    optimal_sequence = ['G']
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]           # nodo actual
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            '''verifica si h(s) + g(s) = f(s). En caso afirmativo, añade el nodo actual a la secuencia óptima
               cambia el nodo de rastreo óptimo correcto al nodo actual'''

            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()              # reverse the optimal sequence

    return closed, optimal_sequence


if __name__ == '__main__':
    visited_nodes, optimal_nodes = AStarSearch()
    print('nodos visitados: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))