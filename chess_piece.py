import string
import functools
from collections import deque
from chess_square import is_valid_square_coord


# Note: if coords are numpy vectors then we wouldn't need this function
def coord_add(coordA, coordB):
    (x1, y1) = coordA
    (x2, y2) = coordB
    return (x1 + x2, y1 + y2)


def knight_moves(origin):
    """
    Takes an origin coordinate and applies all possible knight-move vectors
    int tuple origin: the origin coordinate
    returns filter-iterable: all legal coordinates reachable by a knight
    """
    add_to_origin = functools.partial(coord_add, origin)
    vectors = [(2, 1), (2, -1), (1, 2), (1, -2),
               (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

    heads = filter(is_valid_square_coord, map(add_to_origin, vectors))

    return heads


def find_shortest_path(source, sink, moves):
    """
    Takes a source coordinate, sink coordinate, and a moves generator function
    int tuple source: the starting coordinate
    int tuple sink: the ending coordinate
    (int tuple -> int tuple iterator) moves: a function that takes as input 
        a coordinate and generates all reachable coordinates
    returns list of int tuples: returns the shortest path in the form of a coordinate list. note that this path contains the source. 
    """
    frontier = deque()
    frontier.append(source)

    # The dictionary maps coordinates to the previous node in the shortest path
    # to that coordinate, as well as the length of the shortest path
    prev_node_dict = {}
    prev_node_dict[source] = (None, 0)

    while(len(frontier) > 0):
        node = frontier.popleft()
        neighbor_dist = prev_node_dict[node][1] + 1
        for neighbor in moves(node):
            if neighbor not in prev_node_dict:
                frontier.append(neighbor)
                prev_node_dict[neighbor] = (node, neighbor_dist)
                if neighbor == sink:
                    frontier.clear()
                    break

    shortest_path = deque()
    node = sink
    while(node in prev_node_dict):
        shortest_path.appendleft(node)
        node = prev_node_dict[node][0]

    return list(shortest_path)

# REQUIRES: source != sink
def is_legal_path(source, sink, moves, path):
    if ((len(path) < 1) or source != path[0] or sink != path[-1]):
        return False
    else:
        for (origin, head) in zip(path[:-1], path[1:]):
            if head not in list(moves(origin)):
                return False
        return True
