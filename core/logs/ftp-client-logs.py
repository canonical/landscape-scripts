#!/usr/bin/env python3
import os
from ftplib import FTP

SNAP_DATA = os.getenv("SNAP_DATA")

# connect and login to the FTP server
ftp = FTP("192.168.0.103")
ftp.login("username", "password")

# push all the landscape-client logs to the FTP server
log_files = [
    "broker.log",
    "manager.log",
    "monitor.log",
]
for log_file in log_files:
    with open(f"{SNAP_DATA}/var/log/landscape/{log_file}", "rb") as f:
        ftp.storbinary(f"STOR {log_file}", f)

ftp.quit()
