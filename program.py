import boto3

def main():

    ec2 = boto3.resource('ec2')
    client_ec2 = ec2.meta.client

    i = 1
    for instance in ec2.instances.all():
        if instance.state['Name'] == 'running':
            
            #Alimentação das variáveis
            id_instancia = instance.id
            instance_type = instance.instance_type
            status_instance = instance.state
            id_subnet = instance.subnet_id
            vpc_id_bruto = instance.vpc_id
            vpc_id = client_ec2.describe_vpcs(Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [vpc_id_bruto]
                }
                ],
                MaxResults=5
            ).get('Vpcs', [{}])[0].get('VpcId')
            filtro_vpc = [
                {
                    'Name': 'vpc-id',
                    'Values': [vpc_id]
                }
                ]
            vpc_nacl = client_ec2.describe_network_acls(Filters=filtro_vpc)
            rt_subnet = client_ec2.describe_route_tables(Filters=[
                {
                    'Name': 'route.instance-id',
                    'Values': [id_instancia]
                }
                ],
                MaxResults=100
            )
            sg_id = client_ec2.describe_security_groups(Filters=filtro_vpc).get('SecurityGroups', [{}])[0].get('GroupId')
            sg_name = client_ec2.describe_security_groups(Filters=filtro_vpc).get('SecurityGroups', [{}])[0].get('GroupName')
            sg_ip_permission = client_ec2.describe_security_groups(Filters=filtro_vpc).get('SecurityGroups', [{}])[0].get('IpPermissions')
            sg_ip_permission_egress = client_ec2.describe_security_groups(Filters=filtro_vpc).get('SecurityGroups', [{}])[0].get('IpPermissionsEgress')

            #Imprindo no console os resultados
            print(
                f"#### INSTANCE {i} #####\n"
                f"STATE: {status_instance}\n"
                f"INSTANCE ID: {id_instancia}\n"
                f"INSTANCE TYPE: {instance_type}\n"
                f"VPC ID: {vpc_id}\n"
                f"SUBNET: {id_subnet}\n"
                f"VPC NACL: {vpc_nacl}\n"
                f"ROUTE TABLE SUBNET: {rt_subnet}\n"
                f"SECURITY GROUP ID: {sg_id}\n"
                f"SECURITY GROUP NAME: {sg_name}\n"
                f"SECURITY GROUP PERMISSION: {sg_ip_permission}\n"
                f"SECURITY GROUP PERMISSION EGRESS: {sg_ip_permission_egress}\n"
                f"-------------------------------\n"
            )
            i += 1

    if i == 1:
        print('Nenhuma instância ligada nessa região')


if __name__ == '__main__':
    main()
