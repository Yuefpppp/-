import json
import tkinter as tk
from tkinter import filedialog
import shutil
import os
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
           # update_flag = 1
           # print(update_flag)
    else:
        return
def addnewgame(file_entry,name_entry):
    conf = tk.messagebox.askyesno("确认", "确定清空吗？")
    if conf:
        file_entry.delete(0,tk.END)
        name_entry.delete(0,tk.END)

def update_menu(data_path,game_name_menu,game_name_var):
    # 获取更新后的游戏数据
    try:
        with open(data_path, "r") as f:
            games_data = json.load(f)
    except json.JSONDecodeError:
        games_data = {}
    # 清除 OptionMenu 小部件中的当前选项
    game_name_menu['menu'].delete(0, 'end')

    # 将新选项添加到 OptionMenu 小部件中
    for game_name in games_data.keys():
        game_name_menu['menu'].add_command(label=game_name, command=lambda value=game_name: game_name_var.set(value))


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
      game_name = sync_entry.get()
      game_path = games_data.get(sync_entry.get())
    # 将存档文件复制到指定的同步文件夹中
    #  shutil.copy(game_path, sync_folder) 注意使用shutil.copy是有条件的，比如当个文件到目录
      if game_name=="小月月":
          return
      else:
         src = game_path
         dst = sync_folder
         print(game_name)
         print(dst+game_name)
         if not os.path.exists(dst + game_name):
            print(f"错误: 目标路径 {dst} 不存在")
            os.makedirs(dst+game_name)
            shutil.rmtree(dst + game_name)
            shutil.copytree(src, dst + game_name)  # 复制目录到目录
         else:
            os.makedirs(dst + game_name)
            shutil.rmtree(dst + game_name)
            shutil.copytree(src, dst + game_name)  # 复制目录到目录
   else:
       # 存在json文件中的地址全同步
       with open(data_path, "r") as f:
           games_data = json.load(f)
       for key, value in games_data.items():
           if key == "小月月":
              # print("test")
              continue
           else:
               src = value
               dst = sync_folder
               print(key)
               print(dst + key)
               if not os.path.exists(dst+ key):
                   print(f"错误: 目标路径 {dst} 不存在")
                   os.makedirs(dst + key)
                   shutil.rmtree(dst + key)
                   shutil.copytree(src, dst + key)  # 复制目录到目录
               else:
                   shutil.rmtree(dst + key)
                   shutil.copytree(src, dst + key)  # 复制目录到目录


