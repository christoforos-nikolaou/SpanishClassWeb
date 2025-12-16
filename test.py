import numpy as np
import matplotlib.pyplot as plt
phi, theta = np.meshgrid(np.linspace(0, np.pi, 100), np.linspace(0, 2*np.pi, 200))
# Simulate Earth texture (e.g., simplified land mask or load image)
earth_map = np.sin(phi) * np.cos(theta)**2  # Placeholder topography
plt.imshow(earth_map, extent=[0, 360, -90, 90], aspect='auto', origin='lower')
plt.xlabel('Longitude θ (degrees)'); plt.ylabel('Latitude (90°-φ)');
plt.title('Earth in θ-φ Coordinates')