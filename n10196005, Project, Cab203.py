#!/usr/bin/env python3

#############
###DETAILS###
#############

#Student number: n10196005
#Student name: Dane Mckillop
#Lecturer: Matthew McKague
#Topic: 2x2 Rubik's cube.
#Description: solution(s): Takes initial cube state s. C set of completed states declared.
#             breadthFirst(u,C): Declares int j and sets S,D. Initial state is printed.
#             breadthFirstR(j,S,D,C): Recursively calls itself to solve the cube.
#                       Check if j exceeds 14 moves, otherwise increment.
#                       Set Dnew initialized from return of permute(D) difference S.
#                       If intersection of Dnew and C is not empty, cube solved. Return j.
#                       Otherwise, declare Snew as union between S and Dnew. breadthFirstR(jnew, Snew, Dnew, C)
#             permute(V): Permutes a set V of cube states u to a set P of the six permutations of each u one turn away.
#                       Each turn conducted by: U_clock(u), U_count(u), R_clock(u), R_count(u), F_clock(u), F_count(u).

#Example initial state of the cube to be searched from. Distance 0.
#Map of faces and cube state under Turn Functions
s = (('y','w','r','g'), #face 0
    ('b','r','y','r'),  #face 1
    ('r','w','o','w'),  #face 2
    ('o','y','g','y'),  #face 3
    ('b','o','b','b'),  #face 4
    ('g','g','o','w')   #face 5
)

####################
###Cube state map###
     ####
     #F2#
     ####
#### #### #### ####
#F0# #F1# #F4# #F5#
#### #### #### ####
     ####
     #F3#
     ####

###################
###Face elements###
    #####
    #0 1#
    #2 3#
    #####

#Completed states of cube, 24 permutations of completion.
#Declared in program, here as a reference.
#Tedious, however permuting elements of D from tuples to sets in-process slows the program significantly.
#Additionally, defining set C allows us to check D by intersection.
#C = {(('r','r','r','r'),('b','b','b','b'),('w','w','w','w'),('y','y','y','y'),('o','o','o','o'),('g','g','g','g')), 
#    (('b','b','b','b'),('o','o','o','o'),('w','w','w','w'),('y','y','y','y'),('g','g','g','g'),('r','r','r','r')),
#    (('o','o','o','o'),('g','g','g','g'),('w','w','w','w'),('y','y','y','y'),('r','r','r','r'),('b','b','b','b')),
#    (('g','g','g','g'),('r','r','r','r'),('w','w','w','w'),('y','y','y','y'),('b','b','b','b'),('o','o','o','o')), #4
#    (('b','b','b','b'),('w','w','w','w'),('r','r','r','r'),('o','o','o','o'),('g','g','g','g'),('y','y','y','y')),
#    (('w','w','w','w'),('g','g','g','g'),('r','r','r','r'),('o','o','o','o'),('y','y','y','y'),('b','b','b','b')),
#    (('g','g','g','g'),('y','y','y','y'),('r','r','r','r'),('o','o','o','o'),('b','b','b','b'),('w','w','w','w')),
#    (('y','y','y','y'),('b','b','b','b'),('r','r','r','r'),('o','o','o','o'),('w','w','w','w'),('g','g','g','g')), #8
#    (('w','w','w','w'),('r','r','r','r'),('b','b','b','b'),('g','g','g','g'),('y','y','y','y'),('o','o','o','o')),
#    (('r','r','r','r'),('y','y','y','y'),('b','b','b','b'),('g','g','g','g'),('o','o','o','o'),('w','w','w','w')),
#    (('y','y','y','y'),('o','o','o','o'),('b','b','b','b'),('g','g','g','g'),('w','w','w','w'),('r','r','r','r')),
#    (('o','o','o','o'),('w','w','w','w'),('b','b','b','b'),('g','g','g','g'),('r','r','r','r'),('y','y','y','y')), #12
#    (('b','b','b','b'),('r','r','r','r'),('y','y','y','y'),('w','w','w','w'),('g','g','g','g'),('o','o','o','o')),
#    (('r','r','r','r'),('g','g','g','g'),('y','y','y','y'),('w','w','w','w'),('o','o','o','o'),('b','b','b','b')),
#    (('g','g','g','g'),('o','o','o','o'),('y','y','y','y'),('w','w','w','w'),('b','b','b','b'),('r','r','r','r')),
#    (('o','o','o','o'),('b','b','b','b'),('y','y','y','y'),('w','w','w','w'),('r','r','r','r'),('g','g','g','g')), #16
#    (('w','w','w','w'),('b','b','b','b'),('o','o','o','o'),('r','r','r','r'),('y','y','y','y'),('g','g','g','g')),
#    (('b','b','b','b'),('y','y','y','y'),('o','o','o','o'),('r','r','r','r'),('g','g','g','g'),('w','w','w','w')),
#    (('y','y','y','y'),('g','g','g','g'),('o','o','o','o'),('r','r','r','r'),('w','w','w','w'),('b','b','b','b')),
#    (('g','g','g','g'),('w','w','w','w'),('o','o','o','o'),('r','r','r','r'),('b','b','b','b'),('y','y','y','y')), #20
#    (('r','r','r','r'),('w','w','w','w'),('g','g','g','g'),('b','b','b','b'),('o','o','o','o'),('y','y','y','y')),
#    (('w','w','w','w'),('o','o','o','o'),('g','g','g','g'),('b','b','b','b'),('y','y','y','y'),('r','r','r','r')),
#    (('o','o','o','o'),('y','y','y','y'),('g','g','g','g'),('b','b','b','b'),('r','r','r','r'),('w','w','w','w')),
#    (('y','y','y','y'),('r','r','r','r'),('g','g','g','g'),('b','b','b','b'),('w','w','w','w'),('o','o','o','o'))  #24
#}


