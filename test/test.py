import os
import cv2


class Converter:
    filepath: str
    video: cv2.VideoCapture
    total_frames: int
    fps: int
    video_length: float
    bitrate: float
    video_width: int
    video_height: int

    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.video = cv2.VideoCapture(filepath)
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS))
        self.video_length = float(self.total_frames/self.fps)
        self.bitrate = float(self.video.get(cv2.CAP_PROP_BITRATE))
        self.video_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def close(self):
        self.video.release()
        cv2.destroyAllWindows()

frame_count = 0


def get_fcount():
    global frame_count
    c_count = frame_count
    frame_count += 1
    return c_count


def vid_len(vid):
    length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


def extract_frames(vid, img_path, skip_frames=30):
    length = vid_len(vid)

    for i in range(0, length):
        if i % skip_frames == 0:
            ret, frame = vid.read()
            f_name = "frame_" + str(get_fcount()) + ".bmp"
            save_path = os.path.join(img_path, f_name)
            cv2.imwrite(save_path, frame)
            print(f"{f_name} saved!")


def main():
    vid_path = "visualdon.mp4"
    # img_path = "img_p"
    # video = cv2.VideoCapture(vid_path)
    # extract_frames(video, img_path, 30)
    # video.release()
    # cv2.destroyAllWindows()
    vid = Converter(vid_path)

    print(f"File: {vid.filepath}")
    print(f"Length: {vid.video_length}")
    print(f"FPS: {vid.fps}")
    print(f"Dimension: {vid.video_width}x{vid.video_height}")
    print(f"Bitrate: {vid.bitrate} kbits/s")


    vid.close()


main()
