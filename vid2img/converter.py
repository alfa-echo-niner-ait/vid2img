import os
import cv2
import time

class Converter:
    filepath: str
    image_path: str
    image_format: str
    video: cv2.VideoCapture
    total_frames: int
    fps: int
    video_length: float
    bitrate: float
    video_width: int
    video_height: int
    frame_counter: int
    skip_frames: int
    task_done: bool

    def __init__(self, filepath) -> None:
        print("\nOpening Converter:\n")
        self.filepath = filepath
        self.frame_counter = 0
        self.skip_frames = 30
        self.image_format = "jpeg"
        self.task_done = False
        
        self.extract_video_info()

        
    def extract_video_info(self):
        self.video = cv2.VideoCapture(self.filepath)
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS))
        self.video_length = float(self.total_frames / self.fps)
        self.bitrate = float(self.video.get(cv2.CAP_PROP_BITRATE))
        self.video_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.file_size_bytes = float(os.path.getsize(self.filepath))
        
        
    def extract_frames(self):
        while self.task_done == False:
            for i in range(1, self.total_frames+1):
                if i%self.skip_frames == 0:
                    self.frame_counter += 1
                    ret, frame = self.video.read()
                    image_name = "Frame_" + str(self.frame_counter) + "." + self.image_format
                    save_path = os.path.join(self.image_path, image_name)
                    print(save_path)
                    cv2.imwrite(save_path, frame)
                    print(f"{image_name} saved!")
                    time.sleep(1)
                    
            self.task_done = True


    def close(self):
        self.video.release()
        cv2.destroyAllWindows()
        print("\nConverter Closed!\n")
