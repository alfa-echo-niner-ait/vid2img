import ttkbootstrap as tb
from tkinter import filedialog as fd
from ttkbootstrap.constants import *
import utils
import time
import random

WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600

root = tb.Window(themename="minty")

SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

CENTER_X = int((SCREEN_WIDTH / 2) - (WINDOW_WIDTH / 2))
CENTER_Y = int((SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT / 2))

root.title("Video Image Extractor")
# root.iconbitmap("./vid2img/assets/favicon.ico")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{CENTER_X}+{CENTER_Y}")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=1)

# Elements
# photo = tb.PhotoImage(file="./vid2img/assets/icon.png")
hello = tb.Label(
    root,
    text="Hello, World!",
    bootstyle="primary",
    font=("Segoe UI", 28),
)
# hello.pack(padx=5, pady=5)
hello.grid(column=1, row=0, padx=5, pady=5)

counter_btn = tb.Button(
    root, text="Click Here", bootstyle=INFO, command=lambda: utils.counter(hello)
)
# counter_btn.pack(padx=10, pady=10)
counter_btn.grid(column=1, row=1, padx=10, pady=10)


video_path = tb.StringVar()
video_input_box = tb.Entry(root, width=50, textvariable=video_path)
video_input_box.grid(column=1, row=2, sticky=E)
# file_btn = tb.Label(
#     root,
#     text="Select a Video File",
#     image=photo,
#     compound=tb.LEFT,
#     font=("Segoe UI", 18),
#     bootstyle="primary-inverse",
# )
file_btn = tb.Button(
    root,
    text="Browse",
    bootstyle="dark-outline",
    command=lambda: utils.select_video_file(video_input_box),
)
# file_btn.pack(pady=10, padx=10, ipadx=5, ipady=5)
file_btn.grid(column=2, row=2, padx=5, pady=5, ipadx=5, ipady=5, sticky=W)

# file_btn.bind("<Button-1>", lambda: utils.select_video_file(input_box=video_input_box))


name = tb.StringVar()
name_input_box = tb.Entry(root, textvariable=name)
# name_input_box.focus()
# name_input_box.pack(padx=15, pady=10, ipadx=5, ipady=5, side=tb.LEFT, anchor=tb.W)
name_input_box.grid(column=1, row=4, pady=10, ipadx=180, ipady=5, sticky=tb.W)
submit_btn = tb.Button(
    root, text="Submit", bootstyle=PRIMARY, command=lambda: utils.get_name(name)
)
# submit_btn.pack(padx=5, pady=5, ipadx=3, ipady=3, side=tb.LEFT, anchor=tb.W)
submit_btn.grid(column=1, row=4, pady=5, ipady=3, sticky=tb.E)


progress_label = tb.Label(root, text="Progess: 0%", bootstyle="info")
progress_label.grid(column=1, row=5, padx=5, pady=5)

progress_bar = tb.Progressbar(root, bootstyle="success", orient="horizontal", mode="indeterminate", length=400)
progress_bar.grid(column=1, row=6, padx=5, pady=10, ipady=15)

loop = 1
# while(loop < 11):
#     for i in range(1, 101, 5):
#         progress_bar['value'] = i
#         progress_label.config(text=f"Progress: {loop*10}%")
#         root.update()
#         time.sleep(0.1)
        
#     loop += 1
progress_bar.start(20)
while(loop < 11):
    for i in range(1, 101, 5):
        time.sleep(0.1)    
    loop += 1

progress_bar.stop()
progress_bar['mode'] = 'determinate'
progress_bar['value'] = 100

root.mainloop()
