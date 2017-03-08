# Matrix Algebra

from sympy import *

A = Matrix([[1,2,3],[2,7,4]])
B = Matrix([[1,-1],[0,1]])
C = Matrix([[5,-1],[9,1],[6,0]])
D = Matrix([[3,-2,-1],[1,2,3]])
u = Matrix([[6,2,-3,5]])
v = Matrix([[3,5,-1,4]])
w = Matrix([[1],[8],[0],[5]])


# 1. Matrix Dimensions

# 1.1) A
print A.shape # (2,3)

# 1.2) B
print B.shape # (2,2)

# 1.3) C
print C.shape # (3,2)

# 1.4) D
print D.shape # (2,3)

# 1.5) u
print u.shape # (1,4)

# 1.6) w
print w.shape # (4,1)
 
    
# 2. Vector Operations

#2.1) u + v
print u + v # [[9, 7, -4, 9]]

#2.2) u - v
print u - v # [[3, -3, -2, 1]]

#2.3) a * u, where a = 6
a = 6
print a * u # [[36, 12, -18, 30]]

#2.4) u dot v 
print u.dot(v) # 51

#2.5) norm u
print u.norm() # sqrt(74)


# 3. Matrix Operations

# 3.1) A + C
# Not defined

# 3.2) A - C.T
print A - C.T # [[-4, -7, -3],[3, 6, 4]]

# 3.3) C.T + 3*D
print C.T + 3*D # [[14, 3, 3],[2, 7, 9]]

# 3.4) B * A
print B * A # [[-1, -5, -1],[2, 7, 4]]

# 3.5) B * A.T
# Not defined

# 3.6) B * C
# Not defined

# 3.7) C * B
print C * B # [[5, -6], [9, -8], [6, -6]]

# 3.8) B**4
print B**4 # [[1, -4],[0, 1]]

# 3.9) A * A.T
print A * A.T # [[14, 28],[28, 69]]

# 3.10) D.T * D
print D.T * D # [[10, -4, 0],[-4, 8, 8],[0, 8, 10]]