#######################
###LECTURE FUNCTIONS###
#######################

#Author: Matthew McKague and CAB203 faculty
#Referenced: 'graphs.py'
#Modified: Dane Mckillop

#Traverses the graph in order of distance from s
#Input: u, vertex of interest. C, set of completed vertices.
#Note: Modified to accept sets C, and initialize sets to expand from vertex u.
#      Functionally between the distanceClass and breadthFirst functions in graphs.py
#      Initially, D = S so we could breadthFirstR(j,S,S,C), but this lacks clarity.
def breadthFirst(u, C):
    print("Initial state: ", u)
    j = 0               # Distance is 0, root.
    S = {u}             # S[0] = {u}.
    D = {u}             # D[0] = {u}. 
    return breadthFirstR(j, S, D, C)

#Recursively expand sets S and D while comparing with set C.
#Input: j, distance from s. S, set of vertices at least j from s. D, set of vertices j from s.
#       C, set of completed states.
#Output: j, distance from s.
#Note: Modified to expand sets as we traverse the graph.
#      Exit condition redefined as intersection between Dnew and C.
#      Error condition if distance exceeds 14.
def breadthFirstR(j, S, D, C):
    if j >= 14: return -1           # 14 moves exceeded, error occured. -1 returned for error.
    jnew = j+1                      # Increment j, keep track of current move count.
    Dnew = permute(D) - S           # Set of new permutations, not currently visited.              
    if len(Dnew.intersection(C))!=0:
        print("Solved state: ",Dnew.intersection(C).pop()) #Print a solved state from the intersection of Dnew and C.
        return jnew                 # Match found, return distance j.
    Snew = S | Dnew                 # Add new permutations to visited set. 
    return breadthFirstR(jnew, Snew, Dnew, C)


####################
###TURN FUNCTIONS###
####################

#Author: Dane Mckillop

#TURN DIRECTION#
#PLEASE REFER TO STATE AND FACE MAPS AT TOP OF FILE.
# a->b : face 'a' passes elements to face 'b'.
# @a : elements of face 'a' rotate.
# !a : no change to face 'a'.

