import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from multiprocessing import Process
import re

net = " --add Microsoft.VisualStudio.Workload.ManagedDesktop --add Component.GitHub.VisualStudio"
cpp = " --add Microsoft.VisualStudio.Workload.NativeDesktop"
py = ' --add Microsoft.VisualStudio.Workload.Python'
lang = ""
content = (net, cpp, py, lang)

def get_file_path():
    exe_in.delete(0, 'end')
    try:
        filePath = filedialog.askopenfile().name
    except:
        filePath = ''
    exe_in.insert(0, filePath)

def get_down_path():
    down_path.delete(0,'end')
    try:
        folder = filedialog.askdirectory()
    except:
        folder = ''
    down_path.insert(0, folder)

def down():
    global net_web_desktop
    global net_office
    global cpp
    global lang
    #vs.exe --layout %s -add .... --lang zh-CN
    exe = exe_in.get().replace('/', '\\')
    dpath = down_path.get().replace('/', '\\')
    i = ops.curselection()
    comm = exe+' --layout \"'+dpath+'\"'
    for each in i:
        comm+=content[each]
    comm+=' --includeRecommended --lang zh-CN'
    if len(i)==0:
        messagebox.showinfo(title = "提示", message = "未选择任何组件！")
    Process(target = os.system, args = (comm,)).start()

def inst():
    dpath = down_path.get().replace('/', '\\')
    p = Process(target = os.system, args = (dpath+"\\vs_setup.exe",))
    p.start()
    # ~ os.system(dpath+"\\vs_setup.exe")

app = tk.Tk()
app.title("Visual Studio离线安装工具")
app_title = tk.Label(app, text = "Visual Studio离线安装工具", font = ("Consolas", 18))
exe_in = tk.Entry(app, font = ("Consolas", 16), width = 28)
in_button = tk.Button(text = "浏览安装程序", command = get_file_path, width = 46)
ops = tk.Listbox(app, selectmode = "multiple", height = 4, font = ("Consolas", 12))
ops.insert('end', '.Net桌面开发')
ops.insert('end', 'C++开发')
ops.insert('end', 'Python开发')
ops.insert('end', '完整功能')
down_path = tk.Entry(app, font = ("Consolas", 16), width = 28)
down_path.insert(0, 'd:\\vslayout')
down_path_button = tk.Button(app, text = "指定下载目录...", command = get_down_path, width = 46)
down_but = tk.Button(app, text = "下载离线文件", width = 22, command = down)
inst_but = tk.Button(app, text = "从离线文件安装", width = 22, command = inst)

def main():
    for each in os.listdir():
        if re.search("vs.+\.exe", each):
            exe_in.insert(0, os.getcwd()+'\\'+each)
    app_title.pack(side = "top")
    exe_in.pack(side = "top")
    in_button.pack(side = "top")
    ops.pack(side = "top")
    down_path.pack(side = 'top')
    down_path_button.pack(side = 'top')
    down_but.pack(side = 'left')
    inst_but.pack(side = 'right')
    app.mainloop()
if __name__=='__main__':
    main()
