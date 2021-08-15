import boto3

ec2 = boto3.resource('ec2')

i = 1
for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':
        print(
            "Instância " + str(i) + "\nId: {0}\nInstance Type: {1}\nSecurity Group: {2}\nVpc: {3}\nSubnets: {4}\nState: {5}\n".format(
                instance.id, instance.instance_type, instance.security_groups, instance.vpc, instance.subnet, instance.state
            )
        )
    i += 1
