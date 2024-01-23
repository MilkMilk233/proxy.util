import boto3

def acquire_aws_ip() -> str:
    client = boto3.client('ec2')
    response = client.describe_addresses()
    new_ip = response['Addresses'][0]['PublicIp']
    return new_ip

def change_aws_ip() -> str:
    client = boto3.client('ec2')
    response = client.describe_addresses()
    instanceId = response['Addresses'][0]['InstanceId']
    old_alloc_id = response['Addresses'][0]['AllocationId']
    old_asso_id = response['Addresses'][0]['AssociationId']
    response = client.allocate_address()
    new_alloc_id = response['AllocationId']
    new_ip = response['PublicIp']
    response = client.disassociate_address(
        AssociationId=old_asso_id
    )
    response = client.release_address(
        AllocationId=old_alloc_id
    )
    response = client.associate_address(
        AllocationId=new_alloc_id,
        InstanceId=instanceId
    )
    return new_ip

def process_aws(server) -> str:
    return acquire_aws_ip()