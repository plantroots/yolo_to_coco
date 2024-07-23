Step 1: Convert YOLO to VOC Format
Place the data you want to convert in the current directory.
Create a folder named Annotations in the current directory.
Modify the path in the main function of yolotovoc.py to match your directory structure.
Run yolotovoc.py. Upon successful execution, corresponding XML files in VOC format will be generated in the Annotations folder.
Step 2: Convert VOC to COCO Format
Copy all images into the Annotations folder.
In voctococo.py, the train_ratio variable controls the ratio of training to validation data. Setting train_ratio to 1 will generate all data as training data.
Run voctococo.py to complete the conversion.
