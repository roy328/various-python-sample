from google.cloud import vision

def detect_computer_screen(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    objects = client.object_localization(image=image).localized_object_annotations

    for object in objects:
        if object.name.lower() in ['computer monitor', 'screen', 'display']:
            print(f"Detected a {object.name} with confidence {object.score}")
            # Here you can extract the bounding box coordinates
            # to crop the image to just the screen
            vertices = object.bounding_poly.normalized_vertices
            # Use these vertices to crop the original image
        else:
            print(object.name.lower())
    return objects

detect_computer_screen('pc.jpg')
