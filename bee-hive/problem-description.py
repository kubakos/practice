"""
Input
The input contains two lines. The first line contains five blank separated integers: R N A B X
R: the length (number of cells) of each edge of the grid, where 2≤R≤20. The total number of cells in the grid can be determined by taking a difference of cubes, R3-(R-1)3.
N: the maximum number of cells 0x67 can chew through, where 1≤N<R3-(R-1)3.
A: the starting cell ID, This cell is located on one of the grid edges: The cell has fewer than six neighbors.
B: the cell ID of the cell containing the honey, where 1≤B≤R3-(R-1)3.
X: the number of wax-hardened cells, where 0≤X<(R3-(R-1)3)-1.
The second line contains X integers separated by spaces, where each integer is the ID of a wax-hardened cell.
The ID's, A, B, and all the ID's on the second line, are distinct positive integers less than or equal to R3-(R-1)3.

Output
A single integer K if 0x67 reached the honey at cell B, where B is the Kth cell, otherwise the string No if it was impossible to reach the honey by chewing through N cells or less. 
"""
