#!/bin/bash
fipsdisable() {
  local FIPSENABLED
  local UASTATUS
  local UANOTATTACHED
  UASTATUS=$(ua status)
  UANOTATTACHED=$(echo "$UASTATUS" | grep -c 'This machine is not attached to a UA subscription.')
  if [[ $UANOTATTACHED -eq 0 ]]; then
    ua disable fips --assume-yes
    UASTATUS=$(ua status)
    echo "'ua status' reports FIPS is $(servicestatus 'fips')"
    shutdown -r 1 &
  fi
  fipsannotations "$UASTATUS" "$UANOTATTACHED"
  FIPSENABLED=$(servicestatus 'fips' | grep -c 'enabled')
  if [[ $FIPSENABLED -eq 1 ]]; then
    exit 1
  fi
}
fipsannotations() {
  if [[ $2 -eq 1 ]]; then
    echo 'unavailable' > /var/lib/landscape/client/annotations.d/fips
    echo 'unavailable' > /var/lib/landscape/client/annotations.d/fips-updates
  else
    servicestatus 'fips' > /var/lib/landscape/client/annotations.d/fips
    servicestatus 'fips-updates' > /var/lib/landscape/client/annotations.d/fips-updates
  fi
  chown landscape: /var/lib/landscape/client/annotations.d/fips
  chown landscape: /var/lib/landscape/client/annotations.d/fips-updates
}
servicestatus() {
  echo "$UASTATUS" | grep -m 1 "$1" | awk '{ print $3 }' | sed 's/\xE2\x80\x94/unavailable/'
}
fipsdisable