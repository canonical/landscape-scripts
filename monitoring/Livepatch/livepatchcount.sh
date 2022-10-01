#!/bin/bash
livepatchstatus() {
  local output
  output=$(/snap/bin/canonical-livepatch status --format json 2>/dev/null | grep -c "\"Patched\": true")
  echo "$output"
}
livepatchstatus