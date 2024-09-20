#!/bin/env python3

import argparse
import subprocess
import json

# TODO: Logging config


def search_for_crypt(block_device):
    if "children" in block_device:
        for child in block_device["children"]:
            crypt = search_for_crypt(block_device=child)
            if crypt is not None:
                return crypt
    if "crypt" == block_device.get("type", ""):
        return block_device["name"]

    return None


def wipe(safety_on=True, cycles=10):
    if safety_on:
        print("Safety on - not firing")
        return

    block_devices = json.loads(subprocess.check_output("lsblk --json".split(" ")))
    crypts = []
    for block_device in block_devices["blockdevices"]:
        if crypt := search_for_crypt(block_device):
            crypts.append(crypt)
    for crypt in crypts:
        subprocess.check_call(f"sudo cryptsetup erase /dev/mapper/{crypt}".split(" "))
    subprocess.call("sudo shutdown now".split(" "))


parser = argparse.ArgumentParser("Disk destruction tool.")
parser.add_argument(
    "--safety-on", default=True, dest="safety", action=argparse.BooleanOptionalAction
)


def main():
    args = parser.parse_args()
    wipe(safety_on=args.safety)

if __name__ == "__main__":
    main()
