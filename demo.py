# coding:utf-8

from distutils.util import change_root
import os
from tracemalloc import stop
import chnSegment
import plotWordcloud
import string


if __name__=='__main__':

    # 读取需绘制词云的文本文件
    text = open('doc//背影.txt', encoding='utf-8').read()

    # 若是中文文本，则先进行分词操作
    text=chnSegment.word_segment(text)

    #获取停用词和特定词
    stopwords = []
    with open('stopwords.txt', 'r') as f:
        for stopword in f.readlines():
            stopwords.append(stopword.strip())          # 读取每行的去停用词的时候需要把后面的换行去除，否则下面循环匹配去停用词的时候，根本都匹配不上

    stopwords_order = ['北京']

    stopwords = stopwords + stopwords_order


    changedWords = {'走':'去',       #需要显示的特定词进行替换
                    '送':'来'}

    #去除停用词；替换特定词
    text_wordSegment = text.split(' ')    
    seg_list = ''
    for word in text_wordSegment:
        for key, value in changedWords.items():
            if word in key:
                word = value
        
        if word not in stopwords:
            seg_list=seg_list + " " + word
        
    # 生成词云
    plotWordcloud.generate_wordcloud(seg_list)
