import ttkbootstrap as tb
from vid2img import widgets, utils
from vid2img.sections import VideoInfoSection, VideoSaveSection
from vid2img.converter import Converter


WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600


class App(tb.Window):

    def __init__(self):
        super().__init__(self, themename="minty")
        self.title("Video Image Extractor")
        self.iconbitmap("favicon.ico")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)

        self.converter: Converter
        self.video_path = tb.StringVar()

        self.info_section: VideoInfoSection
        self.save_section: VideoSaveSection

        # 5 (rows) x 4 (cols) grids
        self.configure_grids(5, 4)
        self.init_top_widgets()
        self.init_converter_widgets()


    def run(self):
        widgets.draw_widgets(self)
        self.mainloop()


    def configure_grids(self, row, col):
        for i in range(row):
            self.grid_rowconfigure(i, weight=1)

        for i in range(col):
            self.grid_columnconfigure(i, weight=1)


    def init_top_widgets(self):
        # Header
        self.logo = tb.Label(
            self, text="vid2img", bootstyle="secondary", font=("Helvetica", 20, "bold")
        )
        self.desc = tb.Label(
            self,
            text="Easily extract image frame from the video",
            bootstyle="dark",
            font=("Helvetica", 12),
        )
        self.help_btn = tb.Button(self, bootstyle="danger", text="Help")
        self.about_btn = tb.Button(self, bootstyle="info", text="About")

        # File Selection Section
        self.file_label = tb.Label(
            self,
            text="Select a video file to continue",
            bootstyle="dark",
            font=("Helvetica", 10),
        )
        self.video_input_box = tb.Entry(self, width=40, textvariable=self.video_path)
        self.browse_btn = tb.Button(
            self,
            bootstyle="primary",
            text="Browse",
            command=lambda: utils.select_video_file(
                root_app=self, input_box=self.video_input_box
            ),
        )

        # Continue after file selection
        self.continue_btn = tb.Button(
            self,
            bootstyle="success",
            text="Continue",
            state=tb.DISABLED,
            command=None
        )


    def init_converter_widgets(self):
        self.info_label_frame = tb.LabelFrame(
            self, text="Video Information", bootstyle="info"
        )

        self.save_label_frame = tb.LabelFrame(
            self, text="Save Images Options", bootstyle="info"
        )
