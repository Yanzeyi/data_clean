from pycocotools.coco import COCO
from main import if12

path = r'C:\Users\yanzeyi\Desktop\新建文本文档.txt'
annotation_path = r"C:\Users\yanzeyi\Downloads\annotations_trainval2017\annotations\instances_train2017.json"

coco = COCO(annotation_path)
cat_id = 20
img_ids = coco.getImgIds(catIds=cat_id)

with open(path, "w+") as f:
    for img_id in img_ids:
        mess = if12(img_id)
        mess = 'data' + '/' + 'img' + '/' + mess + '.jpg' + '\n'
        f.write(mess)