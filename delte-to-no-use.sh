#!/bin/bash

set -e

prefix="/usr/local/bin/"
total=`ls | grep .py`
echo "deleting .... ${total}"

for data in ${total[@]}
do
  cmd=""
  cmd+="sudo rm -rf ${prefix}${data}"
  echo ${cmd}
  ${cmd}
done

echo "ok......"

