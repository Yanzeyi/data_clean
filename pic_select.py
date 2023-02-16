import os
import shutil
from pycocotools.coco import COCO

old_path = r'D:\train2017\train2017'
new_path = r'C:\Users\yanzeyi\Desktop\新建文件夹 (3)'
pic_list = os.listdir(old_path)
annotation_path = r"C:\Users\yanzeyi\Downloads\annotations_trainval2017\annotations\instances_train2017.json"

coco = COCO(annotation_path)
img_ids = coco.getImgIds(catIds=20)

for i in range(len(pic_list)):
    name = pic_list[i]
    for j in range(12):
        if name[j] == '0':
            continue
        img_id = name[j-16:].split('.')[0]
        break
    if int(img_id) in img_ids:
        shutil.copy(os.path.join(old_path, name), new_path)


