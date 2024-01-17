from PIL import Image
import numpy as np

im = Image.open('img/img03.tif')
im.show()

x = np.array(im)
# img_out = Image.fromarray(x)
# img_out.save('img_out.tif')

# convert image to uint8 before writing to file
# img_out = Image.fromarray(x.astype(np.uint8))
# img_out.save('img/img03_out.tif')
