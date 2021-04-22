# This script grabs all running EC2 instances and then looks up the name of the AMI that they are running on

import boto3
ec2 = boto3.resource('ec2')
ami_list = {}
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
    if instance.image.id not in ami_list.keys():
        try:
            ami_name = ami_lookup(instance.image.id)
        except:
            ami_name = "Unknown"
        ami_list[instance.image.id] = ami_name

for ami in ami_list:
    print(
        "AMI ID: {0}\nAMI Name: {1}\n".format(
        ami, ami_list[ami] 
        )
    )

