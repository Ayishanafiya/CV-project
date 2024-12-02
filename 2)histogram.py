import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r"C:\Users\aysha\OneDrive\Desktop\Miniproject\image.png", cv2.IMREAD_GRAYSCALE)  # Ensure it's in grayscale
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Calculate and plot the histogram
plt.hist(image.ravel(), bins=256, range=[0, 256])
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()  # Display the histogram

