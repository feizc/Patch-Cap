# scripts for online server evaluation 
import json 
import os 

annotation_path = '/Users/feizhengcong/Desktop/COCO/annotations' 
image_path = '/Users/feizhengcong/Desktop/COCO/val2014'
train_json = 'captions_val2014.json'




if __name__ == '__main__': 
    train_json_path = os.path.join(annotation_path, train_json) 
    with open(train_json_path, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)  
    for p in data_dict['annotations']: 
        img_id = p['image_id']
        filename = os.path.join(image_path, f"COCO_val2014_{int(img_id):012d}.jpg")
        if not os.path.exists(filename): 
            print(filename)


