#!/bin/bash

set -e

total=`ls | grep *.py`
echo "sending .... ${total}"
#sudo cp ${total} /usr/local/bin/

prefix="/usr/local/bin/"

cmd=""
for data in ${total[@]}
do
  cmd+="sudo cp ${data} ${prefix}"
done
echo ${cmd}
${cmd}

echo "ok......"

