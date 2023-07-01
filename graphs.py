V = { 1, 2, 3, 4 }
E = { (1,2), (2,1), (1,3), (3,1), (2,3), (3,2), (1,4), (4,1)}
E_directed = { (1,2), (1,3), (2,3), (3,4) }

# ███    ██ ███████ ██  ██████  ██   ██ ██████   ██████  ██    ██ ██████  ██   ██  ██████   ██████  ██████  ███████
# ████   ██ ██      ██ ██       ██   ██ ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██    ██ ██    ██ ██   ██ ██
# ██ ██  ██ █████   ██ ██   ███ ███████ ██████  ██    ██ ██    ██ ██████  ███████ ██    ██ ██    ██ ██   ██ ███████
# ██  ██ ██ ██      ██ ██    ██ ██   ██ ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██    ██ ██    ██ ██   ██      ██
# ██   ████ ███████ ██  ██████  ██   ██ ██████   ██████   ██████  ██   ██ ██   ██  ██████   ██████  ██████  ███████

print("Vertices")
print(V)
print("Edges, undirected")
print(E)
print("Edges, directed")
print(E_directed)


################
# Directed versions

# vertices connected by an edge from u.
def N_out(V, E, u):
    return { v for v in V if (u,v) in E }

# vertices connected by an edge from S.
def NS_out(V, E, S):
    return { v for v in V for u in S if (u,v) in E }

# vertices connected by an edge to u
def N_in(V, E, u):
   return { v for v in V if (v,u) in E }

# vertices connected by an edge to S
def NS_in(V, E, S):
    return { v for v in V for u in S if (v,u) in E }

############
# Undirected versions
# edges are symmetric, so arbitrarily using the out version of above.
def N(V, E, u):
   return N_out(V, E, u)

# Neighbourhood of a set of vertices
def NS(V, E, S):
    return NS_out(V, E, S)

print()
print('Neighbourhood of 1, undirected')
print(N(V, E, 1))
print('Neighbourhood of {1}, undirected')
print(NS(V, E, { 1 }))

# get a single element of a set. Don't care which
def arbitraryElement(S):
    return next(iter(S))


# ██████  ██ ███████ ████████  █████  ███    ██  ██████ ███████      ██████ ██       █████  ███████ ███████ ███████ ███████
# ██   ██ ██ ██         ██    ██   ██ ████   ██ ██      ██          ██      ██      ██   ██ ██      ██      ██      ██
# ██   ██ ██ ███████    ██    ███████ ██ ██  ██ ██      █████       ██      ██      ███████ ███████ ███████ █████   ███████
# ██   ██ ██      ██    ██    ██   ██ ██  ██ ██ ██      ██          ██      ██      ██   ██      ██      ██ ██           ██
# ██████  ██ ███████    ██    ██   ██ ██   ████  ██████ ███████      ██████ ███████ ██   ██ ███████ ███████ ███████ ███████

# this code works for directed or undirected graphs.  For directed graphs, paths follow same direction as edges (i.e. starting at out edges from starting point)
def distanceClasses(V, E, u):
    V0 = V              # V_0 = V
    D = [ {u} ]         # D[0] = D_0 = {u}
    return distanceClassesR(V0, E, D)

def distanceClassesR(V, E, D):
    Vnew = V - D[-1]            # V_{j} = V_{j-1} / D_{j-1}
    if len(Vnew) == 0: return D # Already considered all elements?
    Dnew = D + [ NS_out(Vnew, E, D[-1]) ]  # D_{j} = N_{V_j}(D_{j-1})
    return distanceClassesR(Vnew, E, Dnew)

print()
print('Distance classes from 4, undirected')
print(distanceClasses(V, E, 4))

def distanceClassesP(V, E, u):
    V0 = V              # V_0 = V
    D = [ {u} ]         # D[0] = D_0 = {u}
    parent = { u: False }
    return distanceClassesPR(V0, E, D, parent)

def distanceClassesPR(V, E, D, parent):
    Vnew = V - D[-1]                          # V_{j} = V_{j-1} / D_{j-1}
    if len(Vnew) == 0: return D, parent       # All done?
    Dnew = D + [ NS_out(Vnew, E, D[-1]) ]     # D_{j} = N_{V_j}(D_{j-1})
    if len(Dnew[-1]) == 0: return D, parent   # No more neighbours, graph is disconnected
    for v in Dnew[-1]:
      parent[v] = arbitraryElement(N_in(D[-1], E, v))
    return distanceClassesPR(Vnew, E, Dnew, parent)

