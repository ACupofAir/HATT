# %%
import os
import sys
import configparser
from tqdm import tqdm

sys.path.append("..")
from spec_utils import audio2specfile, split_frame_by_file

# * get all need split file name
config = configparser.ConfigParser()
config.read("../config.ini")

# ! [FIXME]: change to the dataset directory path you needed
# shipeat_directory = config.get('dataset', 'shipeat_directory')
dataset_directory = config.get("dataset", "deepship_directory")
dataset_audio_directory = config.get("dataset", "deepship_audio_source")
method = "mel"

audio_class_names = os.listdir(dataset_audio_directory)

dataset_img_dir = os.path.join(dataset_directory, method)
if not os.path.exists(dataset_img_dir):
    os.mkdir(dataset_img_dir)
# %%
# * split audio and convert it to spec store it in the shipeat_img_dir
for class_name in audio_class_names:
    #  create directory to store convert image
    class_img_dir = os.path.join(dataset_img_dir, class_name)
    if not os.path.exists(class_img_dir):
        os.mkdir(class_img_dir)

    audio_class_path = os.path.join(dataset_audio_directory, class_name)
    frame_idx = 0

    print(
        f"------------------------------convert {class_name} to audio------------------------------"
    )
    for file_name in tqdm(os.listdir(audio_class_path)):
        split_num = 0
        audio_file_path = os.path.join(audio_class_path, file_name)
        splited_frames, sr = split_frame_by_file(
            frame_size=5, frame_shift=2.5, audio_file=audio_file_path
        )
        print(
            f"------------------------------convert {class_name}/{file_name} to"
            " audio------------------------------"
        )
        for frame in tqdm(splited_frames):
            saved_path = os.path.join(dataset_img_dir, class_name, str(frame_idx) + ".png")
            frame_idx += 1
            audio2specfile(audio_data=frame, sr=sr, saved_path=saved_path)
