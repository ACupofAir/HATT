import os
from tqdm import tqdm

# ! [FIXME]
folder_path = '/home/june/workspace/CDTrans/data/shipsear/target/images/tug'
output_path = '/home/june/workspace/CDTrans/data/shipsear/target_list.txt'


def generate_folder_file_label(folder_path: str, output_path: str, label: str = None) -> None:
    """Create a txt file contain the folder file and label

    Args:
        folder_path (str): the folder path which need to be labeled
        output_path (str): the txt file path
        label (str): the label name
    """

    if not os.path.isdir(folder_path):
        raise ValueError('Not a valid folder path')
    if label == None:
        label = os.path.basename(folder_path)

    for file_name in tqdm(os.listdir(folder_path)):
        with open(output_path, 'a') as output_file:
            file_path = os.path.join(folder_path, file_name)
            print(f'{file_path} {label}', file=output_file)


if __name__ == '__main__':
    generate_folder_file_label(folder_path, output_path)