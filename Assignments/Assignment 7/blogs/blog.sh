#!/bin/bash
counter=1
while [ $counter -le 100 ]
do
	url="$(curl -L -s -o /dev/null -w %{url_effective} 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117')"
	echo $url >> url.txt
	((counter++))
	echo counter
done