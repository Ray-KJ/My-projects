"""
File: blur.py
Name: Ray
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, the image to be processed/blurred. The blur algorithm blurs each pixel by averaging the RGB figure
    of all adjacent pixels
    :return: img, the image after blurred.
    """
    new_w = img.width
    new_h = img.height
    new_img = SimpleImage.blank(new_w, new_h)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            new_pixel = new_img.get_pixel(x, y)
            red = 0
            green = 0
            blue = 0
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            
            if x == 0 and y == 0:
                for i in range(0, 2):
                    for j in range(0, 2):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4

            elif x == img.width-1 and y == 0:
                for i in range(-1, 1):
                    for j in range(0, 2):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4

            elif x == 0 and y == img.height-1:
                for i in range(0, 2):
                    for j in range(-1, 1):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4

            elif x == img.width-1 and y == img.height-1:
                for i in range(-1, 1):
                    for j in range(-1, 1):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 4
                new_pixel.green = green // 4
                new_pixel.blue = blue // 4
 
            elif 0 < x < img.width-1 and y == 0:
                for i in range(-1, 2):
                    for j in range(0, 2):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6

            elif 0 < x < img.width-1 and y == img.height-1:
                for i in range(-1, 2):
                    for j in range(-1, 1):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6

            elif x == 0 and 0 < y < img.height-1:
                for i in range(0, 2):
                    for j in range(-1, 2):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6

            elif x == img.width-1 and 0 < y < img.height-1:
                for i in range(-1, 1):
                    for j in range(-1, 2):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 6
                new_pixel.green = green // 6
                new_pixel.blue = blue // 6

            else:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        old_pixel = img.get_pixel(x+i, y+j)
                        red += old_pixel.red
                        green += old_pixel.green
                        blue += old_pixel.blue
                new_pixel.red = red // 9
                new_pixel.green = green // 9
                new_pixel.blue = blue // 9
    return new_img


def main():
    """
    This program first shows the original image. And then the program shows the blurred image of the original image
    after the original image has been processed through function blur.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
