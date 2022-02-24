# scripts for online server evaluation 
# https://cocodataset.org/#captions-eval 
# https://cocodataset.org/#format-results 
import json 
import os 

annotation_path = '/Users/feizhengcong/Desktop/COCO/annotations' 
val_image_path = '/Users/feizhengcong/Desktop/COCO/val2014'
val_json = 'captions_val2014.json'
test_image_path = '/Users/feizhengcong/Desktop/COCO/test2014'


val_path = 'captions_val2014_transformer_results.json' 
test_path = 'captions_test2014_transformer_results.json'



def image_name_to_image_id(image_name): 
    image_id = int(image_name.split('_')[2].split('.')[0])
    return str(image_id)


if __name__ == '__main__': 
    val_json_path = os.path.join(annotation_path, val_json) 
    with open(val_json_path, 'r', encoding='utf-8') as f:
        data_dict = json.load(f) 

    val_res = [] 
    test_res = [] 

    # validation set 
    for p in data_dict['annotations']: 
        img_id = p['image_id'] 
        filename = os.path.join(val_image_path, f"COCO_val2014_{int(img_id):012d}.jpg")
        if not os.path.exists(filename): 
            print(filename) 

    test_file_name = os.listdir(test_image_path) 
    for name in test_file_name[:10]: 
        print(name, image_name_to_image_id(name))



