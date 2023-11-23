#!/usr/bin/env python3

# Prints the number of ESM updates that the instance can see, but not
# install because it does not have the relevant ESM service enabled.
# This helps administrators to identify and prioritise the enablement
# of ESM across a fleet.
import os
import sys

try:
    from uaclient.api.u.pro.packages.updates.v1 import updates
    from uaclient.api.u.pro.status.enabled_services.v1 import enabled_services

except ImportError:
    # Most likely a newer version of the pro client (ubuntu-advantage-tools) is required.
    print("Unable to find up-to-date Pro client. Try running 'apt install ubuntu-advantage-tools' on the instance.")
    sys.exit(os.EX_UNAVAILABLE)

# Some of these calls to the pro api can take time and we have a 10 second limit on Landscape scripts
# so we will call the endpoints once and reuse the results
update_information_summary = updates().summary
enabled_pro_services_list = list(i.name for i in enabled_services().enabled_services)

unpatchable_esm_updates = 0

if ("esm-infra" not in enabled_pro_services_list):
    unpatchable_esm_updates += update_information_summary.num_esm_infra_updates

if ("esm-apps" not in enabled_pro_services_list):
    unpatchable_esm_updates += update_information_summary.num_esm_apps_updates

print(unpatchable_esm_updates)
