import cv2

# Path to the video file
video_path = r"C:\Users\aysha\OneDrive\Desktop\Miniproject\video.mp4"

# Open video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video details
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Width of the frames in the video
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Height of the frames in the video
fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames

# Print video details
print(f"Video Details:")
print(f"Frame Width: {frame_width} pixels")
print(f"Frame Height: {frame_height} pixels")
print(f"FPS (Frames per second): {fps}")
print(f"Total Frames: {frame_count}")

# Read and display the video
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame or end of video.")
        break
    
    # Display the current frame
    cv2.imshow('Video Playback', frame)

    # Press 'q' to stop the video capture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
