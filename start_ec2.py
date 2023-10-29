import boto3
import json
from send_confirmation import send_confirmation


#Access AWS credentials via AWS secret manager
secret_name = "#####"

secret_manager_client = boto3.client('secretsmanager')

try:
    get_secret_value_response = secrest_manager_client.get_secret_value(SecretID=secret_name)
    secret = json.loads(get_secret_value_response['SecretString'])
    aws_access_key = secret['aws.access_key']
    aws_secret_key = secret['aws.secret_key']
    region_name = secret['region']
except Exceptiion as e:
    print('Error getting credetentials: {str(e)}')
    exit()

#set id of predefined image of Minecraft server 
amiID = "#######"

#start ec2 service
ec2.boto3.client('ec2', aws_access_key_id=aws_access_key,aws_secret_key=aws_secret_key,region_name=region_name)

try:
    response = ec2.run_instances(
        ImageId=amiID,
        MinCount=1,
        MaxCount=1
    )
    #Get instance id and ip to send email confirmation to user
    instance_id = response['Instances'][0]['InstanceId']
    instance_ip = response['Instances'][0]['']
    send_confirmation(instance_id,instance_ip)
except Exception as e:
    print('Error initialising EC2 instance: {str(e)}')