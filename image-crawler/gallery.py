from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt

def gallery(array, ncols=5):
    nindex, height, width, intensity = array.shape
    nrows = nindex//ncols
    assert nindex == nrows*ncols
    result = (array.reshape(nrows, ncols, height, width, intensity)
              .swapaxes(1,2)
              .reshape(height*nrows, width*ncols, intensity))
    return result

augimglist = glob.glob(r'C:/Users/82103/Desktop/Github/crawler/img/1620*.png')
imlist = []
for img in augimglist:
    im = Image.open(img)
    imlist.append(np.asarray(im))
imlist = np.array(imlist)
img = Image.fromarray(gallery(imlist))
img.save(r"C:/Users/82103/Desktop/Github/crawler/img/aumented.png")