# This is a games sync program
# 导入tkinter模块
import function
import tkinter as tk
import json

# 创建主窗口
root = tk.Tk()
data_path = "./save/save.json"
# 同步路径
sync_folder = "D:/test/"
#icacls "C:/Users/xiaoyueyue/Desktop/test" /grant Users:(OI)(CI)F

#games_data = {"test":test}
#with open("./save/save.json", "w") as f:
#     json.dump(games_data, f)

# 创建信息框
# saved_info_label = tk.Label(root, text="")
# saved_info_label.pack()
# with open("./save/save.json", "r") as f:
     # saved_info_label.config(text="已保存游戏记录:"+f.read())

# 初始化

#######################################################################
# 选择同步路径
with open("./save/save_address_sync.json","r")as f:
    select_sync_path = json.load(f)
sync_folder_opt_laber = tk.Label(root, text= "当前同步路径：\n"+select_sync_path)
sync_folder_opt_laber.pack()
sync_folder_opt_button = tk.Button(root,text="点击此处更改同步路径",command=lambda :function.selectPath_1(sync_folder_opt_laber))
sync_folder_opt_button.pack()
#######################################################################
# 创建标签和输入框，用于输入文件路径和游戏名称
file_label = tk.Label(root, text="存档文件路径:")
file_label.pack()
file_entry = tk.Entry(root)
file_entry.pack()
button = tk.Button(root, text="路径浏览", command=lambda: function.selectPath(file_entry))
button.pack()
name_label = tk.Label(root, text="游戏名字:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
#######################################################################
# 保存数据
save_button = tk.Button(root,text="更新",command=lambda: function.savethemessage(file_entry,name_entry,data_path))
save_button.pack()

#######################################################################
# 清空
add_button = tk.Button(root,text="清空",command=lambda :function.addnewgame(file_entry,name_entry))
add_button.pack()
# 清空所有内容
deadkey = tk.Button(root,text="！！清空所有目录！！",command=lambda :function.dead(data_path))
deadkey.pack()
#######################################################################
# 查看已添加的目录
content = tk.Button(root,text="查看已添加内容",command=lambda :function.newwindowsforcontent(data_path))
content.pack()
#######################################################################
# 同步
sync_laber = tk.Label(root,text="单个游戏同步选择:")
sync_laber.pack()
# 创建一个下拉菜单，用于选择要同步的游戏名称
game_name_var = tk.StringVar(root)
game_name_var.set("点击选择游戏")
with open(data_path, "r") as f:
    games_data = json.load(f)
game_name_menu = tk.OptionMenu(root, game_name_var, *games_data.keys())
game_name_menu.pack()
update_menu_button = tk.Button(root,text="刷新菜单",command=lambda :function.update_menu(data_path,game_name_menu,game_name_var))
update_menu_button.pack()
sync_onegame = tk.Button(root,text="同步所选择的游戏",command=lambda :function.sync(True,data_path,game_name_var,select_sync_path))
sync_onegame.pack()
sync_allgame = tk.Button(root,text="*一键同步目录内游戏*",command=lambda :function.sync(False,data_path,game_name_var,select_sync_path))
sync_allgame.pack()
#######################################################################


# 进入消息循环
root.mainloop()