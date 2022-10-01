import cv2
import matplotlib.pyplot as plt
import numpy as np
import colorsys
import argparse


def bgr_2_hsv(b, g, r) -> []:
    b, g, r = b / 255, g / 255, r / 255
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return [np.int32(np.round(h * 179)), np.int32(np.round(s * 255)), np.int32(np.round(v * 255))]


def show_img_and_title(image: np.ndarray, title=None):
    plt.axis('off')
    if title is not None:
        plt.title(title)
    plt.imshow(image)
    plt.show()


def ret_img_and_img_hsv(img_path: str):
    img = cv2.imread(img_path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return img, img_hsv


parser = argparse.ArgumentParser()
parser.add_argument('-r', required=True)
parser.add_argument('-g', required=True)
parser.add_argument('-b', required=True)

parser.add_argument('-p', required=True)

parser.add_argument('-d', required=False)
args = parser.parse_args()

r = int(args.r)
g = int(args.g)
b = int(args.b)
file_path = args.p
delta = 0.05

if args.d:
    delta = float(args.d)

h, s, v = bgr_2_hsv(b, g, r)

img, img_hsv = ret_img_and_img_hsv(file_path)

hsv_mask = cv2.inRange(img_hsv, (int(h * (1 - delta)), int(s * (1 - delta)), 0),
                       (int(min(h * (1 + delta), 179)), int(min(s * (1 + delta), 255)), 255))

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_mask_rgb = cv2.cvtColor(hsv_mask, cv2.COLOR_BGR2RGB)
plt.imsave(file_path.split(".")[0] + "_mask" + ".jpg", arr=cv2.cvtColor(hsv_mask, cv2.COLOR_BGR2RGB))
plt.imsave(file_path.split(".")[0]+ "_masked"+".jpg", cv2.bitwise_and(img, img, mask=hsv_mask))
