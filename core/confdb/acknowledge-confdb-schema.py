#!/usr/bin/env python3

from landscape.client import snap_http

# Acknowledge a confdb-schema assertion into snapd, along with its prerequisite
# account and account-key assertions.
assertion = """\
type: account
authority-id: canonical
account-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
display-name: Stephen Mwangi
timestamp: 2024-01-03T10:36:48.475339Z
username: st3v3nmw
validation: unproven
sign-key-sha3-384: BWDEoaqyr25nF5SNCvEv2v7QnM9QsfCc0PBMYD_i2NGSQ32EF2d4D0hqUel3m8ul

AcLBUgQAAQoABgUCZZU4wAAA0scQABIiB5aAhqNNv70gAJPq42FfzuFaH+0H8bEjDRaEt73kFmo9
ZzV2kHbr5r1WrZn7wPFqSrxBzi9dspCozc9nZi2pdV+S8xcFHFA29aGcGWrT3vs4U8Jv31ydqnQ8
iiwQbgPCVTeGHbAFJqn2pk4opcqLD74Cdh+6kVVmCc3XdcrPHvqI7Cowu6SbEEAGEhTTuLZOpXGr
/rcTtpZvDCw6lCTsUkkpqBgDB4gBZPKijKQpqN4cyKbh1UMlEZOd0u+c+uEtbFgHmLkL6BG9Szny
+SdWZTyHc3L332hPMunM941H+z0M1arGqmkkRaA+xXCdBRVOvqT7SCyxuApzi8Sm2qOoCWcqoFKj
AFdmfPg5Z1Sp6CyUzMRC3GuLODdMahdzz2zkxu4imYOgR4NqfSv5tbw+M2ZXk9Jv7kmdHU5i0scW
8zr8T28LbCCxdm1x8lFbytTDf6sa8iKOK9v3Sz4cEmrpJWikocVSOWLvE/2C8Fzkm2FJRiIZZ0BL
LCMocgEf1i0IaKw6/VdHn0m01uYS8y30Y72S8hkpUo0NTgj90a6Gw+/RDTXY+6F4IqwNhqQOQJBz
scsrCeNF7NkgKvDNJx/Cth11ztIWDHQsTagGElXLPvO7fNz47l5qVDFUH/MXj7GPzCkW5KBJ9AbU
RfhfoQ4nYrvl796kWhDsD08RRDJp

type: account-key
authority-id: canonical
public-key-sha3-384: xkd_Y2ay5N2Uo14v_wsCtfVJYLAVbJgxbiKM8Ne4mZBflaROriZgk2nb5i9Oebum
account-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
name: snapcraft
since: 2024-03-06T08:43:58Z
body-length: 717
sign-key-sha3-384: BWDEoaqyr25nF5SNCvEv2v7QnM9QsfCc0PBMYD_i2NGSQ32EF2d4D0hqUel3m8ul

AcbBTQRWhcGAARAAwfGMiOrB4ST1np6prpDWBlivmdkULG2F9QTYCnKz0uNmLkiHFqe4MN+XDtek
NPC66L0ZSx6IQ74ZLlb3/djdZ8t/mbI/d/nAL3IFrC5aYLrcKtX/e03lKDvzThQUFDPgB31PbZuD
XakbbSG9HjcLGBLVC/jMqBsKQaBarNkddSXwqL0FnKGLWbxIPnbuJ8Zxny/nW9+LU5E5LfuAvxNe
oBYO1cPOlhUfR0XhJiBQqKMDSRiXqIWrr2OYxrnDZgphIgo+WWBfqiYM3vSmNzt36R/AkyfrWq08
bU+s8nc22Ms4KlSYEWFVddz2hbhYvMrjoNgXq85J2O1DkQQWA9gOZXpxskFP3mEd2T/ofS028v0I
YHs4ST/QJWSTsJT2PhtUO6PeNjlAhZ4NMJZlnI3PJt/5c3d5He/SZ6H54B/19tMs3KAgxzXTX7Qx
646qFBF+1ZTsVeZ9UusEbyyZJDexcZVZiVKL+4K+xDjOlXo0Erm8luVkk0I4TwjLgPK8+aPsd0l6
t7rE0KcrUsPmoNcuca1++XD0dJNMwLNkCQDvXk7q0xIr7L/ue231I5dcPW0PT3d76wA/kR3woA+V
tO7yy1Qop0npAE4XzoNSTdlNCzsuWzUgCzlFwLnDIKGPNv3wZFIQUduou8YlAMu3ZTPNJduG0Ylh
RKvjES9B9mRBoNUAEQEAAQ==

AcLBUgQAAQoABgUCZegszgAAJ6AQALEDhdPkEhR5etc4St6D4jcdyt52+IXKUlhiqs+pU/37yHya
p1cSB6HufvykSGshusJ+JENaDOIMIu0zXWMbzJM+mUVYSRn+PLDc5jkgiZQin6FUDf5d+wby3B2B
L2slA3NPf21bYodqCGZPsYKg3V7hDhUIYDE4n12XY00lwU6RsA5e6t9CPJQb899W7hyRxNunfBnS
w5/zHPD+r88VnyKpwqHhbwxIJAtPTE+UFxq57HYwJXvvL5V3KZ/9iF7YyyAsy2FwMyJgpMkS/QSm
3B2KPcGB3tNtWAv3gVEzYcKnFqWfYXZP/qvhQVpB5aSUKTnQFWf0DLFARnfZJxuUNy4SQEVU0Xhq
ZVPiQUDj2HBR6QsLzYH4ySLGiL+iBygIVKYXnm5baP+XNJsN2BKU751aXT1keOELxgJmv8fBahQc
X9Lg/EinlvxBzsrtv+O6CHckVxEsxoVMhRNJM6nFd4dA8leXDxLd0NokMufRf3PDjMIupBSptS7Q
hGXqGUdVV+5PwT+5anvSnxRqd/6IqLrq9M3eBF2PdLGWP0Bx8IVVuIWGPGMMxvHDtYcfYVbcdxu3
LseyUyXh56uPMXPW2CVdAYHdTsSDVYD2l/ksYpA4Cd7tyBeJ7btWh8n9YsZ3HZrk6hasNF0VKURm
fvYaDRZCi27SyGIRI5OXQBmoa2zn

type: confdb-schema
authority-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
revision: 1
account-id: f22PSauKuNkwQTM9Wz67ZCjNACuSjjhN
name: network
timestamp: 2026-01-21T10:19:23+00:00
views:
  proxy-admin:
    rules:
      -
        access: read-write
        content:
          -
            request: url
            storage: url
          -
            request: bypass
            storage: bypass
        request: {protocol}
        storage: proxy.{protocol}
  proxy-state:
    rules:
      -
        access: read
        request: https
        storage: proxy.https
      -
        access: read
        request: ftp
        storage: proxy.ftp
body-length: 487
sign-key-sha3-384: xkd_Y2ay5N2Uo14v_wsCtfVJYLAVbJgxbiKM8Ne4mZBflaROriZgk2nb5i9Oebum

{
  "storage": {
    "aliases": {
      "protocol": {
        "choices": [
          "http",
          "https",
          "ftp"
        ],
        "type": "string"
      }
    },
    "schema": {
      "proxy": {
        "keys": "${protocol}",
        "values": {
          "schema": {
            "bypass": {
              "type": "array",
              "unique": true,
              "values": "string"
            },
            "url": "string"
          }
        }
      }
    }
  }
}

AcLBcwQAAQoAHRYhBHCftZeyXSJlNBvC+h+HHdMBlPLtBQJpjdWQAAoJEB+HHdMBlPLtomUP/iFa
BxCtGrwOzgVNbzmkSJXqf0LRbTGLyQQkCe5lV/X9PKBa4J+I4y7QGrUDAXQwvsSUJgcsR+99NgnA
IJE6mfZos8IXK/1TKRPUM/umeb4CfcLu6xuCwc/PFZnJhxTOK3FQddONXCXqCfQStx4KvRIfPu/S
nybbuMNQrepcvDSMY1YF18nX3kmC4WXnsySFJI5EDkdDNDC5C4mM85khyORdApHXSUewNVWghIP7
JjB0NeYxysJl3rrRcppfeGpB5Akx7lVJiTmGkCzvkDTymizMj4S6sveBGn5SLQPZz44X6jGG95il
EE//X9bM/bEEe2+s0gzIy4OWdDVVFU/X1uxzC6jlI+gwSpbhExKStdapC8nU7phoFvIlABLw7h2L
wFC7n84l95fR6f+9FPm1UKFqoBTO4pexTcihA3SNrKvD3oFyU3GnWZgfI1rgMOVdQnOYrOuaQMCO
lLZG0GgktRb9l/XekJexadsAnbhe8AF1Fb4pUM6eqAoIryy4CRetonlPyCDcFtOy+O4ARgsqYDfi
7YxA1g29kjYDox1Q/5Sb64ZRC68XAyCWF19E3sj4I/MLQ7/c429q5PF2AMMuoB3Z3Do6LmE3awlN
esGfztMtfdb2nRoH595JYbd55L8szS9zvJziSYXWCQ27BOJdxTU8JJaMGvpUOMbjD3YSqGb3
"""

snap_http.add_assertion(assertion)
