from utils import read_imgs, resize_imgs, save, concat

if __name__ == '__main__':
    root_path = '/Users/wangbo/Desktop/改后照片/改后照片'
    img_size = (413, 295, 4)
    rows, cols = 5, 5
    img_list = read_imgs(root_path)
    imgs = resize_imgs(img_list, img_size)
    img = concat(imgs, 0, rows, cols)
    save('/Users/wangbo/Desktop/改后照片/final.png', img)
