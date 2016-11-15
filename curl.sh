#!/bin/sh
id='3956891841188784'
comment='test test test'
if [ $# == 1 ];then
	mid=$1
fi

echo 'mid:',$mid
echo 'commend:',$comment
curl -d "access_token=2.00DyZUyBv5KO5D94bb09a464TFSZWB&id=$mid&comment=$comment" "https://api.weibo.com/2/comments/create.json"
