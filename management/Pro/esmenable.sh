#!/bin/bash
esmenable() {
  local ESMENTITLEMENT
  local ESMENABLED
  local UASTATUS
  local UANOTATTACHED
  UASTATUS=$(ua status)
  UANOTATTACHED=$(echo "$UASTATUS" | grep -c 'This machine is not attached to a UA subscription.')
  if [[ $UANOTATTACHED -eq 0 ]]; then
    ESMENTITLEMENT=$(echo "$UASTATUS" | grep -m 1 'esm-infra' | awk '{ print $2 }' | grep -c 'yes')
    if [[ $ESMENTITLEMENT -eq 1 ]]; then
      ua enable esm-infra --assume-yes
      UASTATUS=$(ua status)
      echo "'ua status' reports esm-infra is $(servicestatus 'esm-infra')"
    fi
  fi
  servicestatus 'esm-infra' > /var/lib/landscape/client/annotations.d/esm-infra
  chown landscape: /var/lib/landscape/client/annotations.d/esm-infra
  ESMENABLED=$(servicestatus 'esm-infra' | grep -c 'enabled')
  if [[ $ESMENABLED -eq 0 ]]; then
    exit 1
  fi
}
servicestatus() {
  echo "$UASTATUS" | grep -m 1 "$1" | awk '{ print $3 }' | sed 's/\xE2\x80\x94/unavailable/'
}
esmenable