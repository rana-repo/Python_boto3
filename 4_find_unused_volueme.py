import boto3

ec2_client = boto3.client('ec2')
sns_Client = boto3.client('sns') 
volumes = ec2_client.describe_volumes()
sns_arn = 'paste your topic arn'

def lambda_handler(event,context):
    unused_vols = []
    for volume in volumes['Volumes']:
        if len(volume['Attachments']) == 0:
            unused_vols.append(volume['VolumeId'])
            print(volume)

    email_body = "Unused Volumes \n"

    for vol in unused_vols:
        email_body= email_body + "VolumeId = {} \n".format(vol)

    # send Email

    sns_client.publish(
        TopicArn = sns_arn,
        Subject = 'Unused Volumes',
        Message = email_body
    )
