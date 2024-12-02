import cv2
import numpy as np

# Read the image
image_path = r"C:\Users\aysha\OneDrive\Desktop\Miniproject\image.png"
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Resize the image for display (reduce size by 50%)
scale_percent = 50  # Adjust this value to resize the image
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Apply the average filter (mean filter) using a kernel size of 5x5
kernel = np.ones((5, 5), np.float32) / 25  # Create a 5x5 averaging kernel
average_filtered_image = cv2.filter2D(resized_image, -1, kernel)

# Display the resized original and filtered images
cv2.imshow("Resized Original Image", resized_image)
cv2.imshow("Average Filtered Image", average_filtered_image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the windows
