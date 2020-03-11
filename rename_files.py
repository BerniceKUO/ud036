# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 07:59:47 2020

@author: 1300183
"""

import os
path=r"C:\prank\prank";
def rename_files():
    file_list=os.listdir(path)
    print(file_list)
    for fileName in file_list:
      # os.rename(os.path.join(path, fileName),fileName.translate(str.maketrans("","","1234567890")))
       os.rename(os.path.join(path,fileName),os.path.join(path,fileName.translate(str.maketrans("","","1234567890"))))
    
rename_files()