import numpy as np
from PIL import Image

DIMENSIONS = 3


class Canvas:
    def __init__(self, size: tuple, color: tuple):
        self.width = size[1]
        self.height = size[0]
        self.color = color

        self.data = np.zeros((self.height, self.width, DIMENSIONS), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path: str):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)