#UPPER CLOCKWISE, U
#Input: u, vertex of interest.
#Output: v, U permutation of u.
#F5->F4->F1->F0->F5#,#@F2#,#!F3#
def U_clock(u):
    v = ((u[1][0],u[1][1],u[0][2],u[0][3]),  #face 0: Top 2 squares shift clockwise.
	    (u[4][0],u[4][1],u[1][2],u[1][3]),   #face 1: Top 2 squares shift clockwise.
 	    (u[2][2],u[2][0],u[2][3],u[2][1]),   #face 2: 90* ROTATION, clockwise.
	    (u[3][0],u[3][1],u[3][2],u[3][3]),   #face 3: No change.
	    (u[5][0],u[5][1],u[4][2],u[4][3]),   #face 4: Top 2 squares shift clockwise.
	    (u[0][0],u[0][1],u[5][2],u[5][3])    #face 5: Top 2 squares shift clockwise.
    )
    return v

#UPPER COUNTER-CLOCKWISE, U'
#Input: u, vertex of interest.
#Output: v, U' permutation of u.
#F5->F0->F1->F4->F5#,#@F2#,#!F3#
def U_count(u):
    v = ((u[5][0],u[5][1],u[0][2],u[0][3]),    #face 0: Top 2 squares shift counter-clockwise.
        (u[0][0],u[0][1],u[1][2],u[1][3]),     #face 1: Top 2 squares shift counter-clockwise.
        (u[2][1],u[2][3],u[2][0],u[2][2]),     #face 2: 90* ROTATION, counter-clockwise.
        (u[3][0],u[3][1],u[3][2],u[3][3]),     #face 3: No change.
        (u[1][0],u[1][1],u[4][2],u[4][3]),     #face 4: Top 2 squares shift counter-clockwise.
        (u[4][0],u[4][1],u[5][2],u[5][3])      #face 5: Top 2 squares shift counter-clockwise.
    )
    return v

#RIGHT CLOCKWISE, R
#Input: u, vertex of interest.
#Output: v, R permutation of u.
#F3->F1->F2->F5->F3#,#@F4#,#!F0#
#Note: Face 5 elements 2,0 exchange with Faces 2 and 3 elements 1 and 3.
def R_clock(u):
    v = ((u[0][0],u[0][1],u[0][2],u[0][3]),    #face 0: No change.
        (u[1][0],u[3][1],u[1][2],u[3][3]),     #face 1: Right two squares shift clockwise.
        (u[2][0],u[1][1],u[2][2],u[1][3]),     #face 2: Right two squares shift clockwise.
        (u[3][0],u[5][2],u[3][2],u[5][0]),     #face 3: Right two squares shift clockwise.
        (u[4][2],u[4][0],u[4][3],u[4][1]),     #face 4: 90* ROTATION, clockwise.
        (u[2][3],u[5][1],u[2][1],u[5][3])      #face 5: Left two squares.
    )
    return v

#RIGHT COUNTER-CLOCKWISE, R'
#Input: u, vertex of interest.
#Output: v, R' permutation of u.
#F3->F5->F2->F1->F3#,#@F4#,#!F0#
#Note: Face 5 elements 2,0 exchange with Faces 2 and 3 elements 1 and 3.
def R_count(u):
    v = ((u[0][0],u[0][1],u[0][2],u[0][3]),    #face 0: No change.
        (u[1][0],u[2][1],u[1][2],u[2][3]),     #face 1: Right two squares shift counter-clockwise.
        (u[2][0],u[5][2],u[2][2],u[5][0]),     #face 2: Right two squares shift counter-clockwise.
        (u[3][0],u[1][1],u[3][2],u[1][3]),     #face 3: Right two squares shift counter-clockwise.
        (u[4][1],u[4][3],u[4][0],u[4][2]),     #face 4: 90* ROTATION, counter-clockwise.
        (u[3][3],u[5][1],u[3][1],u[5][3])      #face 5: Left two squares shift.
    )
    return v

