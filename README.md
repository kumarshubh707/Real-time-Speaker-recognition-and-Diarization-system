# Real time Speaker diarization & Speaker recognition for online exam proctoring system.

This project contains:
* Text-independent Speaker recognition module based on VGG-Speaker-recognition
* Speaker diarization based on UIS-RNN.</br>

## Prerequisites
1. pytorch
2. keras
3. Tensorflow
4. pyaudio (About how to install on windows, refer to [pyaudio_portaudio](https://github.com/intxcc/pyaudio_portaudio))

## Outline

Their paper can refer to [UTTERANCE-LEVEL AGGREGATION FOR SPEAKER RECOGNITION IN THE WILD](https://arxiv.org/pdf/1902.10107.pdf)</br>
It's a novel idea that combines `netvlad/ghostvlad` which popularly used in image recognition to speaker recognition, the state-of-the-art in the past was `i-vector` based, which depended on the `GMM` model and `pLDA`.

About VGG speaker model, I have re-implemented in tensorflow, [ghostvlad-speaker](https://github.com/taylorlu/ghostvlad-speaker) and corresponding pretrained model.

This project only shows how to generate speaker embeddings using pre-trained model for uis-rnn training.</br>
 
### 2. Speaker diarization.</br>
![diarization](https://github.com/taylorlu/Speaker-Diarization/blob/master/resources/diarization.gif)

#### Clustering
`python main.py`

The Result is showing as below:(3 speakers)

    ========= 0 =========
    0:00.288 ==> 0:04.406
    0:07.699 ==> 0:16.461
    0:33.921 ==> 0:35.8
    ========= 1 =========
    0:04.406 ==> 0:07.699
    0:16.461 ==> 0:19.594
    0:30.371 ==> 0:33.921
    0:41.19 ==> 0:44.185
    ========= 2 =========
    0:19.594 ==> 0:30.371
    0:35.8 ==> 0:41.19

The final result is influenced by the size of each window and the overlap rate.
