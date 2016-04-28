#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

m = np.genfromtxt('../DP4/MINT_Krho_SPD_wave.txt', skip_header=1,delimiter=',')
sig = np.genfromtxt("SigGen.txt", skip_header=1)

m12 = m[:,0]
m34 = m[:,1]
c12 = m[:,2]
c34 = m[:,3]
phi = m[:,4]

m12_1 = sig[:,0]
m34_1 = sig[:,1]
c12_1 = sig[:,2]
c34_1 = sig[:,3]
phi_1 = sig[:,4]
w_1   = sig[:,5]

weights = 1.0/len(m12) * np.ones_like(m12)

plt.figure(figsize=(12,6))
plt.hist(m12,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(m12_1,100, weights=w_1/np.sum(w_1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_{SPD}\ m(\pi^+\pi^-)$', fontsize=20)
plt.legend()
plt.savefig("SigGen_m12.png")

plt.figure(figsize=(12,6))
plt.hist(m34,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(m34_1,100, weights=w_1/np.sum(w_1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_{SPD}\ K^-\pi^-$', fontsize=20)
plt.legend()
plt.savefig("SigGen_m34.png")

plt.figure(figsize=(12,6))
plt.hist(phi,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(phi_1,100, weights=w_1/np.sum(w_1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_{SPD} \ \phi$', fontsize=20)
plt.legend()
plt.savefig("SigGen_phi.png")

plt.figure(figsize=(12,6))
plt.hist(c12,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(c12_1,100, weights=w_1/np.sum(w_1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_{SPD} \ \cos(\theta_{12})$', fontsize=20)
plt.legend()
plt.savefig("SigGen_c12.png")

plt.figure(figsize=(12,6))
plt.hist(c34,100, weights=weights,alpha=0.5,label='MINT')
plt.hist(c34_1,100, weights=w_1/np.sum(w_1),alpha=0.5, label='GooFit')
plt.title(r'$(K^*\rho^0)_{SPD} \ \cos(\theta_{34})$', fontsize=20)
plt.legend()
plt.savefig("SigGen_c34.png")