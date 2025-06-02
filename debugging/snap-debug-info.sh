#!/bin/bash

# This script collects information about the status of a device to aid in debugging.
# There is a slight limitation when trying to extract logs using the journalctl
# command. 
#
# If your Landscape snap is based on Core 22 and your device is Core 24, you will not
# be able to extract logs using the journalctl command. This is because the journalctl
# command does not support the log format used by Core 24. 
# 
# If you are using Core 24, you can resolve this by using a Landscape client track 
# that is based on Core 24.


# Collect snapd information
# PRINT DEBUG INFO
echo "SNAP DEBUG INFO REPORT"
echo "================================="
echo ""
echo "UTC DATE:"
echo "================================="
date --utc

echo "UPTIME:"
echo "================================="
uptime -p

echo "DISK SPACE:"
echo "================================="
df -h

# System Logs
echo "SNAPD JOURNAL OUTPUT:"
echo "================================="
journalctl -u snapd --no-pager

echo ""
echo "SNAPD JOURNAL DENIED OUTPUT:"
echo "================================="
# Filter journal output for lines containing "DENIED"
journalctl -u snapd --no-pager | grep "DENIED"

echo ""
echo "SNAPD PROCESS INFORMATION:"
echo "================================="
ps -ax | grep snapd


# Run Python script to collect snapd information

python3 << END
import socket
import pprint
import json
from http.client import HTTPResponse
from io import BytesIO
import errno

BASE_URL = "http://localhost/v2"
SNAPD_SOCKET = "/run/snapd.socket"


def print_services(apps, indent=0):
    for app in apps:
        line = (
            " " * indent +
            f"- {app['name']} "
            f"(snap: {app['snap']}, "
            f"active: {app['active']}, "
            f"enabled: {app['enabled']})"
        )
        print(line)


def make_API_call(method, path):
    sock = socket.socket(family=socket.AF_UNIX)
    try:
        sock.connect(SNAPD_SOCKET)
    except socket.error as e:
        if e.errno in (errno.ECONNREFUSED, errno.ENOENT, errno.ETIMEDOUT):
            raise Exception(f"Could not connect to snapd socket: {e}")
        else:
            raise

    url = BASE_URL + path
    response = HTTPResponse(sock, method=method, url=url)

    request = BytesIO()
    request.write(
        f"{method} {url} HTTP/1.1\r\nHost: localhost\r\n\r\n".encode())

    sock.sendall(request.getvalue())
    response.begin()
    response_body = response.read()
    response.close()
    sock.close()

    response_type = response.getheader("Content-Type")
    if response_type == "application/json":
        return json.loads(response_body)["result"]
    else:
        response_code = response.getcode()
        is_async = response_code == 202
        return {
            "type": "async" if is_async else "sync",
            "status_code": response_code,
            "result": response_body,
        }

print("\nSystem Information:")
print("=================================")
pprint.pprint(make_API_call("GET", "/system-info"))

# Get SnapD Info
print("\nModel and Serial Information:")
print("=================================")
pprint.pprint(make_API_call("GET", "/model/serial"))

print("\nInstalled Snap Information:")
print("=================================")
pprint.pprint(make_API_call("GET", "/apps"))

print("\nSnap Services Information:")
print("=================================")
response_json = make_API_call("GET", "/apps")

# Extract the JSON part from the HTTP response

filtered = [
    {
        "name": app.get("name"),
        "snap": app.get("snap"),
        "active": app.get("active"),
        "enabled": app.get("enabled"),
    }
    for app in response_json
    if "daemon" in app
]

print_services(filtered)

print("\nInterface Connection Information:")
print("=================================")
pprint.pprint(make_API_call("GET", "/connections"))

print("\nSnapD Changes Information:")
print("=================================")
pprint.pprint(make_API_call("GET",  "/changes?select=all"))

print("\nValidation Sets Information:")
print("=================================")
pprint.pprint(make_API_call("GET", "/validation-sets"))

END