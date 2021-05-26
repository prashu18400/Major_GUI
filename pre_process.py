import cv2


def pre_process(crop_img):
    img_ = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
    img_ = cv2.resize(img_, (48, 48))  # except for 23 model for all 48,48
    return img_
