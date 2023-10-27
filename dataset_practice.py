from torch.utils.data import Dataset
import pandas as pd
import os

class MyData(Dataset):
    """Data数据集类，包含读取文件函数以及获得数据量函数
    输入项为主路径以及副路径
    getitem函数可读取数据以及数据标签
    len函数获得该路径下数据量"""
    def __init__(self,root_dir,label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir,self.label_dir)
        self.excel_path = os.listdir(self.path)
    def __getitem__(self, idx):
        excel_name = self.excel_path[idx]
        excel_item_path = os.path.join(self.root_dir,self.label_dir,excel_name)
        excel = pd.read_excel(excel_item_path,index_col=None)
        label = self.label_dir
        return excel,label

    def __len__(self):
        return len(self.excel_path)

a = MyData('Mydata_testdir','Carbon')
print(a[0])