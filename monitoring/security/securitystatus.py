#!/usr/bin/env python3

import json
import subprocess
import sys

return_info = subprocess.check_output(["ua",  "security-status", "--format=json"])
json_output = return_info.decode(sys.stdout.encoding)
ua_security_status = json.loads(json_output)

if "esm-infra" not in ua_security_status["summary"]["ua"]["enabled_services"]:
    unpatchable_esm_infra = ua_security_status["summary"]["num_esm_infra_updates"]
else:    
    unpatchable_esm_infra = 0

if "esm-apps" not in ua_security_status["summary"]["ua"]["enabled_services"]:
    unpatchable_esm_apps = ua_security_status["summary"]["num_esm_apps_updates"]
else:
    unpatchable_esm_apps = 0    

total_unpatchable_esm_updates = unpatchable_esm_infra + unpatchable_esm_apps
print(total_unpatchable_esm_updates)