#FRONT CLOCKWISE, F
#Input: u, vertex of interest.
#Output: v, F permutation of u.
#F3->F0->F2->F4->F3#,#@F1#,#!F5#
#Note: Faces exchange elements non-standard. Refer to in-code comment.
def F_clock(u):
    v = ((u[0][0],u[3][0],u[0][2],u[3][1]),    #face 0: Right two squares shift clockwise.
        (u[1][2],u[1][0],u[1][3],u[1][1]),     #face 1: 90* ROTATION, clockwise.
        (u[2][0],u[2][1],u[0][3],u[0][1]),     #face 2: Bottom two squares shift clockwise.
        (u[4][2],u[4][0],u[3][2],u[3][3]),     #face 3: Top two squares shift clockwise.
        (u[2][2],u[4][1],u[2][3],u[4][3]),     #face 4: Left two squares shift clockwise.
        (u[5][0],u[5][1],u[5][2],u[5][3])      #face 5: No change.
    )
    return v

#FRONT COUNTER-CLOCKWISE, F'
#Input: u, vertex of interest.
#Output: v, F' permutation of u.
#F3->F4->F2->F0->F3#,#@F1#,#!F5#
#Note: Faces exchange elements non-standard. Refer to in-code comment.
def F_count(u):
    v = ((u[0][0],u[2][3],u[0][2],u[2][2]),   #face 0: Right two square shift counter-clockwise.
        (u[1][1],u[1][3],u[1][0],u[1][2]),     #face 1: 90* ROTATION, counter-clockwise.
        (u[2][0],u[2][1],u[4][0],u[4][2]),     #face 2: Bottom two squares shift counter-clockwise.
        (u[0][1],u[0][3],u[3][2],u[3][3]),     #face 3: Top two squares shift counter-clockwise.
        (u[3][1],u[4][1],u[3][0],u[4][3]),     #face 4: Left two squares shift counter-clockwise.
        (u[5][0],u[5][1],u[5][2],u[5][3])      #face 5: No change.
    )
    return v

#Permutes set of vertices V to a set of vertices P one turn away.
#Input: V, set of vertices.
#Output: P, set of permuted vertices.
def permute(V):
    P = set()
    for u in V:
        P.add(U_clock(u))
        P.add(U_count(u))
        P.add(R_clock(u))
        P.add(R_count(u))
        P.add(F_clock(u))
        P.add(F_count(u))
    return P


