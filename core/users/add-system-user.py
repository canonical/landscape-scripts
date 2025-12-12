#!/usr/bin/env python3

from landscape.client import snap_http

# Both the account and account-key assertions are required to be acknowledged
# on the target device in order for system user creation to succeed. All three
# assertions can be included in the same request. Therefore, it is recommended
# to sign system-user assertions with:
# snap sign -k <key name> --chain system-user.json > auto-import.assert
# The below is an example system-user, account-key, and account assertion.
# Please create your own.
assertion = """type: system-user
authority-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
brand-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
email: jane@example.com
models:
  - ubuntu-core-22-amd64
name: Jane Doe
password: >
    $6$goodsoup$XerhNYrEA8Qe5nmUaEQ4F./n2FHmjgs6qc2s513bnpv6IFqDjMxLktRfitQF
    jGiNXfqJWscy7His.QG1l8G7W1
series:
  - 16
since: 2024-02-08T09:14:00+00:00
system-user-authority: *
until: 2038-01-19T03:14:07+00:00
username: jane
sign-key-sha3-384: >
    ncl1u5VJlEitiCt_XeGJ0FMLwWeXLw35r8VvWifR_5Vxeu2q1hYdkGcQZ6DURx1S

AcLBcwQAAQoAHRYhBOt0YHzas+IX2LgSYemrEyH88NiPBQJlxKCMAAoJEOmrEyH88NiPn+gP/3im
+YdXT+A6ZYh5gDaBhvogTB4b57LslWTwBBBoFaYvhkYzKZkFuiDvQvOUTGn3ZKBd23kvYqFXODXH
7lCjCBdOr10j24Yn+wpHelDPwzaGLNHc+2epFFiPHMu6sQyKBAC7Mvnn7LRa/hnDiJ+n5yLmnBWx
VmG+KqOGJa6UclW0nZqBBnmAoaPDRwoa6XCxK0jmhpCVtFRP/ZOh1I/N7/a2VYCNPSwgx9WeMtm1
adr+0unBRt4lsB1/BFoLQozRZF9klZsWDs3o8IxO9FPFEmPaSNeCWj5haS5GO55n5OI6s2nOl8ro
dFiGt+f6eQRSolhR7+pNZBQVGT95S8Cd2LCfThU3Pn1tM6oo56haLTx8uDhUyUlwRZLXyMK689jJ
701ChRvT7QYDksqdDwrKB/2/dxvDkuoRwuuGO0SowwdO5Dil9DFluVL0aq4BPs6CHjlbrngbVFfN
fINbBjAgZvYbcsY2AyDPX4nAXHZIRvXxDFcPTuYDmAP4zLlt0R3wiTMkpQq8c3dEKDq3Cd2UgwLb
s4ZW2IIyxYQzCe8L2ZXXy7aBsB9qMturxA9i2FizeTfO7OU1baHVgdxF8uSgF28F2T3xtA1ReciH
nzAQUNSvsvHSKb6REWEz0+blJQqFA46td/rwlTe7AKk+SlM4GWiI7lXYUZ5/iYTfM8TPzzG2

type: account-key
authority-id: canonical
public-key-sha3-384: DgQXPmlRwyQEqzQ5pg2t8m4tz3rmA4l3IjNto2w-fmChxPPlA91eTVvMKX7UlMks
account-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
name: system-user-key
since: 2023-01-12T19:29:25Z
body-length: 717
sign-key-sha3-384: BWDEoaqyr25nF5SNCvEv2v7QnM9QsfCc0PBMYD_i2NGSQ32EF2d4D0hqUel3m8ul

AcbBTQRWhcGAARAAuiX6q9jbFs8J7O8Ue3AqvcJc/oxU15Id5hYaXQ5qDE4Lm5s2ESqVBrEVPY35
i5wPxt5byAIRK5sV5urZ4XFIiLhHCBTOHn48UbesVQSkJmTXsGOT6A8BuS27FkLb3J6l3d+juQLh
OdzvLiswl5xFNbTEqSX6ha26QIHomn/L9Pml1VuwxNHHM6MeFvUpdHkv9Y+w+4Tf8+2vo/dt7UZL
AFKZ6gzZk2RHHpMF/7xtPxhOhsC9LMI/ZKjuxW7q5O1dL4zWRWhGGGEqqUV+AKsOG8HQJSnv9ZVm
mMHf8XExJKQnfmdnVewCAKzr2B0CMQS9d3DonbAKRpXzmmNIUODnTbbtcxehQ01cBSZLlmsL75p2
AuXOnkFAyCVwKfErRHz3HTZwwKEfdnVbZfTpMByhSQCpRHNSU81LS5h/0P/MRuMcH8nSaV7fdl3C
tMf9Mp8VB9nNJWPt8aEyCQjT527SSV7nvReVYTQDIGOKtD7XH+tSENJ9nXKNbXty8IA5dQRxUBm7
zt7Zx2m1qcDHcvIqwmqFGDhg1JVxPg+fg1IOwyNJAkVLCtd9uAGqiOAGuMEJNkZdGA1OwDr6PUg4
tUu+u25/JPux1wiHmRC2ZstEuNpYZNEqcRe300YFREzSAk1JBS1ymzhupMHX9j5PaFep1R4CNXDM
0j/hcQX5EN3e3G0AEQEAAQ==

AcLBUgQAAQoABgUCY8BflQAAC8MQAM0M3XVERZnBBnSZISFc/l2gksNWCEif1IpSzpgbWzIZHN0+
rO/8kYP4z9MZgAQgEFtZWn8bSZChmQq6KMUYymmawei10cukPdbD/hgrNJrEa2ayCd45SnYQ5BTV
VmhkaaeQjNWOwkTDkYlzYqQYhQMIyBxiJCaR/IzljWWfwSSSebgEuWePqSN6W5pRUT3XhH2ljWEZ
JG/SK2RaOlZP028s+QYo7zyLaFB3DRIehXC6xt2emOqU/PuCICqVpybe4/8GhGXencuXXbWauQY0
e8aLiG/Bc5h2rr3WA7vO0TKcGrp4Z986CzBAy8snwZx3h4UD0tO0Kf/6Ae0C6qbybG9enp6PqeJR
AcxcbV3hOvQ6BCgCBWOR3RrEGi0C65JH9FUufvVcJfrWqUqUDk0IFDpp1uxtrQrCvmgpnZgLdrTE
ezeLrckBhw1ATuzC55tsKZJ0BYRFciG+TfZGplF/lJ1ZBLWEH2bA3Sy31JEOqISp9DSobDDqEWCH
jSTwJ8SrRcKeT1eCqnMOBaOBoMNkyUlrPb1jql6GkD2REuT5ejJVbZbDuYKyJtuel1vIWRcIJnrf
yyypUE4XWJltPKe+T35sZyTIQ+5F32GMtwf9+R6w2HNzaPzGPtsomsy1ugPM6oKpWzFxl2GGt2jz
NFulrCA+Gb2cquz+Zg0xl47mKXCp

type: account
authority-id: canonical
revision: 1
account-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
display-name: Jane Doe
timestamp: 2024-05-02T21:18:36.153427Z
username: jane
validation: unproven
sign-key-sha3-384: BWDEoaqyr25nF5SNCvEv2v7QnM9QsfCc0PBMYD_i2NGSQ32EF2d4D0hqUel3m8ul

AcLBUgQAAQoABgUCZjQDLAAAGCMQABGD2/CsJAecBcEmZalPffBQp+JzI485PR9eb9RRjuTn1EBm
aGDPGBTJzC2czUp3RJ9SlsDYCpXMXSquHT/eFQ/g5VBqyybUBiLNwpYjRerAFfBdcPDB1Uv9qK3W
xuDUvQpygj+bebaRDw9ci9oGtD3s4KKLYBYVY24hq0H97t4Jx0x48gUAurErYIQZeoxdflhyS91t
H1m7z9deLmSuj7W4S2M/NvLq7pboWmnS1CQfD0LPm4+Id/7K0wzdjwnTBzNahLhHxMfGImHiVHZd
afUx2GcoPw/X4VW072sIadA5Jo+f2Rw2jiGKNYTuFUTFNFcC9+/nFFlUeOoDb/YG2MDTV66NGPlg
sV2IbCt6dheYuPLgJa2/Z6FsNjbUbWxI0Wq82qSK1oOrQsdRn6DvE6YbDPRhfo5X2FaWptHN6jKE
eqcbOQ2m4CmGykC4HQuS+D8zQ3eD5uFQBNmHbL7NlWzGCt9fYaiTF8C9kWZFqxcWnTrPN6mlGkuK
rtd6/2W3VUj/f9IxO/0MkmPk1woxNYKeMqCURlM537mqJtEjD3XTmxftYv6/d5UKAg7YJfCs/P6P
d5Rhla5SVJDPDU9WwOZJKHgFufArkdOyWPUCTDhboe8Rr8u+p1QYBaW9A3BuP6z5w7HmRzZynbwt
WQJ3XR0OV2c6gvDH0CdMjdUGDBeq
"""

snap_http.add_assertion(assertion)
snap_http.add_user(
    "jane",
    "jane@example.com",
    sudoer=True,
    force_managed=True,
    known=True,
)
