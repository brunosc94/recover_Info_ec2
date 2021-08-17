import boto3


def main():

    ec2 = boto3.resource('ec2')

    i = 1
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            print(
                f"Instância {i}\n" 
                f"Id: {instance.id}\n"
                f"Instance Type: {instance.instance_type}\n"
                f"Security Group: {instance.security_groups}\n"
                f"Vpc: {instance.vpc}\n"
                f"Subnets: {instance.subnet}\n"
                f"State: {instance.state}\n"
            )
            i += 1
    if i == 1:
        print('Nenhuma instância ligada nessa região')

if __name__ == '__main__':
    main()