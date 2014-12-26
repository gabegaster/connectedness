'''implements some basic number theory stuff: gcd, euler-phi function, inverts numbers modulo n.

'''
import functools

big_primes = 512927357,674506081

def find_a_factor(n):
    for i in xrange(2, n):
        if n%i == 0:
            return n/i, i
    return n, "Prime!"

def invert(a,n):
    # multiplicative inverse of a mod n
    return get_generator(a,n)[1] % n

def phi(n):
    # euler-phi function the number of 0<k<n s.t. gcd(k,n)=1
    return sum(gcd(i,n)==1
               for i in xrange(1,n))

def memoize(obj):
    cache = obj.cache = {}
    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

@memoize
def coprime(a,b):
    for i in xrange(2,min(a,b)+1):
        if not a%i and not b%i:
            return False
    return True

def divide(a,b):
    return a/b, a%b

def euclidean_alg(a,b):
    out = []
    r = 1
    while r>0:
        q,r = divide(a,b)
        out.append((a,q,b,r))
        a,b = b,r
    out.pop()
    return out

def get_generator(a,b):
    eqs = euclidean_alg(a,b)
    if not eqs:
        return 0
    greatest_cd = eqs[-1][-1]
    eq = set_eq2remainder(eqs.pop())
    while eqs:
        eq2 = eqs.pop()
        eq = resort(eq2,eq)
        # assert lin_comb(*eq)==greatest_cd
    return eq

def set_eq2remainder(eq):
    eq = list(eq)
    eq = eq[:3]
    eq.insert(1,1)
    eq[2]*=-1
    return eq

def resort((a,q,b,r),(b1,s,t,r1)):
    assert b==b1
    assert r==r1
    return a,t,(s-t*q),b

def lin_comb(a,b,c,d):
    return a*b + c*d

def gcd(*a):
    return reduce(gcd_inner, a)

def gcd_inner(a,b):
    while b!=0:
        t = b
        b = a%b
        a = t
    return a

def run_tests():
    assert lin_comb(*get_generator(173,101))==1
    assert (invert(101,173)*101)%173==1
    import random
    for _ in xrange(1000):
        a,b = random.randint(1,100),random.randint(1,100)
        if a%b==0: continue
        assert (invert(a,b)*a)%b == gcd(a,b)

if __name__=="__main__":
    run_tests()
