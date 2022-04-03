"""
The point of this program is to turn a normal image into an overlay image which can be used for r/place.

It loads the sketches given in the sketches list and places them on the canvas/overlay, always leaving 2 empty and transparent spaces between each pixel (both horizontally and veritcally)
"""
from PIL import Image
import numpy as np



class Sketch:
    """
    Represents a sketch, in this case a sketch is an image that is placed at a certain coordinate
    """
    def __init__(self, img_file: str, start_coords: tuple[int, int]) -> None:
        self.img                    = np.array(Image.open(img_file))

        # The start coords of the image (top left corner)
        self.start_coords           = start_coords
        self.start_x, self.start_y  = start_coords



# Only thing you should have to change for a regular update
sketches = [
    Sketch("Dani_face_place.png", (1578, 637)),
]





# Constants
# These variables should not change under normal circumstances

canvas_x, canvas_y = (2000, 1000)

# The size of pixels that make up one pixel on the canvas
# In this case one pixel on the canvas is represented by a 3x3 chunk, with all the outer pixels being empty and only the center pixel holding the actual value
chunk_size = 3

finished_file = "dani_place_overlay.png"





def get_canvas():
    """
    Gets the starting canvas we add the images to
    """

    output_img_size = (canvas_y * chunk_size, canvas_x * chunk_size, 4)
    return np.zeros(shape=output_img_size, dtype=np.uint8)



def add_sketch_to_overlay(overlay, sketch: Sketch):
    """
    Adds the sketch to the image
    """
    img                 = sketch.img
    start_x, start_y    = sketch.start_coords

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            pixel = img[y, x]

            # Check the opacity of the pixel
            # If the pixel opacity is below 20 (randomly chosen) we ignore the pixel since it's basically invisible
            if pixel[3] < 20:
                # Empty pixel, skip
                continue

            # add the pixel to the overlay, but only in the middle pixel out of the 9 (since the pixel is actually made up of a 3x3 pixel chunk)
            overlay[(start_y + y) * chunk_size + 1, (start_x + x) * chunk_size + 1] = pixel



overlay_img = get_canvas()



for sketch in sketches:
    add_sketch_to_overlay(overlay_img, sketch)


# Numpy arry to pillow image
finished_img = Image.fromarray(overlay_img)
finished_img.save(finished_file)