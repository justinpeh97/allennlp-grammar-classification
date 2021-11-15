import argparse
import copy
import os
import random

# Apply the edits of a single annotator to generate the corrected sentences.

files = os.listdir('gec_raw')
files.remove('A.train.gold.bea19.m2')
files.remove('B.train.gold.bea19.m2')
files.remove('C.train.gold.bea19.m2')
files.remove('A.dev.gold.bea19.m2')
files.remove('B.dev.gold.bea19.m2')
files.remove('C.dev.gold.bea19.m2')
files.remove('N.dev.gold.bea19.m2')



sentences = []


print("Processing files")

for file in files:
        m2 = open('gec_raw/' + file, encoding="cp437").read().strip().split("\n\n")
        # Do not apply edits with these error types
        skip = {"noop", "UNK", "Um"}

        for sent in m2:
                sent = sent.split("\n")
                original_sent = sent[0].split()[1:] # Ignore "S "
                cor_sent = copy.deepcopy(original_sent)
                edits = sent[1:]
                offset = 0
                for edit in edits:
                        edit = edit.split("|||")
                        if edit[1] in skip: continue # Ignore certain edits
                        coder = int(edit[-1])
                        if coder != 0: continue # Ignore other coders
                        span = edit[0].split()[1:] # Ignore "A "
                        start = int(span[0])
                        end = int(span[1])
                        cor = edit[2].split()
                        cor_sent[start+offset:end+offset] = cor
                        offset = offset-(end-start)+len(cor)

                if cor_sent != original_sent:
                        if len(cor_sent) <= 1 or len(original_sent) <= 1:
                                pass
                        else:
                                sentences.append(" ".join(original_sent) + "\t" + "Incorrect")
                                sentences.append(" ".join(cor_sent)+ "\t" + "Correct")

print("Shuffling and splitting sentences")
random.shuffle(sentences)
split1 = int(len(sentences) * 0.7)
split2 = int(len(sentences) * 0.85)
train = sentences[:split1]
dev = sentences[split1:split2]
test = sentences[split2:]

textfile = open("gec_processed/train.txt","w",encoding = "utf-8")
for element in train:
        textfile.write(element + "\n")
textfile.close()
print("output: train.txt")

textfile = open("gec_processed/test.txt","w",encoding = "utf-8")
for element in test:
        textfile.write(element + "\n")
textfile.close()
print("output: test.txt")


textfile = open("gec_processed/dev.txt","w",encoding = "utf-8")
for element in dev:
        textfile.write(element + "\n")
textfile.close()
print("output: dev.txt")

