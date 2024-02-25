import ttkbootstrap as tb
from vid2img.sections import VideoInfoSection, VideoSaveSection
from vid2img import utils


def draw_widgets(root):
    create_header(root)

    separator = tb.Separator(root, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=5, sticky=tb.EW)

    create_file_select(root)
    continue_after_video_browse(root)

    # Video Info Section
    root.info_label_frame.grid(
        row=4, rowspan=2, column=0, padx=10, ipadx=5, pady=20, sticky=tb.NS
    )
    info_section = VideoInfoSection(root.info_label_frame)
    info_section.draw_sections()

    # Video Save Section
    root.save_label_frame.grid(
        row=4,
        rowspan=2,
        column=1,
        columnspan=3,
        padx=10,
        ipadx=5,
        pady=20,
        sticky=tb.NS,
    )
    save_section = VideoSaveSection(app=root, root=root.save_label_frame)
    save_section.draw_sections()

    # Call Actions
    root.continue_btn.config(
        command=lambda: utils.continue_button_handler(root, info_section, save_section)
    )
    save_section.skip_frames_box.bind(
        "<KeyRelease>",
        lambda event: utils.update_label_on_skip_frame_change(
            converter=root.converter, save_section=save_section
        ),
    )
    save_section.browse_btn.config(
        command=lambda: utils.select_image_path(root.converter, save_section)
    )
    save_section.save_btn.config(
        command=lambda: utils.save_button_handler(root.converter, save_section)
    )


def create_header(root):
    root.logo.grid(row=0, column=0, padx=10, pady=5, sticky=tb.NW)
    root.desc.grid(row=0, column=1, sticky=tb.NW, padx=5, pady=15)

    root.help_btn.grid(row=0, column=2, sticky=tb.NE, padx=5, pady=15)
    root.about_btn.grid(row=0, column=3, sticky=tb.NW, padx=5, pady=15)


def create_file_select(root):
    root.file_label.grid(row=2, column=0, sticky=tb.EW, padx=30, pady=5)
    root.video_input_box.grid(row=2, column=1, pady=5, sticky=tb.EW)
    root.browse_btn.grid(row=2, column=2, sticky=tb.EW, pady=5)


def continue_after_video_browse(root):
    root.continue_btn.grid(row=3, column=1, ipadx=5, sticky=tb.EW)
