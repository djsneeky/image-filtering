import numpy as np
from PIL import Image

def apply_filter(x):
    M, N = x.shape
    y = np.zeros((M, N), dtype=float)

    for m in range(1, M):
        for n in range(1, N):
            y[m, n] = 0.01 * x[m, n] + 0.9 * (y[m - 1, n] + y[m, n - 1]) - 0.81 * y[m - 1, n - 1]

    return y

# Create a 256x256 image with a delta function
x = np.zeros((256, 256), dtype=float)
x[127, 127] = 1.0

# Apply the filter
psf = apply_filter(x)

# Scale and convert to uint8 for saving
scaled_psf = (255 * 100 * psf).astype(np.uint8)

# Save the result to a TIFF file
output_path = 'h_out.tif'
Image.fromarray(scaled_psf).save(output_path)
