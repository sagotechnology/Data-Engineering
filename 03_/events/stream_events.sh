#!/bin/sh
"""
This is a bash shell script counter.  It executes the commands to generate events using Apache Bench.  The counter value is incorporated into the host ID to create 
unique users.  The sleep command halts the while loop for five seconds.  It takes about five minutes to generate two hundred events.
"""
count=1
while [ $count -lt 51 ]
do
    docker-compose exec mids ab -H "Host: user$count.comcast.com" http://localhost:5000/join_guild
    docker-compose exec mids ab -H "Host: user$count.att.com" http://localhost:5000/join_guild
    docker-compose exec mids ab -H "Host: user$count.comcast.com" http://localhost:5000/purchase_a_sword
    docker-compose exec mids ab -H "Host: user$count.att.com" http://localhost:5000/purchase_a_sword
    let "count++"
    sleep 5
done
