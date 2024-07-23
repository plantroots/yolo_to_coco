### >fiftyone app launch ###

import fiftyone as fo


dataset_dir = "."

# Create the dataset
dataset = fo.Dataset.from_dir(
    dataset_dir=dataset_dir,
    dataset_type=fo.types.COCODetectionDataset,
    data_path="dataset/data",
    labels_path="dataset/annotations/train.json",
)

# View summary info about the dataset
print(dataset)
# Print the first few samples in the dataset
print(dataset.head())

# Connect to the existing FiftyOne session
session = fo.launch_app()

# Add the dataset to the session
session.dataset = dataset
session.wait()
