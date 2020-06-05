# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:55:07 2020

@author: HP
"""
# 2020年5月24日

def find_file(path,pattern):
    '''
    通过输入的指定目录，和指定的模式。
    递归搜素目录下所有符合要求的文件，并返回文件的绝对路径。
    '''
    import fnmatch
    import os 
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            paths = os.path.join(path, file)
            find_file(paths, pattern)
        else :
            if fnmatch.fnmatch(file, pattern):
               pa = os.path.abspath(os.path.join(file))
               print(pa)
            
# 测试函数是否正确 
path = input('请输入指定文件路径：')
pattern = input('请输入特定模式：')
#'D:\Python project\竞赛文件','*.py'
find_file(path, pattern)