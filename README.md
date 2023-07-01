1. Introduction 
The 2×2 Rubik’s cube is a small puzzle with six faces, each face having four squares. In a 
completed state each face respectively is coloured red, blue, white, yellow, orange or green. 
Operations may be performed on the cube by rotating one of the faces of the cube by 90°, 
either clockwise or anti-clockwise. These rotations result in a distinct permutation, in which 
each of the six faces will have some combination of red, blue, white, yellow, orange or green 
squares.

Typically, the cube will start in a scrambled state, with the goal to perform operations so 
that the cube is solved, ending in the aforementioned completed state. Six sets of 
operations, excluding equivalent moves, may be performed to reach a new permutation of 
the cube. These are: 
 -A right face clockwise turn. 
 -A right face counter-clockwise turn. 
 -A front face clockwise turn. 
 -A front face counter-clockwise turn. 
 -An upper face clockwise turn. 
 -An upper face counter-clockwise turn. 
Left, bottom and rear rotations will be omitted to reduce complexity. For example, a left 
face clockwise turn and a right face counter-clockwise turn result in the same permutation. 
Given any initial state of the cube, it is desirable to know the shortest number of rotations 
required to reach a completed state. 

2. Instance Model 
An instance of the problem is described by a set of faces, a starting state of the cube and a 
solved state of the cube. A state represents one of the 3,674,160 permutations of the cube 
which are reachable through legal moves. If this is the number of vertices in 𝑉, then it is not 
efficient to populate the set of vertices before operating. Additionally, we can derive a 
completed state of the cube as set of tuples whose members contain consistent elements. 
The example starting state and completed states of the cube provided, as well as a mapping 
of the cube are 
{(𝑦, 𝑤, 𝑟, 𝑔), (𝑏, 𝑟, 𝑦, 𝑟), (𝑟, 𝑤, 𝑜, 𝑤), (𝑜, 𝑦, 𝑔, 𝑦), (𝑏, 𝑜, 𝑏, 𝑏), (𝑔, 𝑔, 𝑜, 𝑤)}
{(𝑟, 𝑟, 𝑟, 𝑟), (𝑏, 𝑏, 𝑏, 𝑏), (𝑤, 𝑤, 𝑤, 𝑤), (𝑦, 𝑦, 𝑦, 𝑦), (𝑜, 𝑜, 𝑜, 𝑜), (𝑔, 𝑔, 𝑔, 𝑔)}
 
The instance is modelled by (𝑠, 𝑑) where 𝑠 is the starting state of the cube and 𝑑 is the
completed state of the cube. Then the instance model is 
ቆ
{(𝑦, 𝑤, 𝑟, 𝑔), (𝑏, 𝑟, 𝑦, 𝑟), (𝑟, 𝑤, 𝑜, 𝑤), (𝑜, 𝑦, 𝑔, 𝑦), (𝑏, 𝑜, 𝑏, 𝑏), (𝑔, 𝑔, 𝑜, 𝑤)},
{(𝑟, 𝑟, 𝑟, 𝑟), (𝑏, 𝑏, 𝑏, 𝑏), (𝑤, 𝑤, 𝑤, 𝑤), (𝑦, 𝑦, 𝑦, 𝑦), (𝑜, 𝑜, 𝑜, 𝑜), (𝑔, 𝑔, 𝑔, 𝑔)}
ቇ
Regarding the completed combination 𝑑, it should be noted there are 24 orientations from 
which a completed cube may be viewed from. Representing these states through tuples is 
tedious, so 𝑑 shall be represented here as a set. This is to emphasize that the combination 
of 𝑑’s faces is irrelevant, only that they are correctly colour matched. For all other 
permutations, order of the faces is significant. 

3. Solution Model 
In order to find the minimum number of operations required to solve the cube, we need to 
identify the distance from our initial state to our completed state. As we have no predefined 
set of permutations, we shall record the permutations we arrive upon as we perform turns 
on the cube. A sequence of turns should not exceed 14, with the last turn ending in the 
completed state. 
Therefore, the solution will be the length of the shortest sequence of turns between two 
states of the cube 𝑠, 𝑎, 𝑏, 𝑐, . . . , 𝑑 where the first state is the initial state and the last state is 
the completed state. For the purposes of this solution, the sequence of turns itself is not 
significant.

