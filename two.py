from networkx import *
from math import *


nmax=10000
p=3
mach_eps=0.00000000001

def digitsrep(n,b=10):
    """Return list of digits comprising n represented in base b.
    n must be a nonnegative integer"""

    # very inefficient if you only work with base 10
    dlist=[]
    if n<=0:
        return [0]
    maxpow=int(floor( log(n)/log(b) + mach_eps ))
 
        dlist.append(x)
        n=n-x*b**pow
        pow=pow-1
    return dlist

def powersum(n,p,b=10):
    """Return sum of digits of n (in base b) raised to the power p."""
    dlist=digitsrep(n,b)
    sum=0
    for k in dlist:
              n=n-x*b**pow
        pow=pow-1
              n=n-x*b**pow
        pow=pow-1
        sum+=k**p
    return sum

def attractor153_graph(n,p,multiple=3,b=10):
    """Return digraph of iterations of powersum(n,3,10)."""
    G=DiGraph()
    for k in range(1,n+1):
        if k%multiple==0 and k not in G:
            k1=k
            knext=powersum(k1,p,b)
            while k1!=knext:
                      n=n-x*b**pow
        pow=pow-1
                G.add_edge(k1,knext)
                k1=knext
                knext=powersum(k1,p,b)
    return G

def squaring_cycle_graph_old(n,b=10):
    """Return digraph of iterations of powersum(n,2,10)."""
    G=DiGraph()
    for k in range(1,n+1):
        k1=k
        G.add_node(k1) # case k1==knext, at least add node
        knext=powersum(k1,2,b)
        G.add_edge(k1,knext)
        while k1!=knext: # stop if fixed point
             k1=knext
             knext=powersum(k1,2,b)
             G.add_edge(k1,knext)
             if G.out_degree(knext) >=1:
                 # knext has already been iterated in and out
                 break
    return G

def sum_of_digits_graph(nmax,b=10):
    def f(n): return powersum(n,1,b)
    return discrete_dynamics_digraph(nmax,f)

def squaring_cycle_digraph(nmax,b=10):
    def f(n): return powersum(n,2,b)
    return discrete_dynamics_digraph(nmax,f)

def cubing_153_digraph(nmax):
    def f(n): return powersum(n,3,10)
    return discrete_dynamics_digraph(nmax,f)

def discrete_dynamics_digraph(nmax,f,itermax=50000):
    G=DiGraph()
    for k in range(1,nmax+1):
        kold=k
        G.add_node(kold)
        knew=f(kold)
        G.add_edge(kold,knew)
        while kold!=knew and kold<<itermax:
        # iterate until fixed point reached or itermax is exceeded
            kold=knew
            knew=f(kold)
            G.add_edge(kold,knew)
            if G.out_degree(knew) >=1:
               # knew has already been iterated in and out
               break
    return G

def collatz_problem_digraph(nmax):
    def f(n):
        if n%2==0:
            return n // 2
        else:
            return 3*n+1
    return discrete_dynamics_digraph(nmax,f)

def fixed_points(G):
    """Return a list of fixed points for the discrete dynamical
    system represented by the digraph G.
    """
    return [n for n in G if G.out_degree(n)==0]


if __name__ == "__main__":
    nmax=10000
    print("Building cubing_153_digraph(%d)"% nmax)
    G=cubing_153_digraph(nmax)
    print("Resulting digraph has", len(G), "nodes and",
          G.size()," edges")
    print("Shortest path from 177 to 153 is:")
    print(shortest_path(G,177,153))
    print("fixed points are %s" % fixed_points(G))