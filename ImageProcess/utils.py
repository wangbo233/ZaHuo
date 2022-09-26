import numpy as np
from skimage import transform, io
import os

IMG_KINDS = ('png', 'jpeg')


def read_img(img_path):
    img = io.imread(img_path)
    print(img.shape)
    return img


def read_imgs(root_path):
    name_list = [name for name in os.listdir(root_path) if name.split('.')[-1] in ('png', 'jpeg')]
    img_list = []
    for name in name_list:
        img_list.append(read_img(root_path + '/' + name))
    return img_list


def resize(img, size):
    img = transform.resize(img, size)
    print(img.shape)
    return img


def resize_imgs(img_list, size):
    resized_img_list = []
    for img in img_list:
        img = transform.resize(img, size)
        img = (img*255.0).astype('uint8')
        resized_img_list.append(img)
    return resized_img_list


def concat(img_list, start_idx, rows, cols):
    img_cols = []
    for i in range(0, rows):
        img_to_concat = img_list[start_idx + i * cols:start_idx + (i + 1) * cols]
        img_cols.append(np.concatenate(img_to_concat, axis=0))
    final_img = np.concatenate(img_cols, axis=1)
    return final_img


def save(path, img):
    io.imsave(path, img)
