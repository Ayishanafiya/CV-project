import cv2
import numpy as np

# Function to add uniform noise to an image
def add_uniform_noise(image, low, high):
    noisy_image = np.copy(image)
    # Generate uniform noise in the specified range
    noise = np.random.uniform(low, high, image.shape).astype(np.uint8)
    noisy_image = cv2.add(noisy_image, noise)  # Add noise to the original image
    return noisy_image

# Read the image
image_path = r"C:\Users\aysha\OneDrive\Desktop\Miniproject\image.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Resize the image for better display (reduce size by 50%)
scale_percent = 50  # Resize factor
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Add uniform noise (range 0 to 50)
low = 0
high = 50
noisy_image = add_uniform_noise(resized_image, low, high)

# Remove the noise using Gaussian blur
denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)  # Kernel size of 5x5

# Display the images
cv2.imshow("Original Image", resized_image)
cv2.imshow("Noisy Image (Uniform Noise)", noisy_image)
cv2.imshow("Denoised Image (Gaussian Blur)", denoised_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
