import numpy as np;
from PIL import Image, ImageDraw;

gray = np.array([0.299, 0.587, 0.114]);

def _get_image_data(image):
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    return draw, width, height, pix

def _get_gray_pix(pix, i, j):
    if type(pix) == int:
        pix = (pix, pix, pix)
    return sum(pix[i, j][:]) // 3

def bw(colour, bw):
    draw, width, height, pix = _get_image_data(colour)

    for i in range(width):
        for j in range(height):
            s = _get_gray_pix(pix, i, j)
            draw.point((i, j), (s, s, s))
    colour.save(bw)
    del draw
    return np.array(colour)

def bw_NP(colour, bw):
    arr_pic = np.asarray(colour)
    grayscale_image = np.dot(arr_pic[..., :3], gray)
    new_pic = Image.fromarray(grayscale_image)
    new_pic = new_pic.convert('RGB')
    new_pic.save(bw)
    return np.array(new_pic)

def bw_vec(colour, bw):
    draw, width, height, pix = _get_image_data(colour)

    [[draw.point((i, j), (_get_gray_pix(pix, i, j), _get_gray_pix(pix, i, j), _get_gray_pix(pix, i, j)))
      for j in range(height)] for i in range(width)]
    colour.save(bw)
    del draw
    return np.array(colour)

nonvec_pic, vec_pic, np_pic = "pics/nonec.jpg", "pics/vec.jpg", "pics/np.jpg"
orig_pic = Image.open("pics/unnamed.jpg")
m1 = bw(orig_pic, nonvec_pic)
m2 = bw_vec(orig_pic, vec_pic)
m3 = bw_NP(orig_pic, np_pic)
print(m1)
print(m2)
print(m3)
