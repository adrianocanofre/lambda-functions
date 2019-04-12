import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    
    filters = [{
            'Name': 'tag:AutoStartStop',
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
        shuttingDown = ec2.instances.filter(InstanceIds=start_ec2).start()
    else:
        print "No instances to be started found"
