# Author: Yebo Feng
# Apr 18 2019

import numpy as np

def fleiss_kappa(M):
  N, k = M.shape
  n_annotators = float(np.sum(M[0, :]))
  p = np.sum(M, axis=0) / (N * n_annotators)
  P = (np.sum(M * M, axis=1) - n_annotators) / (n_annotators * (n_annotators - 1))
  print P
  print p
  Pbar = np.sum(P) / N
  PbarE = np.sum(p * p)
  kappa = (Pbar - PbarE) / (1 - PbarE)
  return kappa

# def transfer(T):
#     R
#     return R

"""
# Below is a test table in wikipedia's format, the result of this table should be 0.210.
table = np.array([[0, 0, 0, 0, 14],
                  [0, 2, 6, 4, 2],
                  [0, 0, 3, 5, 6],
                  [0, 3, 9, 2, 0],
                  [2, 2, 8, 1, 1],
                  [7, 7, 0, 0, 0],
                  [3, 2, 6, 3, 0],
                  [2, 5, 3, 2, 2],
                  [6, 5, 2, 1, 0],
                  [0, 2, 2, 3, 7]])
"""

data=np.loadtxt("fleiss_kappa.csv",delimiter=",",skiprows=1)
print data
res = fleiss_kappa(data)
print res
