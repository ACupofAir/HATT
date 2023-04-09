# HATT
hydroacoustic-transformer-transfer, using domain adpat based transformer to classify hydroacoustic

## :railway_track: roadmap
1. orginal input to specgram image: audio file(*.wav) -> image format(*.png)
    * [ ] split long audio to several seconds
    * [ ] convert audio to png file
2. put image to the CDTrans network and grenerate model
3. verfiy the model
## :toolbox: code usage
### utils
* `audio2specgram`: convert audio to specgram
### data
* `split_audio`: convert audio to specgram