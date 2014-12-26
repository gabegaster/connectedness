'''There is a function mu(k,N) := the probability that k random
numbers from 1...N have a connected graph.

strategy: given N and k pick k random numbers from 1...N and determine
if the graph is connected.

the graph on subset of the naturals, S, has edge between a,b if they
are not coprime.
'''
from itertools import izip

# gabe's
from utils import coprime

def reverse_enumerate(sequence):
    """Enumerate over a sequence in reverse order while retaining proper indexes"""
    return izip(reversed(xrange(len(sequence))), reversed(sequence))

def is_connected(S):
    '''pick random vertex, do depth-first search on graph. if find all
    vertices, stop return true. if finishes without finding all vertices
    stop return false.'''
    S = set(S)
    vertex = S.pop()
    return depth_first(vertex, S, [vertex])

def is_edge(a,b):
    return not coprime(*sorted(a,b))

def depth_first(vertex, the_rest, connected_component):
    """given a vertex, its known connected component, determine if the_rest is connected to it"""
    for b in tuple(the_rest):
        if b in the_rest and is_edge(vertex,b):
            connected_component.append(b)
            the_rest.remove(b)
            depth_first(b, the_rest, connected_component)

    if the_rest:
        return False
    else: 
        return True

def test():
    S = [14, 18, 20, 26, 3]
    assert is_connected(S)
    S = [14, 18, 20, 26, 3,142,13]
    assert is_connected(S)
    S = [14, 18, 20, 26, 3, 7]
    assert is_connected(S)
    S = [14, 18, 20, 26, 3, 7,31]
    assert not is_connected(S)
    S = [2*3,3*5,5*7,7*11,11*13,13*15,15*17,29*2,2*41,2*17*19*37]
    assert is_connected(S)
    assert is_connected(S+[17])
    assert not is_connected(S+[43])
    assert is_connected([7])
    
    import random
    D = [5*3*17, 2*3, 13*11, 2*17*19*37, 7*11, 7*5, 5*19, 41*2, 29*2, 3*5, 13*7]
    for p in xrange(10**3):
        random.shuffle(D)
        assert is_connected(D)

if __name__=="__main__":
    test()
    