#COMPARE by intersection: set(visited permutations & completed states)
#if intersection set is non-empty, they share a complete state. Solved.
#Input: s, initial vertex of search.
#Output: j, integer representing distance from vertex s.
#Note: A distance class could be implemented, with recursion occuring on set D of vertices
#      instead of int j. For the purposes of this solution, we are not keeping track of set D.
def solution(s):
    #Declared here to keep the solution self contained. C set in helper functions. Refer to top of file for further description.
    d = {(('r','r','r','r'),('b','b','b','b'),('w','w','w','w'),('y','y','y','y'),('o','o','o','o'),('g','g','g','g')), 
        (('b','b','b','b'),('o','o','o','o'),('w','w','w','w'),('y','y','y','y'),('g','g','g','g'),('r','r','r','r')),
        (('o','o','o','o'),('g','g','g','g'),('w','w','w','w'),('y','y','y','y'),('r','r','r','r'),('b','b','b','b')),
        (('g','g','g','g'),('r','r','r','r'),('w','w','w','w'),('y','y','y','y'),('b','b','b','b'),('o','o','o','o')), #4
        (('b','b','b','b'),('w','w','w','w'),('r','r','r','r'),('o','o','o','o'),('g','g','g','g'),('y','y','y','y')),
        (('w','w','w','w'),('g','g','g','g'),('r','r','r','r'),('o','o','o','o'),('y','y','y','y'),('b','b','b','b')),
        (('g','g','g','g'),('y','y','y','y'),('r','r','r','r'),('o','o','o','o'),('b','b','b','b'),('w','w','w','w')),
        (('y','y','y','y'),('b','b','b','b'),('r','r','r','r'),('o','o','o','o'),('w','w','w','w'),('g','g','g','g')), #8
        (('w','w','w','w'),('r','r','r','r'),('b','b','b','b'),('g','g','g','g'),('y','y','y','y'),('o','o','o','o')),
        (('r','r','r','r'),('y','y','y','y'),('b','b','b','b'),('g','g','g','g'),('o','o','o','o'),('w','w','w','w')),
        (('y','y','y','y'),('o','o','o','o'),('b','b','b','b'),('g','g','g','g'),('w','w','w','w'),('r','r','r','r')),
        (('o','o','o','o'),('w','w','w','w'),('b','b','b','b'),('g','g','g','g'),('r','r','r','r'),('y','y','y','y')), #12
        (('b','b','b','b'),('r','r','r','r'),('y','y','y','y'),('w','w','w','w'),('g','g','g','g'),('o','o','o','o')),
        (('r','r','r','r'),('g','g','g','g'),('y','y','y','y'),('w','w','w','w'),('o','o','o','o'),('b','b','b','b')),
        (('g','g','g','g'),('o','o','o','o'),('y','y','y','y'),('w','w','w','w'),('b','b','b','b'),('r','r','r','r')),
        (('o','o','o','o'),('b','b','b','b'),('y','y','y','y'),('w','w','w','w'),('r','r','r','r'),('g','g','g','g')), #16
        (('w','w','w','w'),('b','b','b','b'),('o','o','o','o'),('r','r','r','r'),('y','y','y','y'),('g','g','g','g')),
        (('b','b','b','b'),('y','y','y','y'),('o','o','o','o'),('r','r','r','r'),('g','g','g','g'),('w','w','w','w')),
        (('y','y','y','y'),('g','g','g','g'),('o','o','o','o'),('r','r','r','r'),('w','w','w','w'),('b','b','b','b')),
        (('g','g','g','g'),('w','w','w','w'),('o','o','o','o'),('r','r','r','r'),('b','b','b','b'),('y','y','y','y')), #20
        (('r','r','r','r'),('w','w','w','w'),('g','g','g','g'),('b','b','b','b'),('o','o','o','o'),('y','y','y','y')),
        (('w','w','w','w'),('o','o','o','o'),('g','g','g','g'),('b','b','b','b'),('y','y','y','y'),('r','r','r','r')),
        (('o','o','o','o'),('y','y','y','y'),('g','g','g','g'),('b','b','b','b'),('r','r','r','r'),('w','w','w','w')),
        (('y','y','y','y'),('r','r','r','r'),('g','g','g','g'),('b','b','b','b'),('w','w','w','w'),('o','o','o','o'))  #24
    }
    #instance = (s, C)
    #Fringe case: Check if s is a completed state.
    if s in d:
        print("Solved cube was provided. No moves required.")
        return 0
    #Otherwise, we fall through to graph traversal
    #Sets S and D are declared and utilized within the breadthFirst() search.
    #S and D are subsets of V. S, vertices at least distance j from s. D, vertices distance j from s.
    j = breadthFirst(s, d)
    if j == -1:
        print("Error: 14 turns exceeded. Please check supplied cube state is valid.")
        return 0
    else:
        print("Smallest number of moves required to solve: ", j)
        return 1
    
#################
###ENTRY POINT###
#################
try:
    solution(s)
except:
    print("Error: please provide a valid state of the cube.")
    print("Valid example: (('y','w','r','g'),('b','r','y','r'),('r','w','o','w'),('o','y','g','y'),('b','o','b','b'),('g','g','o','w'))")