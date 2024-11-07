import os
import cv2  # OpenCV for handling images
import sqlite3
import numpy as np  # NumPy for numerical operations

# Connect to the SQLite database
connection = sqlite3.connect('signals.db')
cursor = connection.cursor()

# Specify the directory containing the images
image_directory = 'images/images_AM_2015'
image_filenames = sorted(os.listdir(image_directory))  # Get sorted list of image filenames

# Corresponding numero_ministeriale values for the images
numero_ministeriale_list = [
    '01007', '01006', '01005', '01004', '01003', '01002', '01001',  
    '01014', '01013', '01012', '01011', '01010', '01009', '01008',
    '01021' ,'01020' ,'01019' ,'01018' ,'01017' ,'01016' ,'01015',
    '01028' ,'01027' ,'01026' ,'01025' ,'01024' ,'01023' ,'01022',
    '01035' ,'01034' ,'01033' ,'01032' ,'01031' ,'01030' ,'01029',
    '01042' ,'01041' ,'01040' ,'01039' ,'01038' ,'01037' ,'01036',
    '02007' ,'02006' ,'02005' ,'02004' ,'02003' ,'02002' ,'02001',
    '02015' ,'02014' ,'02013' ,'02012' ,'02011' ,'02010' ,'02009', '02008',
    '02022' ,'02021' ,'02020' ,'02019' ,'02018' ,'02017' ,'02016',
    '02030' ,'02029' ,'02028' ,'02027' ,'02026' ,'02025' ,'02024', '02023',
    '02038' ,'02037' ,'02036' ,'02035' ,'02034' ,'02033' ,'02032', '02031',
    '02046' ,'02045' ,'02044' ,'02043' ,'02042' ,'02041' ,'02040', '02039',
    '02054' ,'02053' ,'02052' ,'02051' ,'02050' ,'02049' ,'02048', '02047',
    '02056' ,'02055' 
    '03006' ,'03005' ,'03004' ,'03003' ,'03002' ,'03001' ,
    '03013' ,'03012' ,'03011' ,'03010' ,'03009' ,'03008' ,'03007',
    '03020' ,'03019' ,'03018' ,'03017' ,'03016' ,'03015' ,'03014',
    '03026' ,'03025' ,'03023' ,'03022' ,'03021' ,
    '03033' ,'03032' ,'03029' ,'03028' ,
    '03041' ,'03040' ,'03039' ,'03038' ,'03037' ,'03036' ,'03035',
    '03046' ,'03045' ,'03044' ,'03043' ,'03042' ,
    '04007' ,'04006' ,'04005' ,'04004' ,'04003' ,'04002' ,'04001',
    '04014' ,'04013' ,'04012' ,'04011' ,'04010' ,'04009' ,'04008',
    '04016' ,'04015'
]

# Iterate over images and update database
for i, image_filename in enumerate(image_filenames):
    if not image_filename.endswith('.png'):
        continue  # Skip non-PNG files

    # Get corresponding numero_ministeriale
    if i < len(numero_ministeriale_list):
        numero_ministeriale = numero_ministeriale_list[i]
    else:
        print("Warning: Not enough numero_ministeriale values for the number of images!")
        break

    # Load the image using OpenCV
    image_path = os.path.join(image_directory, image_filename)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Failed to load image: {image_filename}")
        continue

    # Calculate the average RGB values
    average_color = cv2.mean(image)[:3]  # Get the mean value of the image in BGR format
    image_B, image_G, image_R = average_color  # OpenCV loads images as BGR

    # Update the database with the calculated RGB values
    cursor.execute('''
    UPDATE traffic_signals 
    SET image_R = ?, image_G = ?, image_B = ? 
    WHERE numero_ministeriale = ?
    ''', (int(image_R), int(image_G), int(image_B), numero_ministeriale))

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Database updated successfully!")
