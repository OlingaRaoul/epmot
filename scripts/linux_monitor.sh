
#!/bin/bash

echo "CPU Usage:"
top -l 1 | grep "CPU usage"

echo "Memory Usage:"
vm_stat | awk 'NR==1{next} {gsub(/\\./,""); print $1, $2}'

echo "Disk Usage:"
df -h

echo "Network Stats:"
netstat -i