4. Problem Model 
Let an instance (𝑠, 𝑑) be given. We model the permutations of the cube as a graph 
𝐺 = (𝑉, 𝐸). The set of vertices 𝑉 is the set of all 3,674,160 permutations of the cube. 
That is,
V = sum(j=1, n=3674160, f=v(j))
The set of edges 𝐸 contains each 90° turn (𝑢, 𝑣) between the vertices of state 𝑢 ∈ 𝑉
distance 𝑗 − 1 and permutation 𝑣 ∈ 𝑉 distance 𝑗. Since each state has six edges connecting 
to six permutations that is, 
𝑬 = ቐ{𝑢 ∈ 𝑆}:sum(j=1, f=u(j-1), v(j))
We define 𝑆 ⊆ 𝑉 since set 𝑉 is unknown except for 𝑠 ∈ 𝑉 and 𝑑 ∈ 𝑉. Set 𝑆 contains the 
vertices 𝑢 ∈ 𝑆 distance 𝑗 traversed to visit 𝑑 ∈ 𝑆. That is, 
𝑺 = ቊ
{𝑠} ∶ 𝑗 = 0
{𝑠, u(1), u(2), … , u(j-1), d(j)} ∶ 𝑗 ≥ 1
ቋ
As the sequence of turns between 𝑠 and 𝑑 is not significant, the set of edges 𝑇 ⊆ 𝐸 is not 
significant. For consistency, let us define the subset of edges (𝑢, 𝑣) ∈ 𝑇 as the set of edges 
between vertices in set 𝑆, such that 𝑇 = 𝑆 × 𝑆. 
We can get from 𝑠 to 𝑑 by following a path in the subgraph 𝐺
G' = (𝑆, 𝑇) from 𝑠 to 𝑑. 
Therefore, the solution is the length of the shortest path between 𝑠 and 𝑑, given by the 
distance 𝑗 at 𝑑 starting from 𝑠.

5. Solution Model 
As we are attempting to find the length of the shortest path from 𝑠 to 𝑑, we shall implement 
a breadth first search. Each 𝑢 vertex of a cube’s state shall be a tuple of six tuples, each with 
four elements. As we do not know the 𝑢 vertices of 𝑉, we define 𝑆 ⊆ 𝑉, which will be 
required to track vertices in distance classes 𝐷(j). 
To find each set 𝐷(j), we employ a recursive definition which will permute each 𝑢 ∈ 𝐷(j-1) into 
a 𝑣 ∈ 𝐷(j). Initially, 𝑆 = {𝑠} and 𝐷(0) = {𝑠}.
From here we recursively generate 6 × 𝑣 ∈ 𝐷(j) from 𝑢 ∈ 𝐷(j-1) by rearranging elements of 
tuple 𝑢, consistent with the physical equivalent of turning a face. From here, we check that 
∀𝑣 ∈ 𝐷(j) are indeed 𝑗 distance from 𝑠 by set difference to see if ∀𝑣 ∈ 𝐷(j)∶ 𝑣 ∉ S, such that 
𝑫(j) = 𝐷(j) − 𝑆
We can also define 𝑣 ∈ 𝐷(j) as being in the neighbourhood of 𝐷(j-1) but not vertices in sets 
D(0) … D(j-1), notated by
𝑫(j) = 𝑁(v(j)) * 𝐷(j-1)
𝐶 shall be a set containing 24 vertices equivalent to 𝑑 where order is significant. By 
intersection, we then evaluate if the cube has been solved where ∃𝑑 ∈ 𝐷(j)∶ 𝑑 ∈ 𝐶 , that is 
{d} = 𝐷(j) ∩ 𝐶
If the intersection is an empty set, 𝑆 records the new visited vertices distance 𝑗 from 𝑠 for 
the next recursion, through a union of the neighbourhood of 𝑆(j-1) with 𝐷(j), consistent with
𝑺(j) = 𝑁(v(j)) * 𝑆(j-1) ∪ 𝐷(j)
If the intersection is a non-empty set, we have traversed shortest path length 𝑗 of graph 𝐺′
from 𝑠 to 𝑑. There may be more than one 𝑑 for each 𝑠, that is there may be multiple 𝑑
vertices an equal distance 𝑗 from vertex 𝑠. However, we only require 𝑗, so this is not 
significant. For any vertex 𝑢 ∈ 𝐷(j), we can identify the length j of the shortest path to 𝑑 as 
ℓ(𝑢, 𝑑), therefore: 
𝑗(𝑢) = ℓ(𝑢, 𝑑)

To summarise, the solution can be found from an instance as follows: 
1. Initialize 𝑆 and 𝐷 to {𝑠}. 
2. Calculate 𝐷(j) recursively. 
3. Check if intersection of 𝐷(j) and 𝐶 is non-empty, return 𝑗 if so. 
4. Populate 𝑆 by performing a union with 𝐷(j) after each check.
