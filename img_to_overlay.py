"""
The point of this program is to turn a normal image into an overlay image which can be used for r/place


"""
from PIL import Image
import numpy as np


# Constants

canvas_x, canvas_y = (2000, 1000)

# The size of pixels that make up one pixel on the canvas
# In this case one pixel on the canvas is represented by a 3x3 chunk, with all the outer pixels being empty and only the center pixel holding the actual value
chunk_size = 3

finished_file = "dani_place_overlay.png"



class Sketch:
    def __init__(self, img_file: str, start_coords: tuple[int, int]) -> None:
        self.img                    = np.array(Image.open(img_file))

        # The start coords of the image (top left corner)
        self.start_coords           = start_coords
        self.start_x, self.start_y  = start_coords




def get_canvas():
    """
    Gets the starting canvas we add the images to
    """

    output_img_size = (canvas_y * chunk_size, canvas_x * chunk_size, 4)
    return np.zeros(shape=output_img_size, dtype=np.uint8)



def add_sketch_to_overlay(overlay, sketch: Sketch):
    img                 = sketch.img
    start_x, start_y    = sketch.start_coords

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            pixel = img[y, x]

            # Checks whether pixel is nothing or actually has some colour. If any of the 3 rgb values is non-zero, we don't skip (if all of the values are 0, we skip)
            if not pixel.any():
                # Empty pixel, skip
                continue

            overlay[(start_y + y) * chunk_size + 1, (start_x + x) * chunk_size + 1] = pixel



sketches = [
    Sketch("moderate sketch.png", (1549, 565)),
]


overlay_img = get_canvas()


for sketch in sketches:
    add_sketch_to_overlay(overlay_img, sketch)


finished_img = Image.fromarray(overlay_img)
finished_img.save(finished_file)