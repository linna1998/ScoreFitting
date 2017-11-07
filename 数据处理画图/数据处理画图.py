from __future__ import print_function
import os
import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')  
from matplotlib import pyplot as plt

DIR = 'L:/学术/大三/语言统计分析/高考分数段统计/Mymark_20171102/all/'
FIG_DIR = 'L:/学术/大三/语言统计分析/高考分数段统计/Figure/'


for name in sorted(os.listdir(DIR)):
    path = os.path.join(DIR, name)
    title=name
    f = open(path, encoding='UTF-8')
    score = []
    num = []
    isFirst = 1
    for line in f:       
         if isFirst==0:                          
             if len(line.split('\t'))>1:
                 if len((line.split('\t', 2))[0])>0:
                     score.append(int(line.split('\t', 2)[0]))
                 if len((line.split('\t', 2))[1])>0:
                     num.append(int(line.split('\t', 2)[1]))
             if len(line.split(','))>1:
                 if len((line.split(',', 2))[0])>0:
                     score.append(int(line.split(',', 2)[0]))
                 if len((line.split(',', 2))[1])>0:
                     num.append(int(line.split(',', 2)[1]))
         else:
            isFirst=0
            #title=line
    f.close()
    plt.figure()
    plt.title(title)
    plt.plot(score, num)
    plt.xlabel('score')
    plt.ylabel('num')
    plt.show()
    plt.savefig(FIG_DIR + title.split('.', 2)[0] + '.png')
    plt.close()

