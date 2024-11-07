import os
from PIL import Image
import math

def calculate_mean_and_std(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure image is in RGB format

    total_r = total_g = total_b = 0
    total_r_sq = total_g_sq = total_b_sq = 0
    width, height = img.size
    total_pixels = width * height

    # Sum up all pixel values
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            total_r += r 
            total_g += g 
            total_b += b 

            total_r_sq += r ** 2
            total_g_sq += g ** 2
            total_b_sq += b ** 2

    # Calculate mean values
    mean_rgb = (total_r // total_pixels, total_g // total_pixels, total_b // total_pixels)

    # Calculate standard deviation
    std_r = math.sqrt((total_r_sq / total_pixels) - (mean_rgb[0] ** 2))
    std_g = math.sqrt((total_g_sq / total_pixels) - (mean_rgb[1] ** 2))
    std_b = math.sqrt((total_b_sq / total_pixels) - (mean_rgb[2] ** 2))

    return mean_rgb, (std_r, std_g, std_b)

# Example usage
image_directory = 'images/images_AB_8ed_2024/extra'
image_filename = 'page_265_2.png'
image_path = os.path.join(image_directory, image_filename)

mean_rgb, std_rgb = calculate_mean_and_std(image_path)
print("Mean RGB:", mean_rgb)
print("Standard Deviation RGB:", std_rgb[0], std_rgb[1],std_rgb[2])
