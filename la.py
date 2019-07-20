from mat import *
import numpy as np

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    
    # solve(A,b)
    # A - matrix m,k
    # b - matrix k,1 
    # x- lsit of solution [x_1, x_2, ... , x_n]
    
    # using Guass Method
    # 1. กำจัดจุดอ่อน - elimination
    # 2. เเทนค่าย้อนกลับ - back substitution
    
    # YOUR CODE HERE
    A, b = np.array(A), np.array(b)
    n = len(A[0])
    x = np.array([0]*n)
    
    # 1. elimination
    n = len(A[0]) 
    print( f'n={n}')
    for  k in range(n-1): #pivot
        print(f'k={k}')
        for j in range(k+1, n):
            print(f'\tกำจัดตัวแปร{k},ออกจากสมการที่{j}')
            lam = A[j][k]/A[k][k]
            #update A[j][k เป็นต้นไป]

            A[j][k+1:n] = A[j][k+1:n] - lam * A[k][k+1:n]
            # print(f'\t\tlambda={lam}')
            
            #Update B[j]
            b[j] = b[j] - lam * b[k]
        print(A)
        print(b)

    # 2. back substitution
    # x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n-1, -1, -1):
        print(f'back sub k ={k}')
        x[k] = (b[k] - np.dot(A[k,k+1:n], x[k+1:n]))/A[k,k]  
    return x.flatten()

print("==== A ====")
print(A)
print("==== b ====")
print(b)

print( solve(A, b) )