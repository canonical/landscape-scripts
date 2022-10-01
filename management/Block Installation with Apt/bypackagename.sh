#!/bin/bash
bash -c 'cat <<EOF > /etc/apt/preferences.d/audacity.pref
Package: audacity
Pin: release *
Pin-Priority: -1
EOF'