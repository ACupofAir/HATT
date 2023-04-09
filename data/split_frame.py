#%%
import os
import sys
import configparser

sys.path.append('..')
from utils import audio2spectrogram

# * get all need split file name
config = configparser.ConfigParser()
config.read('../config.ini')

shipeat_directory = config.get('dataset', 'shipeat_directory')
shipeat_audio_directory = os.path.join(shipeat_directory, 'audio_source')
method = 'mel'

class_directories = os.listdir(shipeat_audio_directory)
class_directories_full_path = []
for directory in class_directories:
    class_directories_full_path.append(os.path.join(shipeat_audio_directory, directory))


#%%
# * create directory to store convert image
shipeat_img_dir = os.path.join(shipeat_directory, method)
if not os.path.exists(shipeat_img_dir):
    os.mkdir(shipeat_img_dir)
for class_name in class_directories:
    class_img_dir = os.path.join(shipeat_img_dir, class_name)
    if not os.path.exists(class_img_dir):
        os.mkdir(class_img_dir)


# %%
# * split audio and convert it to spec store it in the shipeat_img_dir
for class_audio_dir in class_directories_full_path:
    for audio_file in class_audio_dir:
        # ! todo tomorrow