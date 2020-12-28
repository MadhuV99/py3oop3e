# tiling_strategy.py
from PIL import Image
import sys

my_img_fldr = r".\my_imgs\\"
my_img_pic = r"tatras"
# my_img_pic = r"mr_mrs"
my_img_format = r".jpg"
my_img_file = my_img_fldr+my_img_pic+my_img_format

class TiledStrategy:
    
    def make_background(self, img_file, desktop_size):
        # in_img = Image.open(img_file)
        try:
            in_img = Image.open(img_file)
        except IOError:
            print("Unable to load image")
            sys.exit(1)
        # in_img.show()

        out_img = Image.new("RGB", desktop_size)
        num_tiles = [
            o // i + 1 for o, i in zip(out_img.size, in_img.size)
        ]
        for x in range(num_tiles[0]):
            for y in range(num_tiles[1]):
                out_img.paste(
                    in_img,
                    (
                        in_img.size[0] * x,
                        in_img.size[1] * y,
                        in_img.size[0] * (x + 1),
                        in_img.size[1] * (y + 1),
                    ),
                )
        return out_img


class CenteredStrategy:
    
    def make_background(self, img_file, desktop_size):
        # in_img = Image.open(img_file)
        try:
            in_img = Image.open(img_file)
        except IOError:
            print("Unable to load image")
            sys.exit(1)
        # in_img.show()

        out_img = Image.new("RGB", desktop_size)
        left = (out_img.size[0] - in_img.size[0]) // 2
        top = (out_img.size[1] - in_img.size[1]) // 2
        out_img.paste(
            in_img,
            (left, top, left + in_img.size[0], top + in_img.size[1]),
        )
        return out_img


class ScaledStrategy:
    
    def make_background(self, img_file, desktop_size):
        # in_img = Image.open(img_file)
        try:
            in_img = Image.open(img_file)
        except IOError:
            print("Unable to load image")
            sys.exit(1)
        # in_img.show()

        out_img = in_img.resize(desktop_size)
        return out_img

def main():
    sy = TiledStrategy()
    # sy = CenteredStrategy()
    # sy = ScaledStrategy()
    desktop_size = (640, 640)
    my_img_bg = sy.make_background(my_img_file, desktop_size)
    my_img_bg.show()

if __name__ == '__main__':
    main() 
