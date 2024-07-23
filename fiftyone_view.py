import fiftyone as fo


dataset_dir = "."

dataset = fo.Dataset.from_dir(
    dataset_dir=dataset_dir,
    dataset_type=fo.types.COCODetectionDataset,
    data_path="dataset/data",
    labels_path="dataset/annotations/train.json",
)

print(dataset.head())

# Connect to the existing FiftyOne session
session = fo.launch_app()

# Add the dataset to the session
session.dataset = dataset
session.wait()
