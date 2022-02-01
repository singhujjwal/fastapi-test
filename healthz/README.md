## A basic healthz server to test the LBs

## Setup on AMZN Lnx 2 

sudo yum update -y
sudo yum groupinstall "Development Tools" -y
sudo yum install openssl-devel libffi-devel bzip2-devel wget -y


amazon-linux-extras install python3.8


## Target group
Created a target group instance type
Health check on /api/v1/healthz/ on port 8121 
Target group comes healthy

## Load Balancer

Created a NLB
1. Listener on port 80 will also work and sending requests to again the same port as health check 
but urls decide,
Had to change the SG group for the loadbalancer :)

2. Listener on port 443, ACM certificate set for the domain name. (https://nlb.k8s.<my-domain>/api/v1/healthz/ this works fine)

This means just connection is ternminated at the NLB and traffic is forwarded to the 
target group on port ? I am thinking should be 443 but no 

3. Both have forwarding set for the target group instance

4. You can have advanced settings of the load balancer to override the actual traffic than the 
health check traffic
