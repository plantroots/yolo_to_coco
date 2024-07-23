import fiftyone as fo


IMAGES_DIR = "/home/plantroot/Code/yolo_to_coco/images/train2014"
LABELS_DIR = "/home/plantroot/Code/yolo_to_coco/instances_train2014.json"

dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=IMAGES_DIR,
    labels_path=LABELS_DIR,
)

print(dataset.head())

# Connect to the existing FiftyOne session
session = fo.launch_app()

# Add the dataset to the session
session.dataset = dataset
session.wait()
