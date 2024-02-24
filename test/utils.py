import random
from tkinter import filedialog
import ttkbootstrap as tb


def counter(item):
    num = random.randint(1, 100)
    print(num)
    item.config(text=str(num))

def get_name(item):
    name = item.get()
    print(name)


def select_video_file(input_box, event=None):
    filetypes = (
        ("MP4 File", "*.mp4"),
        ("3GP File", "*.3gp"),
        ("MKV File", "*.mkv"),
        ("All files", "*.*"),
    )
    
    file_path = filedialog.askopenfilename(title="Select a video file", filetypes=filetypes)
    # Open file dialog to select video file
    # file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mkv")])

    # Check if file is selected
    if file_path:
        input_box.delete(0, tb.END)
        input_box.insert(0, file_path)
        print("Selected file:", file_path)
