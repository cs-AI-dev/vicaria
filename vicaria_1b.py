print("Vicaria v1.0.0b\nimporting graphics modules ...", end="")
import tqdm
from tqdm import tqdm as graphicLoadingBar
import blessed
from blessed import Terminal

print("done.\nimporting natural language processing modules ...", end="")
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import words
from nltk.book import text1
from nltk.book import text2
from nltk.book import text3
from nltk.book import text4
from nltk.book import text5
from nltk.book import text6
from nltk.book import text7
from nltk.book import text8
from nltk.book import text9
nltk_book_toggles = {
    1: False,
    2: False,
    3: False,
    4: False,
    5: True,#
    6: False,
    7: False,
    8: False,
    9: False
}

allwords = list(words.words())

print("done.\nimporting system modules ...", end="")
import os
from os import mkdir
from os import rmdir
from os import system
from os import getcwd
import sys
from sys import argv
import time
from time import time
from time import sleep

print("done.")

term = Terminal()

prepareData = False

if prepareData:
    print(term.clear())
    [print("") for x in range(int(term.height/2)-3)]

    print(term.center("Vicaria-1 Artificial General Intelligence System"))
    print(term.center("Reloading static system data. This can take several minutes. Standby.\n"))

    for x in graphicLoadingBar(allwords, ascii=" ▏▎▍▌▋▊▉█"):
        try:
            f = open("E:/draco/nlpdata/"+x+".1b.vic", "w")
            f.write("")
            f.close()
            f = open("E:/draco/nlpdata/"+x+".1b.vic", "a")
            f.write("SYNSETS\n")
            for ss in wn.synsets(x):
                f.write(str(ss).split("\'")[1] + "\n")
            f.write("LEMMAS\n")
            for lm in wn.lemmas(x):
                f.write(str(lm).split("\'")[1] + "\n")
            f.write("HYPERNYMS\n")
            for ss in wn.synsets(x):
                for d in ss.hypernyms():
                    f.write(str(ss).split("\'")[1] + ":" + str(d).split("\'")[1] + "\n")
            f.write("HYPONYMS\n")
            for ss in wn.synsets(x):
                for d in ss.hyponyms():
                    f.write(str(ss).split("\'")[1] + ":" + str(d).split("\'")[1] + "\n")
            f.write("MEMBER_HOLONYMS\n")
            for ss in wn.synsets(x):
                for d in ss.member_holonyms():
                    f.write(str(ss).split("\'")[1] + ":" + str(d).split("\'")[1] + "\n")
            f.write("ROOT_HYPERNYMS\n")
            for ss in wn.synsets(x):
                for d in ss.root_hypernyms():
                    f.write(str(ss).split("\'")[1] + ":" + str(d).split("\'")[1] + "\n")
            f.write("ANTONYMS\n")
            for lm in wn.lemmas(x):
                for d in lm.antonyms():
                    f.write(str(lm).split("\'")[1] + ":" + str(d).split("\'")[1] + "\n")
            f.write("DERIVATIONALLY_RELATED_FORMS\n")
            for lm in wn.lemmas(x):
                for d in lm.derivationally_related_forms():
                    f.write(str(lm).split("\'")[1] + ":" + str(d).split("\'")[1] + "\n")
            f.write("PERTAINYMS\n")
            for lm in wn.lemmas(x):
                for d in lm.pertainyms():
                    f.write(str(lm).split("\'")[1] + ":" + str(d).split("\'")[1] + "\n")
            f.write("FRAME_IDS\n")
            for lm in wn.lemmas(x):
                try:
                    f.write(str(lm.frame_ids()[0]) + "/" + str(lm.frame_ids()[1]))
                except IndexError:
                    pass
                except Exception as e:
                    raise e

            f.write("\nEND\n")

            f.close()

            f = open("E:/draco/relations/"+x+".1b.vic", "w")
            f.write("SENTENCES\nSIMILAR\nCOMPONENTS")
            f.close()

            f = open("E:/draco/contexts/"+x+".1b.vic", "w")
            if nltk_book_toggles[1]:
                f.write("")
                i = 0
                for tok in range(len(text1.tokens)):
                    if text1.tokens[tok] == x:
                        f.write(" ".join(text1.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[2]:
                f.write("")
                i = 0
                for tok in range(len(text2.tokens)):
                    if text2.tokens[tok] == x:
                        f.write(" ".join(text2.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[3]:
                f.write("")
                i = 0
                for tok in range(len(text3.tokens)):
                    if text3.tokens[tok] == x:
                        f.write(" ".join(text3.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[4]:
                f.write("")
                i = 0
                for tok in range(len(text4.tokens)):
                    if text4.tokens[tok] == x:
                        f.write(" ".join(text4.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[5]:
                f.write("")
                i = 0
                for tok in range(len(text5.tokens)):
                    if text5.tokens[tok] == x:
                        f.write(" ".join(text5.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[6]:
                tk = text6.tokens
                f.write("")
                i = 0
                for tok in range(len(text6.tokens)):
                    if text6.tokens[tok] == x:
                        f.write(" ".join(text6.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[7]:
                f.write("")
                i = 0
                for tok in range(len(text7.tokens)):
                    if text7.tokens[tok] == x:
                        f.write(" ".join(text7.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[8]:
                f.write("")
                i = 0
                for tok in range(len(text8.tokens)):
                    if text8.tokens[tok] == x:
                        f.write(" ".join(text8.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
            if nltk_book_toggles[9]:
                f.write("")
                i = 0
                for tok in range(len(text9.tokens)):
                    if text9.tokens[tok] == x:
                        f.write(" ".join(text9.tokens[tok-5:tok+6]))
                        i += 1
                f.write(str(i))
        except ValueError:
            print(term.clear())
            [print("") for x in range(int(term.height/2)-4)]
            print(term.center("Vicaria-1 Artificial General Intelligence System"))
            print(term.center("Reloading static system data. This can take several minutes. Standby."))
            print(term.yellow_on_black("ERROR: " + str(x)))
        except Exception as e:
            raise e

print(term.clear())
print(term.center("Vicaria-1 Artificial General Intelligence System"))
print(term.center("System startup complete."))
print(" ╔" + "".join(["═" for x in range(term.width-4)]) + "╗ ")
[print(" ║" + "".join([" " for x in range(term.width-4)]) + "║ ") for x in range(term.height-4)]
print(" ╚" + "".join(["═" for x in range(term.width-4)]) + "╝ ")

dstack = []

def display(txt):
    global dstack
    dstack = dstack[::-1]
    dstack.append(txt)
    dstack = dstack[::-1]
    for x in range(len(dstack)):
        with term.location(3, term.height - (4 + x)): print(dstack[x])

while True:
    cmd_r = ""
    with term.location(3, term.height - 3): print("".join([" " for x in range(75)]))
    with term.location(3, term.height - 3): cmd_r = input("► ")

    display("► " + cmd_r)

    cmd = cmd_r.split(" ")

    name = cmd[0]

    if name == "subsystem":
        if cmd[1] == "info":
            pass
