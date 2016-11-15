#!/bin/sh
id='3956891841188784'
comment='小宜已我们为您打造了与您优雅气质相符专属理财产品-宜定赢, 请点击: http://www.yirendai.com/finance/list/1'
if [ $# == 1 ];then
	mid=$1
fi

echo 'mid:',$mid
echo 'commend:',$comment
curl -d "access_token=2.00DyZUyBv5KO5D94bb09a464TFSZWB&id=$mid&comment=$comment" "https://api.weibo.com/2/comments/create.json"
