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
            'Values': ['running']
        }
    ]
    instances = ec2.instances.filter(Filters=filters)

    stop_ec2 = [instance.id for instance in instances]
    if len(stop_ec2) > 0:
        stop = ec2.instances.filter(InstanceIds=instances).stop()
	    print stop
    else:
        print "No instances to be stopped found"
