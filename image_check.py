import boto3

client = boto3.client('rekognition')

with open('pc.jpg', 'rb') as image:
    response = client.detect_labels(Image={'Bytes': image.read()})

for label in response['Labels']:
    if label['Name'] == 'Computer' or label['Name'] == 'Monitor':
        print(f"Detected a {label['Name']} with confidence {label['Confidence']}")
