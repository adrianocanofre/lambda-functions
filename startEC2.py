import boto3
region = 'us-east-1'

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    filters = [{
            'Name': 'tag:AutoOff',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }
    ]
    instances = ec2.instances.filter(Filters=filters)

    start_ec2 = [instance.id for instance in instances]
    if len(start_ec2) > 0:
        start = ec2.instances.filter(InstanceIds=instances).start()
	    print start
    else:
        print "No instances to be started found"
