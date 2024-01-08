import cv2
import numpy as np

def enhance_image(img_path):
    # Read the image
    img = cv2.imread(img_path)

    # Convert the image to LAB color space
    lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # Split the LAB image into L, A, and B channels
    l_channel, a_channel, b_channel = cv2.split(lab_image)

    # Apply CLAHE to the L channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enh_l_channel = clahe.apply(l_channel)

    # Apply bilateral filter for smoothing
    smooth_img = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    # Increase the brightness of the smoothed image
    enhanced_img = cv2.addWeighted(smooth_img, 1.5, np.zeros_like(smooth_img), 0, 30)

    # Merge the enhanced L channel with the original A and B channels
    enh_lab_image = cv2.merge([enh_l_channel, a_channel, b_channel])

    # Convert the enhanced LAB image back to BGR color space
    final_result = cv2.cvtColor(enh_lab_image, cv2.COLOR_LAB2BGR)

    return final_result

# Input image path
input_image_path = 'unclear.jpeg'

# Enhance the image
enhanced_image = enhance_image(input_image_path)

# Save the enhanced image
cv2.imwrite('enhanced_image.jpeg', enhanced_image)

print("Enhancement completed.")
