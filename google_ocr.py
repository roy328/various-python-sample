# from google.cloud import vision
# from google.oauth2 import service_account

# # Load the service account key
# credentials = service_account.Credentials.from_service_account_file('path/to/your-service-account-file.json')

# # Initialize the Vision API client
# client = vision.ImageAnnotatorClient(credentials=credentials)

# # Load the image from a file
# with open('path_to_image.jpg', 'rb') as image_file:
#     content = image_file.read()

# image = vision.Image(content=content)

# # Call the Vision API for text detection
# response = client.text_detection(image=image)

# # Extract detected text
# texts = response.text_annotations
# if texts:
#     print('Detected text:')
#     print(texts[0].description)  # the first item contains the full detected text

# if response.error.message:
#     raise Exception(f'{response.error.message}')


# Imports the Google Cloud client library
from google.cloud import vision



def run_quickstart() -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The URI of the image file to annotate
    file_uri = "11.png"

    image = vision.Image()
    image.source.image_uri = file_uri

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print("Labels:")
    for label in labels:
        print(label.description)

    return labels

run_quickstart()
