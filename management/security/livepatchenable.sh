#!/bin/bash
livepatchenable() {
  local LIVEPATCHENTITLEMENT
  local LIVEPATCHENABLED
  local UASTATUS
  local UANOTATTACHED
  UASTATUS=$(ua status)
  UANOTATTACHED=$(echo "$UASTATUS" | grep -c 'This machine is not attached to a UA subscription.')
  if [[ $UANOTATTACHED -eq 0 ]]; then
    LIVEPATCHENTITLEMENT=$(echo "$UASTATUS" | grep -m 1 'livepatch' | awk '{ print $2 }' | grep -c 'yes')
    if [[ $LIVEPATCHENTITLEMENT -eq 1 ]]; then
      ua enable livepatch --assume-yes
      UASTATUS=$(ua status)
      echo "'ua status' reports livepatch is $(servicestatus 'livepatch')"
    fi
  fi
  servicestatus 'livepatch' > /var/lib/landscape/client/annotations.d/livepatch
  chown landscape: /var/lib/landscape/client/annotations.d/livepatch
  LIVEPATCHENABLED=$(servicestatus 'livepatch' | grep -c 'enabled')
  if [[ $LIVEPATCHENABLED -eq 0 ]]; then
    exit 1
  fi
}
servicestatus() {
  echo "$UASTATUS" | grep -m 1 "$1" | awk '{ print $3 }' | sed 's/\xE2\x80\x94/unavailable/'
}
livepatchenable