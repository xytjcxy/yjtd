# # -*- coding: utf-8 -*-
import xlrd
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import tkinter.messagebox as messagebox
import UpdateSoilT
import shangChuan


# 获取工作表的行列数，返回一个数组，第一项是行数，第二项是列数
def getRowCol(filename, sheetname):
    workbook = xlrd.open_workbook(filename)
    table = workbook.sheet_by_name(sheetname)
    res = [table.nrows, table.ncols]
    return res


# 获取工作表第row行的数据
def getRowValue(filename, sheetname, row):
    workbook = xlrd.open_workbook(filename)
    table = workbook.sheet_by_name(sheetname)
    res = table.row_values(row)
    return res


# 获取工作表第col列的数据
def getColValue(filename, sheetname, col):
    workbook = xlrd.open_workbook(filename)
    table = workbook.sheet_by_name(sheetname)
    res = table.col_values(col)
    return res


class MyWindows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('525x800')
        self.ft = tkFont.Font(family='Fixdsys', size=13, weight=tkFont.NORMAL)
        self.title('沿江通道数据处理')

        # welcome image
        canvas = tk.Canvas(self, height=800, width=525, bg='white')
        im = Image.open('images\\2.jpg')
        imag = ImageTk.PhotoImage(im)
        canvas.create_image(200, 400, image=imag)
        canvas.pack(side='top')

        self.var_file_name1 = tk.StringVar()
        self.var_file_name2 = tk.StringVar()

        b1 = tk.Button(self, text='更新今日土温数据', font=self.ft, bg='pink', command=self.createUST)
        b1.place(x=160, y=330)
        b2 = tk.Button(self, text='更新今日上传模板', font=self.ft, bg='pink', command=self.createSC)
        b2.place(x=160, y=380)
        self.mainloop()

    def on_click1(self):
        filename = self.var_file_name1.get()
        result = UpdateSoilT.UpdateSoil(filename).solveFile()
        if result:
            messagebox.showinfo('result', 'data solve successfully!')
        else:
            messagebox.showinfo('result', 'file not find!')

    def on_click2(self):
        # filename是土温汇总,filename1是上传模板
        filename = self.var_file_name1.get()
        filename1 = self.var_file_name2.get()
        result = shangChuan.shangChuan(filename, filename1).solveFile()
        if result:
            messagebox.showinfo('result', 'data solve successfully!')
        else:
            messagebox.showinfo('result', 'file not find!')

    def createUST(self):
        top = tk.Toplevel(height=500, width=450, bg='white')
        top.title('数据处理')
        tk.Label(top, text='文件路径: ', bg='pink', anchor='w', font=self.ft).place(x=14, y=160)
        self.var_file_name1.set('E:\\YJTD\\10.26\\6#土温汇总.xlsx')
        entry_file_name = tk.Entry(top, textvariable=self.var_file_name1, width=35, font=self.ft)
        entry_file_name.place(x=130, y=160)
        b = tk.Button(top, text='确认', font=self.ft, bg='pink', command=self.on_click1)
        b.place(x=130, y=190)

    def createSC(self):
        top = tk.Toplevel(height=500, width=450, bg='white')
        top.title('数据处理')
        tk.Label(top, text='土温汇总文件路径: ', bg='pink', anchor='w', font=self.ft).place(x=130, y=160)
        self.var_file_name1.set('E:\\YJTD\\10.26\\6#土温汇总.xlsx')
        tk.Label(top, text='上传模板文件路径: ', bg='pink', anchor='w', font=self.ft).place(x=130, y=260)
        self.var_file_name2.set('E:\\YJTD\\10.26\\上传模板.xlsx')
        entry_file_name = tk.Entry(top, textvariable=self.var_file_name1, width=35, font=self.ft)
        entry_file_name.place(x=130, y=190)
        entry_file_name = tk.Entry(top, textvariable=self.var_file_name2, width=35, font=self.ft)
        entry_file_name.place(x=130, y=290)
        b = tk.Button(top, text='确认', font=self.ft, bg='pink', command=self.on_click2)
        b.place(x=130, y=320)
