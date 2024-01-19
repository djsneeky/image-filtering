import numpy as np
import matplotlib.pyplot as plt

# Define the range of frequency variables u and v
u = np.linspace(-np.pi, np.pi)
v = np.linspace(-np.pi, np.pi)

# Create a meshgrid for (u, v)
uu, vv = np.meshgrid(u, v)

# Calculate the frequency response magnitude
H_uv = np.abs(0.01 / (1 - 0.9 * np.exp(-1j * uu) - 0.9 * np.exp(-1j * vv) + 0.81 * np.exp(-1j * uu) * np.exp(-1j * vv)))

plt.style.use('dark_background')

# Plot the magnitude of the frequency response
fig1, ax1 = plt.subplots()
co = ax1.contourf(uu, vv, H_uv, cmap='plasma')
fig1.colorbar(co, label='Magnitude', ax=ax1)
ax1.set_title('IIR Frequency Response')
ax1.set_xlabel('u')
ax1.set_ylabel('v')

fig2, ax2 = plt.subplots(subplot_kw={"projection": "3d"})
su = ax2.plot_surface(uu, vv, H_uv, cmap='plasma')
fig2.colorbar(su, label='Magnitude', ax=ax2)
ax2.set_title('IIR Frequency Response')
ax2.set_xlabel('u')
ax2.set_ylabel('v')

fig1.savefig('iir_freq_resp_2d')
fig2.savefig('iir_freq_resp_3d')

plt.show()