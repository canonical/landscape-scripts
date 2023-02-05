#!/bin/bash
livepatchannotations() {
  local UASTATUS
  local UANOTATTACHED
  UASTATUS=$(pro status)
  UANOTATTACHED=$(echo "$UASTATUS" | grep -c 'This machine is not attached')
  if [[ $UANOTATTACHED -eq 1 ]]; then
    echo 'unavailable' > /var/lib/landscape/client/annotations.d/livepatch
    echo "'pro status' reports this machine is not attached to an Ubuntu Pro subscription."
  else
    servicestatus 'livepatch' > /var/lib/landscape/client/annotations.d/livepatch
    echo "'pro status' reports livepatch is $(servicestatus 'livepatch')"
  fi
  chown landscape: /var/lib/landscape/client/annotations.d/livepatch
}
servicestatus() {
  echo "$UASTATUS" | grep -m 1 "$1" | awk '{ print $3 }' | sed 's/\xE2\x80\x94/unavailable/'
}
livepatchannotations
