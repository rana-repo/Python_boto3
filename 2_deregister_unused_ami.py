import boto3
Client = boto3.resourse('ec2')

instances =client.describe_instances()
used_ami = []
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_ami.append(instance['ImageID'])

print(used_ami)
# Remove duplicate ami
def remove_duplicate(amis):
    unique_ami = []
    for ami in amis:
        if ami not in unique_ami:
            unique_ami.append(ami)
    return unique_ami

unique_ami = remove_duplicate(used_ami)     
print(unique_ami)

# get custom ami's from the account.

custom_images = client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': ['available']
        },
    ],
    Owners= ['self'] #aws account id can also be set here
)

custom_ami_list = []
for image in custom_images['Images']:
    custom_ami_list.append(image['ImageId'])

for custom_ami in custom_ami_list:
    if custom_ami not in used_ami:
        print("Deregistering ami {}".format(custom_ami))
        # Delete unused AMIs
        client.client.deregister_image(ImageID=image['ImageId'])
