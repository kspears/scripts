# This script grabs all running EC2 instances and then looks up the name of the AMI that they are running on

import boto3
ec2 = boto3.resource('ec2')
ami_list = []
def ami_lookup(ami_id):
    image_iterator = ec2.images.filter(
        ImageIds=[
                    ami_id
                ]
    )
    ami_name = next(iter(image_iterator)).name
    return ami_name

    
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    try:
        ami_name = ami_lookup(instance.image.id)
    except:
        ami_name = "None"

    print(
        "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nAMI Name: {5}\nState: {6}\n".format(
        instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, ami_name, instance.state, 
        )
    )

