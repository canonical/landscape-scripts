#!/bin/bash

PRO_STATUS="/var/tmp/pro-status.yaml"

pro_status(){
  pro status --format yaml > $PRO_STATUS
  PRO_ATTACH=$(awk '/machine_id/{print $NF}' $PRO_STATUS)
}

annotation(){
  pro_status

  if [[ $PRO_ATTACH == 'null' ]]; then
    echo "attachedfalse" > /var/lib/landscape/client/annotations.d/$1
    echo "'pro status' reports this machine is not attached to an Ubuntu Pro subscription."
  else
    echo "attachedtrue" > /var/lib/landscape/client/annotations.d/$1
    echo "'pro status' reports Ubuntu Pro is attached to:"
    awk '/contract:/,/tech_support_level:/{print}' $PRO_STATUS
  fi

  chown landscape:landscape /var/lib/landscape/client/annotations.d/$1

  if [[ -s $PRO_STATUS ]]; then rm $PRO_STATUS; fi
}

annotation ubuntu-pro