print()
print('Distance classes from 4, undirected, with edges in spanning tree')
print(distanceClassesP(V, E, 4))
print()
print('Distance classes from 1, directed, with edges in spanning tree')
print(distanceClassesP(V, E_directed, 1))


# ██████  ███████ ███████
# ██   ██ ██      ██
# ██████  █████   ███████
# ██   ██ ██           ██
# ██████  ██      ███████

def breadthFirst(V, E, u):
    print('processing ', u)            # Process vertex u
    V0 = V              # V_0 = V
    D = {u}             # D[0] = D_0 = {u}
    return breadthFirstR(V0, E, D)

def breadthFirstR(V, E, D):
    Vnew = V - D                 # V_{j} = V_{j-1} / D_{j-1}
    if len(Vnew) == 0: return    # Already considered all elements?
    Dnew = NS_in(Vnew, E, D)     # D_{j} = N_{V_j}(D_{j-1})
    for u in Dnew:
        print('processing ', u)              # Process vertex u
    return breadthFirstR(Vnew, E, Dnew)

print()
print('BFS from 4')
print(breadthFirst(V, E, 4 ))


# ██████  ███████ ███████
# ██   ██ ██      ██
# ██   ██ █████   ███████
# ██   ██ ██           ██
# ██████  ██      ███████

def depthFirst(V, E, u):
    T = {u}             # set of vertices already seen
    depthFirstR(V, E, u, T)

def depthFirstR(V, E, u, T):
    print('processing ', u)                # process vertex u
    if len(T) == len(V): return T # already seen all?
    Nu = N(V, E, u) - T     # Neighbours not already seen
    T.update(Nu)            # Update set of vertices seen
    for v in Nu:
        T.update(depthFirstR(V, E, v, T))  # update vertices seen in branch
    return T


print()
print('DFS from 4')
print(depthFirst(V, E, 4))


# ██████  ██ ██████   █████  ██████  ████████ ██ ████████ ███████
# ██   ██ ██ ██   ██ ██   ██ ██   ██    ██    ██    ██    ██
# ██████  ██ ██████  ███████ ██████     ██    ██    ██    █████
# ██   ██ ██ ██      ██   ██ ██   ██    ██    ██    ██    ██
# ██████  ██ ██      ██   ██ ██   ██    ██    ██    ██    ███████

def forall(S, p):
    falseX = { 1 for x in S if not p(x) }
    if len(falseX) > 0:
        return False
    return True

def isBipartite(V,E):
   u = arbitraryElement(V)
   D = distanceClasses(V, E, u)
   return forall(D, lambda S : S.isdisjoint(NS(V, E, S)))

print()
print('find bipartition, undirected')
print(isBipartite(V,E))
E2 = { (1,2), (2,1), (1,3), (3,1), (2,4), (4,2)}
print('new undirected edge set:', E2)
print('find bipartition, new edge set')
print(isBipartite(V,E2))

# ████████  ██████  ██████       ██████  ██████  ██████  ███████ ██████  ██ ███    ██  ██████  ███████
#    ██    ██    ██ ██   ██     ██    ██ ██   ██ ██   ██ ██      ██   ██ ██ ████   ██ ██       ██
#    ██    ██    ██ ██████      ██    ██ ██████  ██   ██ █████   ██████  ██ ██ ██  ██ ██   ███ ███████
#    ██    ██    ██ ██          ██    ██ ██   ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██    ██      ██
#    ██     ██████  ██           ██████  ██   ██ ██████  ███████ ██   ██ ██ ██   ████  ██████  ███████

#Khan's algorithm

V2 = {1,2,3,4,5}
E3 = { (1,2), (2,3), (5,3), (1,4), (5,4)}

def hasInEdge(V, E, v):
    return len(N_in(V, E, v)) != 0

def topOrdering(V, E):
    return topOrderingR(E, set(), V, [])    # G0 = {}, V0 = V

def topOrderingR(E, G, V, ordering):
    Gnew = { v for v in V if not hasInEdge(V, E, v) }
    if len(Gnew) == 0: return False         # there must be a cycle
    ordering = ordering + [ u for u in Gnew ]
    Vnew = V - Gnew
    if len(Vnew) == 0: return ordering      # no more vertices
    return topOrderingR(E, Gnew, Vnew, ordering)

print()
print('new vertices: ', V2)
print('new edges, directed: ', E3)
print('Topological ordering')
print(topOrdering(V2, E3))
