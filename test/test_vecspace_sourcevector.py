import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import cg, inv, spsolve
from fealpy.pde.darcy_forchheimer_2d import DarcyForchheimerdata1
from fealpy.functionspace.lagrange_fem_space import VectorLagrangeFiniteElementSpace

box = [-1, 1, -1, 1]
mu = 1
rho = 1
beta = 10
alpha = 1/beta
tol = 1e-6
level = 1
mg_maxN = 1
maxN = 2000
p = 0

pde = DarcyForchheimerdata1(box,mu,rho,beta,alpha,level,tol,maxN,mg_maxN)
mesh = pde.init_mesh(level)
NC = mesh.number_of_cells()
NN = mesh.number_of_nodes()
cellmeasure = mesh.entity_measure('cell')

integrator = mesh.integrator(p+2)
V = VectorLagrangeFiniteElementSpace(mesh, p, spacetype='D')
b = V.source_vector(pde.f, integrator, cellmeasure)
print(b)
