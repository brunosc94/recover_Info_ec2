import boto3
from mypy_boto3_ec2.service_resource import Vpc

ec2 = boto3.resource('ec2')
sg = ec2.security_groups('GroupName')
vpc = ec2.vpcs()

i = 1
for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':

        print(
            "Instância " + str(i) + "\nId: {0}\nSecurity Group: {1}\nVpc: {2}\nInstance Type: {3}\nState: {4}\n".format(
                instance.id, instance.security_groups, instance.vpc, instance.instance_type, instance.state
            )
        )
    i += 1
