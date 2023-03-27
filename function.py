import json
import tkinter as tk
from tkinter import filedialog
import shutil
def selectPath(file_entry):
    path_ = filedialog.askdirectory()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, path_)
def savethemessage(file_entry,name_entry,data_path):
    games_data = {}
    save_path = file_entry.get()
    save_name = name_entry.get()
    conf = tk.messagebox.askyesno("确认","确定更新吗？")
    if conf:
        with open(data_path,"r")as f:
             games_data = json.load(f)
        games_data[save_name] = save_path
        with open(data_path,"w")as f:
             json.dump(games_data,f)
def addnewgame(file_entry,name_entry):
    conf = tk.messagebox.askyesno("确认", "确定清空吗？")
    if conf:
        file_entry.delete(0,tk.END)
        name_entry.delete(0,tk.END)

def update(name,data_path):
    conf = tk.messagebox.askyesno("确认", "确定更新吗？")
    if conf:
        with open(data_path, "r") as f:
             name.config(text=json.load(f))
#def confirm_save(saved_info_label):
#    conf = tk.messagebox.askyesno("确认","确定更新吗？")
#    if conf:
#        update(saved_info_label)
def newwindowsforcontent(data_path):
    root2 = tk.Tk()
    with open(data_path,"r")as f:
        games_data = json.load(f)
    for key,value in games_data.items():
     #   print(key,value)
         name = tk.Label(root2,text="游戏名称:  "+key)
         name.pack()
         address = tk.Label(root2,text="存档地址:  "+value)
         address.pack()
def dead(data_path):
    new_data = {"小月月": "2023年3月28日"}
    conf = tk.messagebox.askyesno("确认", "确定清空所有目录吗？")
    if conf:
      with open(data_path,"w")as f:
           json.dump(new_data,f)

def sync(flag,data_path,sync_entry,sync_folder):
   with open(data_path,'r')as f:
        games_data = json.load(f)
   if flag:
    # 单个游戏同步
    #  print(games_data.get(sync_entry.get()))
      game_path = games_data.get(sync_entry.get())
    # 将存档文件复制到指定的同步文件夹中
    #  shutil.copy(game_path, sync_folder)
      src = game_path
      dst = sync_folder
      shutil.rmtree(dst)
      shutil.copytree(src, dst)
