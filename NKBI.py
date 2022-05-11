import os ,sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

bn = r'C:\Users\ADMIN\Downloads\Result_Compare_3_softwares\Result_Compare_3_softwares\Bernese\NKBI.csv'
gx = r'C:\Users\ADMIN\Downloads\Result_Compare_3_softwares\Result_Compare_3_softwares\GipsyX\NKBI.csv'
rk = r'C:\Users\ADMIN\Downloads\Result_Compare_3_softwares\Result_Compare_3_softwares\RTKLIB\NKBI.csv'

df_bn = pd.read_csv(bn)
df_gx = pd.read_csv(gx)
df_rk = pd.read_csv(rk)

gx_bn = pd.merge(df_gx ,df_bn , left_on='id' , right_on='id')
gx_rk = pd.merge(df_gx ,df_rk , left_on='id' , right_on='id')
bn_rk = pd.merge(df_bn ,df_rk , left_on='id' , right_on='id')

dE1 = gx_bn['utm_e_x']-gx_bn['utm_e_y']
dN1 = gx_bn['utm_n_x']-gx_bn['utm_n_y']
dH1 = gx_bn['ell_h_x']-gx_bn['ell_h_y']
dS1 = (dE1**2+dN1**2)**0.5
dR1 = (dE1**2+dN1**2+dH1**2)**0.5
dE2 = gx_rk['utm_e_x']-gx_rk['utm_e_y']
dN2 = gx_rk['utm_n_x']-gx_rk['utm_n_y']
dH2 = gx_rk['ell_h_x']-gx_rk['ell_h_y']
dS2 = (dE2**2+dN2**2)**0.5
dR2 = (dE2**2+dN2**2+dH2**2)**0.5
dE3 = bn_rk['utm_e_x']-bn_rk['utm_e_y']
dN3 = bn_rk['utm_n_x']-bn_rk['utm_n_y']
dH3 = bn_rk['ell_h_x']-bn_rk['ell_h_y']
dS3 = (dE3**2+dN3**2)**0.5
dR3 = (dE3**2+dN3**2+dH3**2)**0.5
           
avggbs = dS1.mean()
stdgbs = dS1.std()
avggbr = dR1.mean()
stdgbr = dR1.std()
print('average distanae2D 1 =', avggbs)
print('std distanae2D 1 =', stdgbs)
print('average distanae3D 1 =', avggbr)
print('std distanae3D 1 =', stdgbr)


avggrs = dS2.mean()
stdgrs = dS2.std()
avggrr = dR2.mean()
stdgrr = dR2.std()
print('average distanae2D 2 =', avggrs)
print('std distanae2D 2 =', stdgrs)
print('average distanae3D 2 =', avggrr)
print('std distanae3D 2 =', stdgrr)

avgbrs = dS3.mean()
stdbrs = dS3.std()
avgbrr = dR3.mean()
stdbrr = dR3.std()
print('average distanae2D 3 =', avgbrs)
print('std distanae2D 3 =', stdgbs)
print('average distanae3D 3 =', avgbrr)
print('std distanae3D 3 =', stdbrr)




fig,ax1 = plt.subplots()
ax1.plot(gx_bn['doy_x'],gx_bn['utm_e_x'],'x',markersize=14)
ax1.plot(gx_bn['doy_x'],gx_bn['utm_e_y'],'+',markersize=14)
plt.show()

fig,ax2 = plt.subplots()
ax2.plot(gx_bn['doy_x'],gx_bn['utm_n_x'],'x',markersize=14)
ax2.plot(gx_bn['doy_x'],gx_bn['utm_n_y'],'+',markersize=14)
plt.show()

fig,ax3 = plt.subplots()
ax3.plot(gx_bn['doy_x'],gx_bn['ell_h_x'],'x',markersize=14)
ax3.plot(gx_bn['doy_x'],gx_bn['ell_h_y'],'+',markersize=14)
plt.show()

fig,ax4 = plt.subplots()
ax4.plot(gx_rk['doy_x'],gx_rk['utm_e_x'],'x',markersize=14)
ax4.plot(gx_rk['doy_x'],gx_rk['utm_e_y'],'2',markersize=14)
plt.show()

fig,ax5 = plt.subplots()
ax5.plot(gx_rk['doy_x'],gx_rk['utm_n_x'],'x',markersize=14)
ax5.plot(gx_rk['doy_x'],gx_rk['utm_n_y'],'2',markersize=14)
plt.show()

fig,ax6 = plt.subplots()
ax6.plot(gx_rk['doy_x'],gx_rk['ell_h_x'],'x',markersize=14)
ax6.plot(gx_rk['doy_x'],gx_rk['ell_h_y'],'2',markersize=14)
plt.show()

fig,ax7 = plt.subplots()
ax7.plot(bn_rk['doy_x'],bn_rk['utm_e_x'],'+',markersize=14)
ax7.plot(bn_rk['doy_x'],bn_rk['utm_e_y'],'2',markersize=14)
plt.show()

fig,ax8 = plt.subplots()
ax8.plot(bn_rk['doy_x'],bn_rk['utm_n_x'],'+',markersize=14)
ax8.plot(bn_rk['doy_x'],bn_rk['utm_n_y'],'2',markersize=14)
plt.show()
           
fig,ax9 = plt.subplots()
ax9.plot(bn_rk['doy_x'],bn_rk['ell_h_x'],'+',markersize=14)
ax9.plot(bn_rk['doy_x'],bn_rk['ell_h_y'],'2',markersize=14)
plt.show()    
