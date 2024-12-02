import cv2
import numpy as np

# Function to add Gaussian noise to an image
def add_gaussian_noise(image, mean=0, std=25):
    # Generate Gaussian noise
    gaussian_noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, gaussian_noise)  # Add noise to the original image
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

# Add Gaussian noise (mean = 0, standard deviation = 25)
mean = 0
std = 25
noisy_image = add_gaussian_noise(resized_image, mean, std)

# Remove Gaussian noise using Gaussian blur
denoised_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)  # Apply Gaussian blur

# Display the images
cv2.imshow("Original Image", resized_image)
cv2.imshow("Noisy Image (Gaussian Noise)", noisy_image)
cv2.imshow("Denoised Image (Gaussian Blur)", denoised_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
