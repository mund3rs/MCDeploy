import boto3
import json
import smtplib, ssl
import configparser

conf = configparser.ConfigParser()
conf.read('config.ini')

def send_ip(ip_address, user_email):
    host = conf['Email']['host']
    port = conf['Email']['port']
    server_email=conf['Minecraft']['server_email']
    password=conf['Minecraft']['appkey']
    
    context = ssl.create_default_context()

    message=f"""\
        Subject: Your Minecraft Server IP - {ip_address}

        From: {server_email}

        Yey! Your Minecraft server is now ready. Connect using this IP: {ip_address}
        Your client needs to be running version 18.2
        """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(server_email, password)
        server.sendmail(server_email, user_email, message)

def start_ec2(user_email, serverType):
#Access AWS credentials via AWS secret manager
    secret_name = conf['AWS']['secret_name']
    secret_manager_client = boto3.client('secretsmanager')

    print(serverType)

    try:
        get_secret_value_response = secret_manager_client.get_secret_value(SecretId=secret_name)
        print(get_secret_value_response)
        secret = json.loads(get_secret_value_response['SecretString'])
        aws_access_key = secret['aws_access_key']
        print(aws_access_key)
        aws_secret_key = secret['aws_secret_key']
        region = secret['region']
    except Exception as e:
        print('Error getting credetentials: '+str(e))
        exit()

    #set id of predefined image of Minecraft server 
    amiID = conf['EC2']['ami_id']
    instanceType = conf['EC2']['instance_type']

    #start ec2 service
    ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key,aws_secret_access_key=aws_secret_key,region_name=region)

    try:
        response = ec2.run_instances(
            ImageId=amiID,
            MinCount=1,
            MaxCount=1,
            InstanceType=instanceType,

        )
        #get instance id
        instance_id = response['Instances'][0]['InstanceId']
        #wiat until instance is running
        w = ec2.get_waiter('instance_running')
        w.wait(InstanceIds=[instance_id])
        #get public IP4
        describe_response = ec2.describe_instances(InstanceIds=[instance_id])
        ip_address = describe_response['Reservations'][0]['Instances'][0]['PublicIpAddress']
        #send ip to user
        send_ip(ip_address,user_email)
        
    except Exception as e:
        print('Error initialising EC2 instance: ' + str(e))




