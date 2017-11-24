import argparse
import boto.ec2

access_key = ''
secret_key = ''

def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
    reservations = ec2_conn.get_all_reservations()
    for reservation in reservations:    
        for inst in reservation.instances:
            if inst.state=='running':
                print "set security address-book "+address_book, "address",inst.public_dns_name, inst.ip_address+"/32"



def main():
    regions = ['eu-west-1','eu-west-2','us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1',
                'ap-southeast-1','ap-southeast-2','ap-northeast-1']
    parser = argparse.ArgumentParser()
    parser.add_argument('access_key', help='Access Key');
    parser.add_argument('secret_key', help='Secret Key');
    parser.add_argument('address_book', help='Junos SRX Address book');

    args = parser.parse_args()
    global access_key
    global secret_key
    global address_book
    access_key = args.access_key
    secret_key = args.secret_key
    address_book = args.address_book
    
    for region in regions: get_ec2_instances(region)

if  __name__ =='__main__':main()
