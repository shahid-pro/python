#!/bin/bash

c=1
while [c!=4]
do
	echo "Enter choice"
	echo "1 Display Python path"
	echo "2 Display Bash path"
	echo "3 Display Proxy"
	echo "4 Exit"
	if [c==1]
		which Python
	elif [c==2]
		which bash
	elif [c==3]
		echo $http_proxy
	else
		echo "Wrong Choice"
	fi
done