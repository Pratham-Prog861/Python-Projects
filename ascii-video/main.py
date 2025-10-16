import cv2
import os
import time
import numpy as np

def convert_frame_to_ascii(frame, width=80):
    """
    Convert a frame to ASCII art using brightness-based characters.
    """
    ascii_chars = " .:-=+*#%@"
    
    # Maintain aspect ratio
    height = max(1, int(frame.shape[0] * width / frame.shape[1] / 2))
    
    gray = cv2.cvtColor(cv2.resize(frame, (width, height)), cv2.COLOR_BGR2GRAY)
    normalized = gray / 255.0

    indices = (normalized * (len(ascii_chars) - 1)).astype(int)
    ascii_art = "\n".join("".join(ascii_chars[pix] for pix in row) for row in indices)
    
    return ascii_art


def find_video_in_current_folder():
    """
    Automatically find the first video file in the current directory.
    Supported formats: .mp4, .avi, .mkv, .mov
    """
    supported_ext = ('.mp4', '.avi', '.mkv', '.mov')
    for file in os.listdir('.'):
        if file.lower().endswith(supported_ext):
            return file
    return None


def play_video_in_terminal(video_path, width=80, fps=30):
    """
    Play a video as ASCII art in the terminal.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return

    cap = cv2.VideoCapture(video_path)
    video_fps = cap.get(cv2.CAP_PROP_FPS) or fps
    frame_delay = 1.0 / video_fps

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_art = convert_frame_to_ascii(frame, width)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_art)

            time.sleep(frame_delay)

    except KeyboardInterrupt:
        print("\nVideo playback interrupted.")
    finally:
        cap.release()


if __name__ == "__main__":
    # Try auto-detecting video in current folder
    detected_video = find_video_in_current_folder()

    if detected_video:
        print(f"🎥 Found video in current folder: {detected_video}")
        video_path = detected_video
    else:
        video_path = input("Enter the path to the video file: ").strip()

    try:
        width = int(input("Enter terminal width (default 80): ") or "80")
    except ValueError:
        width = 80

    try:
        fps = int(input("Enter FPS (default: use video FPS): ") or "0")
    except ValueError:
        fps = 0

    play_video_in_terminal(video_path, width, fps)
