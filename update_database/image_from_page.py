import cv2
import numpy as np
import os

def extract_images_from_left_quarter(input_image_path, output_folder):
    # Load the image
    img = cv2.imread(input_image_path)

    # Get image dimensions
    height, width = img.shape[:2]

    # Crop the left 1/4 area of the image
    left_quarter_img = img[:, :width // 5]

    # Convert to grayscale
    gray = cv2.cvtColor(left_quarter_img, cv2.COLOR_BGR2GRAY)

    # Threshold the image to get a binary image
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # Invert binary image for better contour detection

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a counter for output images
    count = 0

    for contour in contours:
        # Get the bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)

        # Check the size of the bounding box
        if 27 <= w and 30 <= h:
            count += 1
            # Extract the region of interest (ROI)
            roi = left_quarter_img[y:y+h, x:x+w]

            # Save the ROI
            output_image_path = f"{output_folder}/{os.path.basename(input_image_path).split('.')[0]}_{count}.png"
            cv2.imwrite(output_image_path, roi)
            print(f"Extracted: {output_image_path}")

# Example usage
input_folder = 'pages/page_SUP_2014'  # Your input directory containing images
output_folder = 'extracted_images'  # Desired output folder path

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):  # You can adjust this to other file types as needed
        input_image_path = os.path.join(input_folder, filename)
        extract_images_from_left_quarter(input_image_path, output_folder)
