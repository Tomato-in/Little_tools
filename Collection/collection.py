'''
@Author: Michael 2022-12-05 19:26:59
This code is about homework collecting.

'''

import pandas as pd
import wget

class GetData(object):
    def __init__(self, person):
        self.name = person[1]
        self.id   = person[2]
        self.url  = person[3]
        self.getfile()
    def getfile(self):
        wget.download(self.url, out = f'{self.id}-{self.name}.docx')

def main():
    path = input('请输入表格文件地址：')
    data = pd.read_excel(path)
    for i in range(len(data)):
        print(f'正在处理第{i+1}/{len(data)}个')
        GetData(data.loc[i])
        print('\n')

main()