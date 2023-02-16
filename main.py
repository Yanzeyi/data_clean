from pycocotools.coco import COCO
import os


def coco2yolo(x, y, w, h, img_w, img_h):
    """
    :param x:       float       目标检测框左上点横坐标
    :param y:       float       目标检测框左上点纵坐标
    :param w:       float       目标检测框宽度
    :param h:       float       目标检测框高度
    :param img_w:   float       图片宽度
    :param img_h:   float       图片高度
    :return:        float       检测框中心坐标以及长宽
    """
    x1, y1, x2, y2 = x, y, int(x + w), int(y + h)
    x_o, y_o, w, h = ((x2 - x1) / 2 + x1) / img_w, ((y2 - y1) / 2 + y1) / img_h, w / img_w, h / img_h
    return round(x_o, 6), round(y_o, 6), round(w, 6), round(h, 6)


def getlabel(img_id, cat_id):
    """                 type
    :param img_id:      int     图片ID
    :param cat_id:      int     种类ID
    :return:            str     单个图片的符合种类ID的所有标签
    """
    label = ''
    ann_ids = coco.getAnnIds(imgIds=img_id)
    targets = coco.loadAnns(ann_ids)
    imgInfo = coco.loadImgs(img_id)[0]
    img_h, img_w = imgInfo['height'], imgInfo['width']
    for target in targets:
        if target["category_id"] != cat_id:
            continue
        x, y, w, h = target["bbox"]
        x_o, y_o, w, h = coco2yolo(x, y, w, h, img_w, img_h)
        label = label + str(x_o) + ' ' + str(y_o) + ' ' + str(w) + ' ' + str(h) + '\n'
    return label


def for2back(path):
    file_path = ''
    path_list = list(path)
    for i in range(len(path_list)):
        if path_list[i] == '\\':
            path_list[i] = '/'
    for i in range(len(path_list)):
        file_path = file_path + path_list[i]
    return file_path


def if12(img_name):
    """
    :param img_name:    int     图片id
    :return:            str     补零
    """
    file_name = ''
    num0 = 12 - len(str(img_name))
    for i in range(num0):
        file_name = file_name + '0'
    file_name = file_name + str(img_name)
    return file_name


def one_pic_label_write(img_id, cat_id, file_path):
    label = getlabel(img_id, cat_id)
    path = os.path.join(file_path, if12(img_id) + '.txt')
    if label != '':
        with open(path, "w+") as f:
            f.write(label)


def muti_pic_label_write(file_path):
    # cat_id = coco.getCatIds('sheep')
    cat_id = 20
    img_ids = coco.getImgIds(catIds=cat_id)
    # img_test = img_ids[:2]
    for img_id in img_ids:
        one_pic_label_write(img_id, cat_id, file_path)
        # print(img_id)


if __name__ == '__main__':
    annotation_path = r"C:\Users\yanzeyi\Downloads\annotations_trainval2017\annotations\instances_train2017.json"
    coco = COCO(annotation_path)
    muti_pic_label_write(r'C:\Users\yanzeyi\Desktop\test')


