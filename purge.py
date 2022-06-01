import tqdm
import os

for f in tqdm.tqdm(os.listdir("E:/draco/nlpdata"), desc="(1/4)", ascii="█ "):
    try:
        os.remove("E:/draco/nlpdata/"+f)
    except Exception as e:
        print("Error occurred during purge: " + str(e))

for f in tqdm.tqdm(os.listdir("E:/draco/relations"), desc="(2/4)", ascii="█ "):
    try:
        os.remove("E:/draco/relations/"+f)
    except Exception as e:
        print("Error occurred during purge: " + str(e))

for f in tqdm.tqdm(os.listdir("E:/draco/contexts"), desc="(3/4)", ascii="█ "):
    try:
        os.remove("E:/draco/contexts/"+f)
    except Exception as e:
        print("Error occurred during purge: " + str(e))

for f in tqdm.tqdm(os.listdir("E:/draco/ngrams"), desc="(4/4)", ascii="█ "):
    try:
        os.remove("E:/draco/ngrams/"+f)
    except Exception as e:
        print("Error occurred during purge: " + str(e))
