from tkinter import filedialog, TclError
import ttkbootstrap as tb
from vid2img.converter import Converter
from threading import Thread
import time

def select_video_file(root_app, input_box, event=None):
    filetypes = (
        ("MP4 File", "*.mp4"),
        ("3GP File", "*.3gp"),
        ("MKV File", "*.mkv"),
        ("All files", "*.*"),
    )

    file_path = filedialog.askopenfilename(
        title="Select a video file", filetypes=filetypes
    )

    if file_path:
        root_app.continue_btn["state"] = tb.NORMAL
        input_box.delete(0, tb.END)
        input_box.insert(0, file_path)


def continue_button_handler(root, info_section, save_section, event=None):
    root.converter = Converter(root.video_path.get())

    # Info Section
    info_section.show_file_size["text"] = (
        f"{root.converter.file_size_bytes/1024**2:.2f} MB"
    )
    info_section.show_duration["text"] = f"{root.converter.video_length} Seconds"
    info_section.show_dimension["text"] = (
        f"{root.converter.video_height}x{root.converter.video_width}"
    )
    info_section.show_total_frames["text"] = f"{root.converter.total_frames}"
    info_section.show_fps["text"] = f"{root.converter.fps} FPS"
    info_section.show_bitrate["text"] = f"{root.converter.bitrate} kbits/s"

    # Enable Save Section
    save_section.skip_frames_box["state"] = tb.NORMAL
    save_section.skip_frames.set(root.converter.fps)
    save_section.format_box["state"] = tb.READONLY
    save_section.image_path_box["state"] = tb.NORMAL
    save_section.browse_btn["state"] = tb.NORMAL
    save_section.progress_label["text"] = (
        f"Total Images to be Saved: {int(root.converter.total_frames/root.converter.fps)}"
    )


def select_image_path(converter, save_section, event=None):
    image_path = filedialog.askdirectory()

    if image_path:
        converter.image_path = image_path
        # converter.close()

        save_section.image_path_box.delete(0, tb.END)
        save_section.image_path_box.insert(0, image_path)
        save_section.save_btn["state"] = tb.NORMAL


def save_button_handler(converter, save_section, event=None):
    print("Starting proress bar!")
    save_section.progress_bar["mode"] = tb.INDETERMINATE
    save_section.progress_bar.start(20)
    print("Progress bar started!")

    convert = Thread(
        target=converter.extract_frames, name="Start Extracting Images", daemon=True
    )
    convert.start()

    while converter.task_done == False:
        save_section.progress_label["text"] = (
            f"Total Images Saved: {int(converter.frame_counter)}"
        )

    save_section.progress_bar.stop()
    save_section.progress_bar["mode"] = tb.DETERMINATE
    save_section.progress_bar["value"] = 100

def update_label_on_skip_frame_change(converter, save_section, event=None, *args):
    
    try:
        if save_section.skip_frames.get() != "":
            print(f"Frames changed to --> {int(save_section.skip_frames.get())}")
            converter.skip_frames = int(save_section.skip_frames.get())
    except TclError:
        pass
        
    save_section.progress_label["text"] = (
        f"Approx Images to be Saved: {int(converter.total_frames/converter.skip_frames)}"
    )

def start_progress_bar(save_section):
    save_section.progress_bar["mode"] = tb.INDETERMINATE
    save_section.progress_bar.start(20)

def update_progress_bar_label(converter, save_section):
    save_section.progress_label["text"] = (
        f"Total Images Saved: {int(converter.frame_counter)}"
    )
