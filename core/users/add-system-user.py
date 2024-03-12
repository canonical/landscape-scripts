#!/usr/bin/env python3

from landscape.client import snap_http

# this is an example system-user assertion,
# please create and sign your own
assertion = """
type: system-user
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
"""

snap_http.add_assertion(assertion)
snap_http.add_user(
    "jane",
    "jane@example.com",
    sudoer=True,
    force_managed=True,
    known=True,
)
