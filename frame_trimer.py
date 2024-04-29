import cv2
import os

# Path to the video file
video_path = '../DJI_0199.MOV'

# Output directory to save frames
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Skip the first 1200 frames
for _ in range(1200):
    cap.read()

# Counter for saved frames
frame_count = 0

# Iterate through frames
while True:
    ret, frame = cap.read()
    
    # Check if frame is None (end of video)
    if frame is None:
        break
    
    # Save every 25th frame
    if frame_count % 25 == 0:
        frame_filename = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved frame {frame_count}")
    
    frame_count += 1

# Release video capture
cap.release()

print("Frames saved successfully.")
