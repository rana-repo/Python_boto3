import boto3
import os

client = boto3.client('ec2')
secClient = boto3.client('ses')    # Simple Email Service Client.

# Accessing Envionment variables declared in lambda function.
SOURCE_EMAIL = os.environ['SOURCE_EMAIL']
DEST_EMAIL = os.environ['DEST_EMAIL']

def lambda_handler(event,context):
    response = client.describe_addresses()
    eips=[]
    for eip in response['Addresses']:
        if 'InstanceId' not in eip:
            eips.append(eip['PublicIp'])
    
    # print(eips)

    # send email using AWS Simple Email Service.

    if eips: #eip arrray is not empty
        sesClient.send_emails(
            Sourse = SOURCE_EMAIL,
            Destination={
                'ToAddresses': [
                    DEST_EMAIL
                ]
            },
            MESSAGE={
                'Subject': {
                    'Data': 'Unused EIPS',
                    'Charset': 'utf-8'
                },
                'Body': {
                    'Text': {
                        'Data': str(eips),
                        'Charset': 'utf-8'
                    }
                }
            }
        )
