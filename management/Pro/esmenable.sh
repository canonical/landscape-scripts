#!/bin/bash

PRO_STATUS="/var/tmp/pro-status.yaml"

pro_status(){
  pro status --format yaml > $PRO_STATUS
  PRO_ATTACH=$(awk '/machine_id/{print $NF}' $PRO_STATUS)
  SRV_STATUS=$(grep -A2 -B5 "^..name:.$1" $PRO_STATUS | awk '/status:/{print $NF}')
}

annotation(){
  echo $SRV_STATUS > /var/lib/landscape/client/annotations.d/$1
  echo "'pro status' reports $1 is $SRV_STATUS"
  chown landscape:landscape /var/lib/landscape/client/annotations.d/$1
}

pro_service(){
  pro_status $1
  if [[ $PRO_ATTACH == 'null' ]]; then
    SRV_STATUS="unavailable"
    annotation $1
    echo "'pro status' reports this machine is not attached to an Ubuntu Pro subscription."
    exit 1
  elif [[ ! $SRV_STATUS =~ $2 ]]; then
    pro $2 $1 --assume-yes
    pro_status $1
  fi
  annotation $1
  if [[ -s $PRO_STATUS ]]; then rm $PRO_STATUS; fi
  if [[ ! $SRV_STATUS =~ $2 ]]; then exit 2; fi
}

pro_service esm-infra enable

