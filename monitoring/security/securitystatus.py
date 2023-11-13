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

    unpatchable_esm_updates = 0

    if (not any(i.name == "esm_infra" for i in enabled_services().enabled_services)) and (updates().summary.num_esm_infra_updates > 0):
        unpatchable_esm_updates += updates().summary.num_esm_infra_updates

    if (not any(i.name == "esm_apps" for i in enabled_services().enabled_services)) and (updates().summary.num_esm_apps_updates > 0):
        unpatchable_esm_updates += updates().summary.num_esm_apps_updates

    print(unpatchable_esm_updates)
    sys.exit(os.EX_OK)

except ImportError:
    # Most likely a newer version of the pro client (ubuntu-advantage-tools) is required.
    # Return 99 so that someone takes a look.
    print("Unable to find up-to-date Pro client. Try running 'apt install ubuntu-advantage-tools' on the instance.")
    sys.exit(os.EX_UNAVAILABLE)
