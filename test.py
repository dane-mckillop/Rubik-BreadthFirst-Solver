s = (('y','w','r','g'), #face 0
    ('b','r','y','r'),  #face 1
    ('r','w','o','w'),  #face 2
    ('o','y','g','y'),  #face 3
    ('b','o','b','b'),  #face 4
    ('g','g','o','w')   #face 5
)

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
#Input: u, vertex of interest
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
#Input: u, vertex of interest
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
#Input: u, vertex of interest
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
#Input: u, vertex of interest
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
#Input: u, vertex of interest
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

def permute(u):
    P = set()
    P.add(U_clock(u))
    P.add(U_count(u))
    P.add(R_clock(u))
    P.add(R_count(u))
    P.add(F_clock(u))
    P.add(F_count(u))
    return P

def genDnew(D):
    
    return D_new

def solution(s):
    D = {s}
    print('Permutations:',genDnew(D))
    print('Intersection:',len(genDnew(D).intersection(D)))

solution(s)