import os
import boto3
import argparse
import tarfile

AWS_ACCESS_KEY_ID= os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY= os.getenv("AWS_SECRET_ACCESS_KEY")

class DataLoader:

    def __init__(self, aws_access_key_id: str = AWS_ACCESS_KEY_ID, aws_secret_access_key: str = AWS_SECRET_ACCESS_KEY) -> None:
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
    
    def load_data(self, bucket_key, key_training_dataset, key_dataset_labels, output_data_folder = './data'):

        s3 = boto3.resource(
            's3', 
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )
        bucket = s3.Bucket(bucket_key)
        
        if not os.path.isdir(output_data_folder):
            os.makedirs(output_data_folder)

        car_dataset_labels_path= os.path.join(
            output_data_folder,
            'car_dataset_labels.csv'
        )

        with open(car_dataset_labels_path, 'wb') as data:
            bucket.download_fileobj(key_dataset_labels, data)
        
        training_image_set_path= os.path.join(
            output_data_folder,
            'training_image_set.tgz'
        )

        with open(training_image_set_path, 'wb') as data:
            bucket.download_fileobj(key_training_dataset, data)

        with tarfile.open(training_image_set_path, 'r') as tfile:
            tfile.extractall(path= output_data_folder)
        
        
def parse_args():
    parser = argparse.ArgumentParser(description="Train your model.")
    parser.add_argument(
        "bucket_key",
        type=str,
        help=(
            "Bucket key where data is located. E.g. "
            "`anyoneai-datasets`."
        ),
    )
    parser.add_argument(
        "key_training_dataset",
        type=str,
        help=(
            "Key inside bucket for the training dataset E.g. "
            "`cars196/car_ims.tgz`."
        ),
    )
    parser.add_argument(
        "key_dataset_labels",
        type=str,
        help=(
            "Key inside bucket for the dataset labels." "E.g. `cars196/car_dataset_labels.csv`."
        ),
    )

    args = parser.parse_args()

    return args

def main(bucket_key, key_training_dataset, key_dataset_labels, output_data_folder= './data'):
    """
    Parameters
    ----------
    bucket_key : str
        Bucket key where data is located.

    key_training_dataset : str
        Key inside bucket for the training dataset.

    key_dataset_labels : str
        Key inside bucket for the dataset labels.
    
    output_data_folder : str
        Where to alocate the data retreived.
    
    """
    
    data_loder = DataLoader()
    data_loder.load_data(bucket_key, key_training_dataset, key_dataset_labels)

if __name__ == "__main__":
    args = parse_args()
    main(args.bucket_key, args.key_training_dataset, args.key_dataset_labels, './data')