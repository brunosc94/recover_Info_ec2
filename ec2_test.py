import boto3

REGION_NAME = 'us-east-1'
client = boto3.client('ec2', region_name=REGION_NAME)

print("***************INSTANCE INFORMATIONS***************")
for instances in client.describe_instances()['Reservations']:
    for instance in instances['Instances']:
        print('\n')
        print('Instance', instance['KeyName'], ':')
        print('\n')
        print('InstanceId:', instance['InstanceId'])
        print('InstanceType:', instance['InstanceType'])
        print('LaunchTime:', instance['LaunchTime'])
        print('SubnetId:', instance['SubnetId'])
        print('VpcId:', instance['VpcId'])
        print('SecurityGroups:', instance['SecurityGroups'])
        print('placement:', instance['Placement'])
        print('PrivateDnsName:', instance['PrivateDnsName'])
        print('PrivateIpAddress:', instance['PrivateIpAddress'])
        print('\n')


print("***************SECURITY GROUP INFORMATIONS***************")
for sgs in client.describe_security_groups()['SecurityGroups']:
    if sgs['GroupName'] != 'default':
        print('\n')
        print('SG', sgs['GroupName'], ':')
        print('\n')
        print('Description:', sgs['Description'])
        for sg in sgs['IpPermissions']:
            print('Inbound:')
            print('FromPort:', sg['FromPort'])
            print('IpProtocol:', sg['IpProtocol'])
            for ipi in sg['IpRanges']:
                print('CidrIp:', ipi['CidrIp'])
        for sg in sgs['IpPermissionsEgress']:
            print('Outbound:')
            for ipo in sg['IpRanges']:
                print('CidrIp:', ipo['CidrIp'])
        print('VpcId:', sgs['VpcId'])
        print('\n')


print("***************VPC INFORMATIONS***************")
for vpcs in client.describe_vpcs()['Vpcs']:
    print('\n')
    print('VPC ID', vpcs['VpcId'], ':')
    print('\n')
    print('State:', vpcs['State'])
    print('CidrBlock:', vpcs['CidrBlock'])
    print('OwnerId:', vpcs['OwnerId'])
    print('\n')
    print("************************************")


print("***************SUBNET INFORMATIONS***************")
subnetids = []
for subnets in client.describe_subnets()['Subnets']:
    print('\n')
    print('SubnetId', subnets['SubnetId'], ':')
    print('\n')
    print('VpcId:', subnets['VpcId'])
    print('OwnerId:', subnets['OwnerId'])
    print('AvailabilityZone:', subnets['AvailabilityZone'])
    print('CidrBlock:', subnets['CidrBlock'])
    print('State:', subnets['State'])
    print('\n')
    print("************************************")
    subnetids.append(subnets['SubnetId'])


print("***************NACL INFORMATIONS***************")
for nacls in client.describe_network_acls()['NetworkAcls']:
    for association in nacls['Associations']:
        if association['SubnetId'] in subnetids:
            print('\n')
            print('NetworkAclId', association['NetworkAclId'], ':')
            print('SubnetId:', association['SubnetId'])
            print('\n')
            print("************************************")

print("***************ROUTE TABLE INFORMATIONS***************")
for rt in client.describe_route_tables()['RouteTables']:
    print('\n')
    print('RouteTableId', rt['RouteTableId'], ':')
    print('\n')
    for associantions in rt['Associations']:
        print('RouteTableAssociationId:',
              associantions['RouteTableAssociationId'])
    print('Routes:', rt['Routes'])
    print('VpcId:', rt['VpcId'])
    print('\n')
    print("************************************")