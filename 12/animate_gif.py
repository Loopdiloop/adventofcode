
import imageio.v3 as iio
import matplotlib.pyplot as plt
import numpy as np

n = 100
gif_path = "path_taken.gif"

n = 360

frames = np.stack([iio.imread(f"plots/step_{x}.png") for x in range(n)], axis=0)

iio.imwrite(gif_path, frames)