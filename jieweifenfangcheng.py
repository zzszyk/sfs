from numpy import *

h = 2*pi/N
x = linspace(0, 2*pi, N+1)
A = zeros((N, N))
F = zeros((N, 1))
u = zeros((N+1, 1))
for i in range(N):
    A[i, i] = 1
    if i > 0: A[i, i-1] = h-1
    F[i] = h*(sin(x[i]) + cos(x[i]))
u[1:] = dot(linalg.inv(A), F)
