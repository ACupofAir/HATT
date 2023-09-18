# HATT
hydroacoustic-transformer-transfer, using domain adpat based transformer to classify hydroacoustic

## :railway_track: roadmap
1. orginal input to specgram image: audio file(*.wav) -> image format(*.png)
    * [ ] split long audio to several seconds
    * [ ] convert audio to png file
2. put image to the CDTrans network and grenerate model
3. verfiy the model
## :toolbox: code usage
1. `split_frame.py`: split big audio file to smaller and more
2. `split_img_folder.py`: split these small audio file folder to source and target folder

### example to create dataset for source and target
* split frame
    1. `data_config.json`: config your source and target audio folder path. The directory structure should look like the following.
        * `directory`: the directory will store the spectrograms generate by the program
        * `audio_path`: the directory store audio files which will be convert to spectrograms
        ```bash
        DeepShip
        └── DeepShip_audio
            ├── Cargo
            │   ├── 103.wav
            │   ├── 110.wav
            ├── Passengership
            │   ├── 1.wav
            │   ├── 12.wav
            ├── Tanker
            │   ├── 10.wav
            │   ├── 12.wav
            ...
        ```
    2. `split_frame.py` -> `FIXME`, change the directory and method in the file, and generate mel images folder after running this script
    ```python
    # run in HATT
    cd data
    python split_frame.py
    ```
* link the dataset to the cdtrans net
    ```bash
    ln -s /mnt/d/workspace/dataset/deepship_source/mel data/shipsear/source/images
    ln -s /mnt/d/workspace/dataset/shipears_target/mel data/shipsear/target/images
    ```
* generate label list for dataset
    * `generate_label.py` -> FIXME: change the folder_path, output_path
    * run the `python generate_label.py` command in the `HATT/data` directory

### utils
* `audio2specgram`: convert audio to specgram
### data
* `split_audio`: convert audio to specgram