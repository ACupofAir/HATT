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
* split frame: `split_frame.py` -> FIXME, change the directory in the file, and generate mel images folder after running this script
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