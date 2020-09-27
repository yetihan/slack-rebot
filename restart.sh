pids=`ps aux | grep message_server.py | grep python | awk '{print $2}'`

echo "pids: ${pids}"

for pid in ${pids}
do
    s="kill -9 ${pid}"
    echo ${s}
    ${s}
done

mkdir -p log
echo "restart server " >> log/server.log
nohup python message_server.py >> log/server.log &

