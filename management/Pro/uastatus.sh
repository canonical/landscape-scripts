#!/bin/bash
uaannotations() {
  local UASTATUS
  local UANOTATTACHED
  UASTATUS=$(ua status)
  UANOTATTACHED=$(echo "$UASTATUS" | grep -c 'This machine is not attached to a UA subscription.')
  if [[ $UANOTATTACHED -eq 1 ]]; then
    echo 'unattached' > /var/lib/landscape/client/annotations.d/ua
  else
    echo 'attached' > /var/lib/landscape/client/annotations.d/ua
  fi
  chown landscape: /var/lib/landscape/client/annotations.d/ua
}
uaannotations