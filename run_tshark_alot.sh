#/usr/local/bin/bash

for file in "$@";do echo "$file";tshark -r "$file" -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e ip.len -E header=y -E separator=, -E quote=d -E occurrence=f>> output.csv;done
