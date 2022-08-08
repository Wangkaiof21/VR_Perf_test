import openpyxl
import os
from LogMessage import LogMessage, LOG_INFO, LOG_ERROR
from zipfile import BadZipFile
from openpyxl.styles import Alignment


class Excel:
    def __init__(self, file_name, new_flag=False):
        """
        对openpyxl封装
        :param file_name:需要操作的excel文件路径和名称
        :param new_flag:如果file_name 不存在则新建，存在也不会覆盖
        """
        self.file_name = file_name
        if os.path.exists(self.file_name):
            try:
                self.wb = openpyxl.load_workbook(file_name)
            except BadZipFile as e:
                raise BadZipFile(f"Excel 文件损坏 ,{e}.....")
        else:
            if new_flag:
                self.wb = openpyxl.Workbook()
                self.wb.save(file_name)
                LogMessage(level=LOG_INFO, module="Excel", msg='sheet_name:"{}"不存在 新建~'.format(self.file_name))
            else:
                LogMessage(level=LOG_ERROR, module="Excel", msg='sheet_name:"{}"不存在'.format(self.file_name))
        # file_name 里面所有sheet的名字 (List[str])
        self.sheet_list = self.wb.sheetnames
        self.align = Alignment(horizontal="left", vertical="center")
