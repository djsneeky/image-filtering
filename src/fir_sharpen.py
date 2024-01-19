import numpy as np
import matplotlib.pyplot as plt

# FIR LPF filter
# Define the range of frequency variables u and v
u = np.linspace(-np.pi, np.pi)
v = np.linspace(-np.pi, np.pi)

# Create a meshgrid for (u, v)
uu, vv = np.meshgrid(u, v)

# Calculate the frequency response magnitude
H_uv = np.abs(sum(sum((1/25) * np.exp(-1j * (uu * n + vv * m)) for n in range(-2, 3)) for m in range(-2, 3)))

plt.style.use('dark_background')

# Plot the magnitude of the frequency response
fig1, ax1 = plt.subplots()
co = ax1.contourf(uu, vv, H_uv, cmap='plasma')
fig1.colorbar(co, label='Magnitude', ax=ax1)
ax1.set_title('FIR LPF Frequency Response')
ax1.set_xlabel('u')
ax1.set_ylabel('v')

fig2, ax2 = plt.subplots(subplot_kw={"projection": "3d"})
su = ax2.plot_surface(uu, vv, H_uv, cmap='plasma')
fig2.colorbar(su, label='Magnitude', ax=ax2)
ax2.set_title('FIR LPF Frequency Response')
ax2.set_xlabel('u')
ax2.set_ylabel('v')

fig1.savefig('fir_lpf_5_freq_resp_2d')
fig2.savefig('fir_lpf_5_freq_resp_3d')

# FIR Sharpen filter
# Define the range of frequency variables u and v
u = np.linspace(-np.pi, np.pi)
v = np.linspace(-np.pi, np.pi)

# Create a meshgrid for (u, v)
uu, vv = np.meshgrid(u, v)

# Calculate the frequency response magnitude
lam = 1.5
G_uv = np.abs(1 + lam * (1 - sum(sum(1/25 * np.exp(-1j * (uu * n + vv * m)) for n in range(-2, 3)) for m in range(-2, 3))))

fig3, ax3 = plt.subplots()
co = ax3.contourf(uu, vv, G_uv, cmap='plasma')
fig3.colorbar(co, label='Magnitude', ax=ax3)
ax3.set_title('FIR Sharpen Frequency Response')
ax3.set_xlabel('u')
ax3.set_ylabel('v')

fig4, ax4 = plt.subplots(subplot_kw={"projection": "3d"})
su = ax4.plot_surface(uu, vv, G_uv, cmap='plasma')
fig4.colorbar(su, label='Magnitude', ax=ax4)
ax4.set_title('FIR Sharpen Frequency Response')
ax4.set_xlabel('u')
ax4.set_ylabel('v')

fig3.savefig('fir_sharpen_freq_resp_2d')
fig4.savefig('fir_sharpen_freq_resp_3d')

plt.show()