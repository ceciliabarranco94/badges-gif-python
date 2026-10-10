from PIL import Image
import imageio.v3 as iio
import numpy as np

filenames = ['1-earthBadge.png', '2-memoryBadge.png', '3-roadBadge.png', '4-haloBadge.png', '5-sequenceBadge.png', '6-puzzleBadge.png', '7-rubyBadge.png', '8-filesBadge.png']
target_size = (800, 600)

images = []

for filename in filenames:
  img = Image.open(filename).convert("RGB").resize(target_size)
  images.append(np.array(img))

iio.imwrite('badges.gif', images, duration = 500, loop = 0)
print("¡GIF creado con éxito!")

