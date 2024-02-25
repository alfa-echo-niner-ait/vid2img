import ttkbootstrap as tb


class VideoInfoSection:

    def __init__(self, root) -> None:
        self.root = root
        self.show_file_size = tb.Label(self.root, text="0.0 MB")
        self.show_duration = tb.Label(self.root, text="0.0 Seconds")
        self.show_dimension = tb.Label(self.root, text="0x0")
        self.show_total_frames = tb.Label(self.root, text="0")
        self.show_fps = tb.Label(self.root, text="0 FPS")
        self.show_bitrate = tb.Label(self.root, text="0.0 kbits/s")

    def draw_sections(self):
        file_size_label = tb.Label(self.root, text="File Size: ")
        file_size_label.grid(row=0, column=0, padx=5, pady=5, sticky=tb.EW)
        self.show_file_size.grid(row=0, column=1, padx=5, sticky=tb.EW)

        duration_label = tb.Label(self.root, text="Duration: ")
        duration_label.grid(row=1, column=0, padx=5, pady=5, sticky=tb.EW)
        self.show_duration.grid(row=1, column=1, padx=5, sticky=tb.EW)

        dimension_label = tb.Label(self.root, text="Dimension: ")
        dimension_label.grid(row=2, column=0, padx=5, pady=5, sticky=tb.EW)
        self.show_dimension.grid(row=2, column=1, padx=5, sticky=tb.EW)

        total_frames_label = tb.Label(self.root, text="Total Frames: ")
        total_frames_label.grid(row=3, column=0, padx=5, pady=5, sticky=tb.EW)
        self.show_total_frames.grid(row=3, column=1, padx=5, sticky=tb.EW)

        fps_label = tb.Label(self.root, text="FPS: ")
        fps_label.grid(row=4, column=0, padx=5, pady=5, sticky=tb.EW)
        self.show_fps.grid(row=4, column=1, padx=5, sticky=tb.EW)

        bitrate_label = tb.Label(self.root, text="Bitrate: ")
        bitrate_label.grid(row=5, column=0, padx=5, pady=5, sticky=tb.EW)
        self.show_bitrate.grid(row=5, column=1, padx=5, sticky=tb.EW)


class VideoSaveSection:
    def __init__(self, app, root) -> None:
        self.app = app
        self.root = root
        self.selected_format: str
        self.img_formats = (
            "JPEG",
            "PNG",
            "BMP",
        )
        self.format_box = tb.Combobox(
            self.root, bootstyle="success", values=self.img_formats, state=tb.DISABLED
        )
        self.skip_frames = tb.IntVar()
        self.image_path = tb.StringVar()
        self.progress_bar = tb.Progressbar(
            root,
            bootstyle="success",
            orient=tb.HORIZONTAL,
            mode=tb.DETERMINATE,
            length=480,
            value=0,
        )
        self.progress_label = tb.Label(
            self.root, text="Image Saved: 0", bootstyle="success", font=("bold")
        )

    def draw_sections(self):
        image_format_label = tb.Label(self.root, text="Image Format:")
        image_format_label.grid(row=0, column=0, padx=5, pady=5, sticky=tb.EW)
        self.format_box.grid(row=0, column=1, padx=5, pady=5, sticky=tb.EW)
        self.format_box.set(self.img_formats[0])
        self.format_box.bind("<<ComboboxSelected>>", self.format_box_handler)

        skip_frame_label = tb.Label(self.root, text="Skip Frames Per Image:")
        skip_frame_label.grid(row=1, column=0, padx=5, pady=5, sticky=tb.EW)
        self.skip_frames_box = tb.Entry(
            self.root,
            bootstyle="success",
            textvariable=self.skip_frames,
            state=tb.DISABLED,
        )
        self.skip_frames_box.grid(row=1, column=1, padx=5, pady=5, sticky=tb.EW)

        save_label = tb.Label(
            self.root,
            text="Select a Location to Save Images:",
        )
        save_label.grid(row=2, column=0, sticky=tb.EW, padx=5, pady=5)

        self.image_path_box = tb.Entry(
            self.root, width=35, textvariable=self.image_path, state=tb.DISABLED
        )
        self.image_path_box.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tb.EW
        )

        self.browse_btn = tb.Button(
            self.root, bootstyle="primary", text="Browse", state=tb.DISABLED, command=None
        )
        self.browse_btn.grid(row=3, column=2, sticky=tb.EW, pady=5)

        self.save_btn = tb.Button(
            self.root, bootstyle="success", text="Save Images", state=tb.DISABLED
        )
        self.save_btn.grid(
            row=4, column=0, columnspan=2, ipadx=5, padx=5, pady=5, sticky=tb.EW
        )

        self.progress_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
        self.progress_bar.grid(row=6, column=0, columnspan=3, padx=5, pady=5, ipady=10)
        

    # Handlers
    def format_box_handler(self, event):
        self.selected_format = self.format_box.get()
        print(self.selected_format)
        self.app.converter.image_format = self.format_box.get()
        

    def update_progress_status(self):
        self.progress_bar['mode'] = tb.INDETERMINATE
        self.progress_bar.start(20)
