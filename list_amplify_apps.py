import boto3

def list_amplify_apps(region):
    client = boto3.client('amplify', region_name=region)
    response = client.list_apps()
    return response['apps']

regions = [
    'us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'eu-central-1',
    'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ap-northeast-2',
    'sa-east-1', 'ca-central-1', 'eu-west-2', 'eu-west-3', 'eu-north-1',
    'ap-south-1', 'ap-east-1', 'me-south-1', 'af-south-1'
]

for region in regions:
    print(f"Checking region: {region}")
    apps = list_amplify_apps(region)
    if apps:
        for app in apps:
            print(f"App: {app['name']}, Region: {region}")

