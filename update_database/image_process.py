import cv2
import numpy as np
import os

def remove_right(image):    
    lower_bound = np.array([235, 235, 235])  # Specify lower bound
    upper_bound = np.array([255, 255, 255])  # Specify upper bound

    mask = cv2.inRange(image, lower_bound, upper_bound)

    # Scan the image from top to bottom to find the first non-zero pixel in the mask
    height, width = mask.shape
    
    # Iterate from the right to left to find the first non-white pixel column
    for x in range(width - 1, -1, -1):
        if np.any(mask[:, x] == 0):  # Found a column with a non-white pixel
            # Crop the image to remove the white section on the right
            return image[:, :x]  # Return the cropped image and the new width

    # If no white section detected, return the original image
    return image

def remove_bottom(image):
    lower_bound = np.array([235, 235, 235])  # Specify lower bound
    upper_bound = np.array([255, 255, 255])  # Specify upper bound
    # Create a mask for the specific color range
    mask = cv2.inRange(image, lower_bound, upper_bound)

    # Scan the image from top to bottom to find the first non-zero pixel in the mask
    height, width = mask.shape
    
    for y in range(height - 1, -1, -1):
        if np.any(mask[y, :] == 0):  # If there's a non-white pixel in this row
            return image[:y + 1, :]  # Return the cropped image
    
    return image  # If no white pixels were found, return original image

def remove_left(image):    
    lower_bound = np.array([235, 235, 235])  # Specify lower bound
    upper_bound = np.array([255, 255, 255])  # Specify upper bound

    mask = cv2.inRange(image, lower_bound, upper_bound)

    # Scan the image from top to bottom to find the first non-zero pixel in the mask
    height, width = mask.shape
    
    # Iterate over columns from left to right
    for x in range(width):
        if np.any(mask[:, x] == 0):  # Found a non-white column
            return image[:, x:]  # Return cropped image from the first non-white pixel to the right

    return image  # If all columns are white, return the original image

def remove_top(image):
    lower_bound = np.array([235, 235, 235])  # Specify lower bound
    upper_bound = np.array([255, 255, 255])  # Specify upper bound
    # Create a mask for the specific color range
    mask = cv2.inRange(image, lower_bound, upper_bound)

    # Scan the image from top to bottom to find the first non-zero pixel in the mask
    height, width = mask.shape

    top_cut_off = height
    
    for y in range(height):
        if np.any(mask[y, :] == 0):  # If there's a non-white pixel in this row
            top_cut_off = y  # Keep track of the first non-white row
            break

    # Return the cropped image
    return image[top_cut_off:, :]

input_folder = 'manual_images'
output_folder = 'processed_images'
count = 0
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):  # You can adjust this to other file types as needed
        input_image_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_image_path)

        # # image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        # cv2.imwrite(f"{output_folder}/{count}.png", img)
        # count+=1
        image = remove_top(img)

        image = remove_bottom(image)

        image = remove_right(image)

        image = remove_left(image)

        output_image_path = f"{output_folder}/{os.path.basename(input_image_path).split('.')[0]}.png"
            
        cv2.imwrite(output_image_path, image)
