#!/bin/bash
ESMannotations() {
  local UASTATUS
  local UANOTATTACHED
  UASTATUS=$(ua status)
  UANOTATTACHED=$(echo "$UASTATUS" | grep -c 'This machine is not attached to a UA subscription.')
  if [[ $UANOTATTACHED -eq 1 ]]; then
    echo 'unavailable' > /var/lib/landscape/client/annotations.d/esm-infra
    echo "'ua status' reports this machine is not attached to a UA subscription."
  else
    servicestatus "$UASTATUS" 'esm-infra' > /var/lib/landscape/client/annotations.d/esm-infra
    echo "'ua status' reports ESM is $(servicestatus "$UASTATUS" 'esm-infra')"
  fi
  chown landscape: /var/lib/landscape/client/annotations.d/esm-infra
}
servicestatus() {
  echo "$1" | grep -m 1 "$2" | awk '{ print $3 }' | sed 's/\xE2\x80\x94/unavailable/'
}
ESMannotations