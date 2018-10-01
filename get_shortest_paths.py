
import numpy as np

def read_numbers(data_file):
    input_data_file = open(data_file, 'r')
    input_data = input_data_file.readlines()
    input_data_file.close()

    numbers = np.array([])
    for i_line in xrange(len(input_data)):
        entries = input_data[i_line].split()
        entries = filter(None, entries) # remove empty entries
        line_numbers = [ float(x) if x.lower != "inf" else float("inf") for x in entries ]
        numbers = np.append(numbers, line_numbers)
    return numbers

def read_data(data_file):
    numbers = read_numbers(data_file)
    cur_entry = 0

    # number of nodes
    n = int(numbers[cur_entry])
    cur_entry += 1

    # init graph
    neighbors = [None] * n
    weights = [None] * n

    # construct the graph
    for i_node in xrange(n):
        num_neighbors = int(numbers[cur_entry])
        cur_entry += 1
        cur_neighbors = np.zeros(num_neighbors, dtype = 'int32')
        cur_weights = np.zeros(num_neighbors, dtype = 'float')
        for i_neighbor in xrange(num_neighbors):
            cur_neighbors[i_neighbor] = int(numbers[cur_entry])
            cur_entry += 1
            cur_weights[i_neighbor] = numbers[cur_entry]
            cur_entry += 1
        neighbors[i_node] = cur_neighbors
        weights[i_node] = cur_weights

    # get pairs of nodes to compute distances
    num_pairs_of_interest = int(numbers[cur_entry])
    cur_entry += 1

    node_pairs = np.zeros( (num_pairs_of_interest, 2), dtype = 'int32' )
    for i_pair in xrange(num_pairs_of_interest):
        node_pairs[i_pair][0] = int(numbers[cur_entry])
        cur_entry += 1
        node_pairs[i_pair][1] = int(numbers[cur_entry])
        cur_entry += 1

    return neighbors, weights, node_pairs

def make_dummy_solution(neighbors, weights, node_pairs):
    num_pairs = len(node_pairs)
    answer=np.empty(num_pairs)
    answer.fill(float('inf'))
    return answer

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        neighbors, weights, node_pairs = read_data(file_location)

        answer = make_dummy_solution(neighbors, weights, node_pairs)
        print '\n'.join(map(str, answer))
    else:
        print 'This script requires an input file as command line argument.'
