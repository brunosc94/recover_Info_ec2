import boto3


def main():

    ec2 = boto3.resource('ec2')

    
    count = 1

    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            instance_id = None
            instance_type = None
            instance_state = None
            availability_zone = None
            subnet_id = None
            subnet_rt_associations = []
            subnet_rt_entries = []
            vpc_id = None
            vpc_filter = None
            vpc_nacl = None
            vpc_nacl_id = []
            vpc_nacl_entries = []
            security_group = []
            sg_ip_permission = []
            sg_ip_permission_egress = []
            client_ec2 = instance.meta.client
            for instance_description in client_ec2.describe_instances(InstanceIds=[instance.id])['Reservations']:
                # EC2 Informations
                current_instance = instance_description['Instances']
                for ins in current_instance:
                    instance_state = ins['State']["Name"]
                    instance_id = ins['InstanceId']
                    instance_type = ins['InstanceType']
                    availability_zone = ins['Placement']["AvailabilityZone"]
                    vpc_id = ins['VpcId']
                    subnet_id = ins['SubnetId']
                    for sg in ins['SecurityGroups']:
                        security_group.append(sg)

                # NACL Informations of Subnet
                vpc_nacl = client_ec2.describe_network_acls(Filters= [
                    {
                        'Name': 'association.subnet-id',
                        'Values': [subnet_id]
                    }
                ])['NetworkAcls']
                for nacl in vpc_nacl:
                    vpc_nacl_id.append(nacl['NetworkAclId'])
                    nacl_entries = nacl['Entries']
                    for entries in nacl_entries:
                        vpc_nacl_entries.append(entries)

                # Subnet Route Table Informations
                subnet_route_table = client_ec2.describe_route_tables(Filters=[
                    {
                        'Name': 'route.instance-id',
                        'Values': [instance_id]
                    }
                ])['RouteTables']
                for subnet_rt in subnet_route_table:
                    for associations in subnet_rt['Associations']:
                        subnet_rt_associations.append(
                            {'Main': 'associations["Main"]', 'RouteTableId': 'associations["RouteTableId"]', 'SubnetId': 'associations["SubnetId"]'})
                    subnet_rt_entries.append(subnet_rt['Entries'])

                # Security Group Informations CORRIGIR OUTPUT
                for sg_describe in security_group:
                    sg_permission = client_ec2.describe_security_groups(Filters=[
                        {
                            'Name': 'group-id',
                            'Values': [sg_describe['GroupId']]
                        }
                    ])['SecurityGroups']
                    for sg_rules in sg_permission:
                        for sg_inb in sg_rules['IpPermissions']:
                            #### APAGAR ESSE PRINT ABAIXO DE TESTE
                            print(sg_inb)
                            for value in sg_inb:
                                sg_ip_permission.append(value)
                        for sg_egr in sg_rules['IpPermissionsEgress']:
                            for value in sg_egr:
                                sg_ip_permission_egress.append(value)

                print(
                    f"################ INSTANCE {count} ################\n"
                    f"* INSTANCE STATE: {instance_state}\n"
                    f"* INSTANCE ID: {instance_id}\n"
                    f"* INSTANCE TYPE: {instance_type}\n"
                    f"* AVAILABITLITY ZONE: {availability_zone}\n"
                    f"* VPC ID: {vpc_id}\n"
                    f"* SUBNET: {subnet_id}"
                )
                print("* NACL IDs:")
                for p in vpc_nacl_id:
                    print(p)
                print("* NACL RULES:")
                for p in vpc_nacl_entries:
                    print(p)
                print("* SUBNET ROUTE TABLES:")
                for p in subnet_rt_associations:
                    print(p)
                print("* SUBNET ROUTE TABLES RULES:")
                for p in subnet_rt_entries:
                    print(p)
                print("* SECURITY GROUPS:")
                for p in security_group:
                    print(p)
                print("* SECURITY GROUP INBOUND PERMISSION:")
                for p in sg_ip_permission:
                    print(p)
                print("* SECURITY GROUP EGRESS PERMISSION:")
                for p in sg_ip_permission_egress:
                    print(p)
                print("-------------------------------\n")
                count += 1

    # Verificação se há alguma instância ligada
    if count == 1:
        print('No instances connected in this region')


if __name__ == '__main__':
    main()