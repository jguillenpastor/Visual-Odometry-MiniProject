import cv2

# Path to the video file
video_path = '../DJI_0199.MOV'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Frame counter
frame_count = 0

# Resize scale factor
scale_factor = 0.2  # You can adjust this value as needed

# Read and display the first 1200 frames
while frame_count < 1200:
    ret, frame = cap.read()
    
    # Check if frame is None (end of video)
    if frame is None:
        print("End of video reached.")
        break
    
    # Resize the frame
    resized_frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor)
    
    # Display the frame
    cv2.imshow('Frame', resized_frame)
    
    # Wait for 25 milliseconds (40 frames per second)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    frame_count += 1

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
