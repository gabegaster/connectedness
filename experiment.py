import numpy as np
from itertools import combinations, imap

from timer import show_progress
from connectedness import is_connected

def brute_main():
    for N in show_progress(xrange(4,1000)):
        print N,brute(N)

def brute(N):
    return sum(is_connected(s) 
               for s in combinations(xrange(N),3))

def mu(N,k=3):
    data = [is_connected(np.random.choice(N, k, replace=False))
            for _ in xrange(10**3)]
    return np.mean(data)

def bootstrap(N,k=3):
    data = [mu(N,k) for _ in xrange(10)]
    return np.mean(data), (max(data)-min(data))/2

def boot_main():
    for N in show_progress(xrange(10,10**3)):
        print ",".join(map(str,[N]+list(bootstrap(N,k=int(N**.5)))))

if __name__=="__main__":
    boot_main()
