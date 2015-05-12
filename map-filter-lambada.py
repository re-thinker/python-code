#!/usr/bin/env python

import os

def find_filter_files(dir_list, name):
    found_file_list = []
    # 对指定目录(dirname）处理，该目录下的文件和子目录都在list_of_dir列表里，
    # 处理（包括过滤子目录和过滤一些文件）后的结果保存到found_file_list里    
    # 0）使用lambda定义一个简单的合成完整路径的匿名函数，其中a就是list_of_dir中的元素    
    # 1）map用来将list_of_dir列表里的所有元素加上完整路径名    
    # 2）第二个filter用来过滤掉所有的子目录    
    # 3）第一个filter用来过滤掉不符合后缀名条件的文件    
    # 4）最后通过extend将符合条件的文件存放到found_file_list列表里    
    
    def filter_name_func(found_file_list, dirname, list_of_dir):
        found_file_list.extend(\
            filter(lambda a : os.path.splitex(a)[1] in name,\
                   filter(os.path.isfile,\
                          map(lambda a : os.path.join(dirname, a), list_of_dir))))
    
    def func(one_dir):    
        # path.walk对一个目录做处理，
        # 对该目录下的每个子目录和文件都会调用
        # filter_name_func做处理，
        # 对目录的每个子目录又会递归如上的处理。 
        
        os.path.walk(one_dir, filter_name_func, found_file_list)
    
    # 遍历dir_list列表，以每一个元素（比如dir1目录）
    # 作为入参去调用函数func    
    map(func, dir_list)    
    return found_file_list    

def find_filter_files_2(dir,name):

    found_file_list = []

    # 将每个需要处理的目录（parent_dirname)下的文件和子目录区分对待
    # 文件列表存放到list_of_dir里，子目录列表存放在dirname里
    # 其它部分代码参考jsj_xx_1.py即可

    for parent_dirname,dirname,list_of_dir in os.walk(dir):    
      found_file_list.extend(\
          filter(lambda a: os.path.splitext(a)[1] in name,\
                 filter(os.path.isfile,\ 
                        map(lambda a: os.path.join(parent_dirname, a), list_of_dir))))

    return found_file_list



