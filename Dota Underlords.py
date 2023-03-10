import tkinter as tk
import re
import os

root = tk.Tk()

resolution_h = root.winfo_screenwidth()
resolution_v = root.winfo_screenheight()


resolution_h_r = r'("setting.defaultres"\s*)"\d+(")'
resolution_v_r = r'("setting.defaultresheight"\s*)"\d+(")'

def screen_resolution_replace(search_text,replace_text):
    with open('C:/Program Files (x86)/Steam/steamapps/common/Underlords/game/dac/cfg/video.txt', 'r+', encoding='UTF-8') as file:
        file_r = file.read()
        file_r = re.sub(search_text, rf'\1"{str(replace_text)}\2', file_r)
        file.seek(0)
        file.write(file_r)
        file.truncate()

    return "Resolution replaced"

def Run_underlords():
    print(screen_resolution_replace(resolution_h_r, resolution_h))
    print(screen_resolution_replace(resolution_v_r, resolution_v))
    os.startfile("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Underlords\\game\\bin\\win64\\underlords")


if __name__  == '__main__':
    Run_underlords()

