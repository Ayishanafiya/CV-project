import cv2
import numpy as np

# Read the image
image_path = r"C:\Users\aysha\OneDrive\Desktop\Miniproject\image.png"
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Resize the image for display (reduce size by 50%)
scale_percent = 50  # Adjust this value for different sizes
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Apply the mean filter (using a kernel size of 5x5)
mean_filtered_image = cv2.blur(resized_image, (5, 5))

# Display the resized original and filtered images
cv2.imshow("Resized Original Image", resized_image)
cv2.imshow("Mean Filtered Image", mean_filtered_image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the windows
