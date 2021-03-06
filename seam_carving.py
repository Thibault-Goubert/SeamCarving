# -*- coding: utf-8 -*-
from PIL import Image
import seam
import seam_treatment

def horizontal_carving(im, img):
    cm = seam.calculate_cost_matrix(img)
    sm = seam.detect_seam(cm)
    im = seam_treatment.remove_seam(im,sm)
    img = seam_treatment.remove_seam(img,sm)
    return (im, img)

def vertical_carving(im,img):
    im = im.rotate(-90, expand=True)
    img = img.rotate(-90, expand=True)
    im, img = horizontal_carving(im,img)
    im = im.rotate(90, expand=True)
    img = img.rotate(90, expand=True)
    return (im, img)

if __name__ == "__main__":
    horizontal_carving(Image.open('1.jpg'), Image.open('1g.jpg'))