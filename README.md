# AllenNLP Grammar Classification Guide

This is a forked repository from https://github.com/allenai/allennlp-guide. As such, credits goes to allenai for their code. 
This repository aims to build a text classification model to determine is a sentence is grammatically correct or gramatically incorrect.


## Processing grammar classification dataset

1. Download FCE v2.1, Lang-5 Corpus of Learner English, NUCLE, W&1+LOCNESS v2.1 Dataset from https://www.cl.cam.ac.uk/research/nl/bea2019st/#data.
2. Extract all the contents into allennlp-grammar-classification/quick_start/data/gec


The following are the files that should be extracted from the 4 downloads above and copied into the folder. 

![image](https://user-images.githubusercontent.com/68331483/141755687-a4b163f6-eab9-436a-a817-bef260322d07.png)

3. Delete sample.m2 from the folder above
4. Run the following code
   ```
   python quick_start/data/converter.py
   ```

TODO: Allow argument parser to specify which datasets were used.




## Running model

To be updated

## Results 

To be updated
