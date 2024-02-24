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
    file_size_bytes: float
    

    def __init__(self, filepath) -> None:
        print("\nOpening Converter:\n")
        self.filepath = filepath
        self.video = cv2.VideoCapture(filepath)
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS))
        self.video_length = float(self.total_frames / self.fps)
        self.bitrate = float(self.video.get(cv2.CAP_PROP_BITRATE))
        self.video_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.file_size_bytes = float(os.path.getsize(self.filepath))

    def close(self):
        self.video.release()
        cv2.destroyAllWindows()
        print("\nConverter Closed!\n")
