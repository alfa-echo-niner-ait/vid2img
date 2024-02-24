from converter import Converter

def main():
    file = "visualdon.mp4"

    vid = Converter(file)

    print(f"File: {vid.filepath}")
    print(f"Length: {vid.video_length} seconds")
    print(f"Total Frames: {vid.total_frames}")
    print(f"FPS: {vid.fps}")
    print(f"Dimension: {vid.video_width}x{vid.video_height}")
    print(f"Bitrate: {vid.bitrate} kbits/s")
    print(f"Size: {vid.file_size_bytes/(2**20):.2f} Megabytes")

    vid.close()

main()
