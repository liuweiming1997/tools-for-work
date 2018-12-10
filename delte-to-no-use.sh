#!/bin/bash

set -e

prefix="/usr/local/bin/"
total=`ls | grep *.py`
echo "deleting .... ${total}"

cmd=""
for data in ${total[@]}
do
  cmd+="sudo rm -rf ${prefix}${data}"
done

echo ${cmd}

${cmd}

echo "ok......"

