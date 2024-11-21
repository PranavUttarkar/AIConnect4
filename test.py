# def go2(i, q):
#     if i == 0:
#         q += 1
#     for j in range(i):
#         q = go(i - 1, q)
#         print(i, q, 'go2')
#     return q

# def go(i, q):
#     if i == 0:
#         q += 1
#     for j in range(i):
#         q = go2(i - 1, q)
#         print(i, q, 'go')
#     return q

# def main():
#     q = 0
#     q = go(2, q)
#     print(q)

# main()

# s=""
# n=0
# for i in range(2):
#     while(n<3):
#         s = "*" + s
#         n+=1
#     while(n>0):
#         s += "_"
#         n-=1
#     s += "\n"
# print(s)

# def aplus(i):
#     j=0
#     while(i!=1):
#         if(i%2==0):
#             i/=2
#         else:
#             i=i*3+1
#         j+=1
#     print(j)
# aplus(20)

import numpy as np
a = np.array([[2, 4], [5, 7]])
print(a)
print(np.dot(a, 2))
a += a
print(a)