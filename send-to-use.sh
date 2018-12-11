#!/bin/bash

set -e

total=`ls | grep .py`
echo "sending .... ${total}"
#sudo cp ${total} /usr/local/bin/

prefix="/usr/local/bin/"

for data in ${total[@]}
do
  cmd=""
  cmd+="sudo cp ${data} ${prefix}"
  echo ${cmd}
  ${cmd}
done

echo "ok......"

