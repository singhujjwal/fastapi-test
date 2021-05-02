# export IP_ADDR=$(curl -s http://instance-data/latest/meta-data/local-ipv4)/32

# For Azure
# export IP_ADDR=$(curl -s -H Metadata:true 'http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/privateIpAddress?api-version=2017-08-01&format=text')/32

# For local
export IP_ADDR=$(ifconfig eth1 | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d:)/32
