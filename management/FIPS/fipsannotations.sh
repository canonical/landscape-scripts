#!/bin/bash
fipsannotations() {
  local UASTATUS
  local UANOTATTACHED
  UASTATUS=$(ua status)
  UANOTATTACHED=$(echo "$UASTATUS" | grep -c 'This machine is not attached to a UA subscription.')
  if [[ $UANOTATTACHED -eq 1 ]]; then
    echo 'unavailable' > /var/lib/landscape/client/annotations.d/fips
    echo 'unavailable' > /var/lib/landscape/client/annotations.d/fips-updates
    echo "'ua status' reports this machine is not attached to a UA subscription."
  else
    servicestatus 'fips' > /var/lib/landscape/client/annotations.d/fips
    echo "'ua status' reports FIPS is $(servicestatus 'fips')"
    servicestatus 'fips-updates' > /var/lib/landscape/client/annotations.d/fips-updates
    echo "'ua status' reports FIPS Updates is $(servicestatus 'fips-updates')"
  fi
  chown landscape: /var/lib/landscape/client/annotations.d/fips
  chown landscape: /var/lib/landscape/client/annotations.d/fips-updates
}
servicestatus() {
  echo "$UASTATUS" | grep -m 1 "$1" | awk '{ print $3 }' | sed 's/\xE2\x80\x94/unavailable/'
}
fipsannotations