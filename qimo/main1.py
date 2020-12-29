from PIL import Image
from numpy import *
def hash(img1, img2):
    img1 = array(Image.open(img1).convert('L').resize((8, 8)))
    img2 = array(Image.open(img2).convert('L').resize((8, 8)))
    n1 = n2 = 0
    for i in range(8):
        for j in range(8):
            n1 += img1[i][j]
            n2 += img2[i][j]
    n1 = n1 / 64
    n2 = n2 / 64
    han = 0
    for i in range(8):
        for j in range(8):
            if img1[i][j] < n1:
                img1[i][j] = 0
            else:
                img1[i][j] = 1
            if img2[i][j] < n2:
                img2[i][j] = 0
            else:
                img2[i][j] = 1
            if img1[i][j] != img2[i][j]:
                han += 1
    return han


if __name__ == '__main__':
    img1 ='dog.jpg'
    img2 ='dog1.jpg'
    print("两图片汉明距离为")
    print(hash(img1, img2))