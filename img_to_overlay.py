"""
The point of this program is to turn a normal image into an overlay image which can be used for r/place


"""
from PIL import Image
import numpy as np

# The start coords of the image (top left corner)
start_coords = (1558, 575)


canvas_x, canvas_y = (2000, 1000)




img_file = "billy.png"

img = np.array(Image.open(img_file))



# The size of pixels that make up one pixel on the canvas
# In this case one pixel on the canvas is represented by a 3x3 chunk, with all the outer pixels being empty and only the center pixel holding the actual value
chunk_size = 3



output_img_size = (canvas_y * chunk_size, canvas_x * chunk_size, 4)

new_img = np.zeros(shape=output_img_size, dtype=np.uint8)


start_x, start_y = start_coords


for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        pixel = img[y, x]

        # Checks whether pixel is nothing or actually has some colour. If any of the 3 rgb values is non-zero, we don't skip (if all of the values are 0, we skip)
        if not pixel.any():
            # Empty pixel, skip
            continue

        new_img[(start_y + y) * chunk_size + 1, (start_x + x) * chunk_size + 1] = pixel


overlay_img = Image.fromarray(new_img)

overlay_img.save("overlay_img.png")