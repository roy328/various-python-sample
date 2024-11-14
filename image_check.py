import os
import boto3

os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'  # Replace with your desired region
client = boto3.client('kms')

with open('1.png', 'rb') as image:
    response = client.detect_labels(Image={'Bytes': image.read()})

for label in response['Labels']:
    if label['Name'] == 'Computer' or label['Name'] == 'Monitor':
        print(f"Detected a {label['Name']} with confidence {label['Confidence']}")
