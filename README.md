<img src="https://assets.ubuntu.com/v1/bc04c279-landscape-title-logo-white.svg" height="150">

# Landscape Scripts

Landscape can execute scripts on machines on demand, or at a regular interval for monitoring purposes.

1. Remote execution Scripts
2. Graphs for monitoring over time

[**scripts-in-landscape.md**](./scripts-in-landscape.md) explains how to add and run these scripts in Landscape.

## The purpose of this project

Landscape Scripts can be authored in any familiar shell scripting language. Some scripts are easier to implement with bash, others are easier to implement with Python. The goal of this project is to continuously improve and grow a collection of useful scripts that perform systems management or systems monitoring functions.

## Attention open-source contributors

If you
- have an idea for a new script
- are able to convert a bash script to python
- can convert scripts to any other shell scripting language
- have thoughts around improving the quality of this material

Do not hesitate to fork this repository, and submit a pull request with your improvements. If appropriate, you are encouraged to [**write a companion tutorial**](https://ubuntu.com/tutorials/tutorial-guidelines) for your contribution, or suggest updates to the existing tutorials.

---

<img src="https://assets.ubuntu.com/v1/c9dc2869-Use-snap-commands.svg" height="48" align="left">

## Systems Management Scripts

### Security Patching

- [**Tutorial**](https://ubuntu.com/tutorials/test-and-deploy-individual-cve-fixes-with-ua-client-and-landscape): Test and deploy individual CVE fixes with UA Client and Landscape
    - [**uafix.sh**](./management/security/uafix.sh): Granular security patching by USN patch number of CVE number.
    - **uafix.py** - conversion needed
- [**Tutorial**](https://ubuntu.com/tutorials/manage-livepatch-configurations-at-scale-with-landscape): Enable or disable Livepatch at scale with Landscape
    - [**livepatchenable.sh**](./management/security/livepatchenable.sh)
    - **livepatchenable.py** - conversion needed
    - [**livepatchdisable.sh**](./management/security/livepatchdisable.sh)
    - **livepatchdisable.py** - conversion needed
- [**Tutorial**](https://ubuntu.com/tutorials/monitor-and-manage-livepatch-configurations-at-scale-with-landscape#3-monitor-livepatch-via-landscape): Track the Livepatch entitlement in an auditable manner, through Landscape
    - [**livepatchannotations.sh**](./management/security/livepatchannotations.sh)
    - **livepatchannotations.py** - pending

### Ubuntu Advantage and Ubuntu Pro Subscriptions

- **Tutorial**: add annotations to machines in Landscape, identifying each machine's Ubuntu Advantage entitlements. This tutorial does not yet exist.
    - [**uastatus.sh**](./management/Pro/uastatus.sh)
    - **uastatus.py** - conversion needed
- [**Tutorial**](https://ubuntu.com/tutorials/audit-ua-client-esm-configurations-at-scale-with-landscape): Audit UA Client ESM configurations at scale with Landscape
    - [**esmaudit.sh**](./management/Pro/esmaudit.sh)
    - **esmaudit.py** - conversion needed
- [**Tutorial**](): Enable ESM configurations at scale with UA Client and Landscape
    - [**esmenable.sh**](./management/Pro/esmenable.sh)
    - **esmenable.py** - conversion needed

### FIPS configurations at scale with Landscape

- [**Tutorial**](https://ubuntu.com/tutorials/manage-ua-client-fips-configurations-at-scale-with-landscape): Enable and disable the Ubuntu Advantage FIPS entitlement in an auditable manner, through Landscape
    - [**fipsenable.sh**](./management/FIPS/fipsenable.sh)
    - **fispenable.py** - conversion needed
    - [**fipsdisable.sh**](./management/FIPS/fipsdisable.sh)
    - **fipsdisable.py** - conversion needed
- [**Tutorial**](https://ubuntu.com/tutorials/audit-ua-client-fips-configurations-at-scale-with-landscape): Track the Ubuntu Advantage FIPS entitlement in an auditable manner, through Landscape
    - [**fipsannotations.sh**](./management/FIPS/fipsannotations.sh)

### Blocking Software Package Installation with Landscape

- [**Tutorial**](https://ubuntu.com/tutorials/blocking-software-package-installation-with-landscape): Granular software restrictions by apt package name.
    - [**bypackagename.sh**](./management/Block%20Installation%20with%20Apt/bypackagename.sh)
    - **bypackagename.py** - conversion needed
- **Tutorial**: There is a need to programmatically create **.pref** files to block all packages from Universe. This allows tightly regulated environments to lock down their Ubuntu environments, and loosen restrictions as needed. This tutorial and its companion scripts do not yet exist. Feel free to contribute!
    - **allpackages.sh** - pending
    - **allpackages.py** - pending

### Get all computers from Landscape

- A Windows PowerShell function to get all registered computers from Canonical Landscape.
    - [**Get-LSComputers.ps1**](./management/Get-LSComputers/Get-LSComputers.ps1)

---

<img src="https://assets.ubuntu.com/v1/d3aa493c-Build-your-first-snap.svg" height="48" align="left">

## Systems Monitoring Scripts

### Security Patching Graphs

- **Tutorial**: find inaccessible security updates on any Ubuntu instance, by identifying the availability of software updates from the security pocket of the Expanded Security Maintenance repository. This tutorial does not yet exist. Feel free to contribute!
    - **securitystatus.sh** - pending
    - [**securitystatus.py**](./monitoring/security/securitystatus.py)

- [**Tutorial**](https://ubuntu.com/tutorials/add-livepatch-graphs-in-landscape): chart kernel live patching activities over time with Landscape’s custom graphs.
    - [**livepatchcount.sh**](./monitoring/Livepatch/livepatchcount.sh)
    - **livepatchcount.py** - conversion needed

---

<img src="https://assets.ubuntu.com/v1/4a28b0b5-menu-icon--product-cloud-init.svg" height="48" align="left">

## Landscape Deployment Script

### Deploy Landscape with cloud-init and Juju

- **Tutorial**: Deploy Landscape to an ARM powered Ubuntu instance on Oracle Public Cloud. This tutorial does not yet exist.
    - [**cloud-init.yaml**](./provisioning/cloud-init.yaml)


## Landscape for IoT / Ubuntu Core devices

_Note: some scripts may require python3-requests deb (or PyPI requests) in order to function correctly. It is automatically installed in most environments (including the Landscape Client Snap) but that might not always be the case._

### Snap Management

- **Tutorial**: Install a snap using a python wearfile and dump script output to a temporary file for debugging on the device.
    - [**install-snap-debug.sh**](./core/snaps/install-snap-debug.sh)

- **Tutorial**: Install a snap using a python script and the SnapD REST API
    - [**install-snap.py**](./core/snaps/install-snap.py)

- **Tutorial**: Run an attached python script
    - [**run-attached-script.sh**](./core/snaps/run-attached-script.sh)

- **Tutorial**: Install a snap using python and the snap-http library
    - [**snap-http-install.py**](./core/snaps/snap-http-install.py)

- **Tutorial**: Remove a snap using python and the snap-http library
    - [**snap-http-remove.py**](./core/snaps/snap-http-remove.py)

- **Tutorial**: Update snapd configuration using Python and the snap-http library
    - [**update-snap-config.py**](./core/snaps/update-snap-config.py)

- **Tutorial**: Set the refresh timer using Python and the snap-http library
    - [**set-refresh-timer.py**](./core/snaps/set-refresh-timer.py)

- **Tutorial**: Put device into managed mode (disable automatic snap refreshes)
    - [**snap-http-remove.py**](./core/snaps/snap-http-managed-mode.py)

### Snap Services

- **Tutorial**: Enable a snap service using Python and the snap-http library
    - [**enable-service.py**](./core/services/enable-service.py)

- **Tutorial**: Restart a snap service using Python and the snap-http library
    - [**restart-services.py**](./core/services/restart-services.py)

- **Tutorial**: Stop a snap service using Python and the snap-http library
    - [**stop-service.py**](./core/services/stop-service.py)

### Snap Interfaces

- **Tutorial**: Connect a snap interface using Python and the snap-http library
    - [**connect-interface.py**](./core/interfaces/connect-interface.py)

- **Tutorial**: Disconnect a snap interface using Python and the snap-http library
    - [**disconnect-interface.py**](./core/interfaces/disconnect-interface.py)

- **Tutorial**: Get interface connections using Python and the snap-http library
    - [**get-connections.py**](./core/interfaces/get-connections.py)

### Logs

- **Tutorial**: Display logs for all snaps using Python and the snap-http library
    - [**snapd-logs.py**](./core/logs/snapd-logs.py)

- **Tutorial**: Push landscape-client's logs to an FTP server using Python
    - [**ftp-client-logs.py**](./core/logs/ftp-client-logs.py)

### User Management

- **Tutorial**: Add an Ubuntu SSO user to a Core device using Python and the snap-http library
    - [**add-sso-user.py**](./core/users/add-sso-user.py)

- **Tutorial**: Add a system user to a Core device using Python and the snap-http library
    - [**add-system-user.py**](./core/users/add-system-user.py)

- **Tutorial**: Remove a user from a Core device
    - [**remove-user.py**](./core/users/remove-user.py)

### Debugging

- **Tutorial**: Collect a large amount of SnapD and core system information that could be useful when debugging a system with Canonical Support
    - [**remove-user.py**](./debugging/snap-debug-info.sh)
