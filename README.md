<img src="https://assets.ubuntu.com/v1/bc04c279-landscape-title-logo-white.svg" height="150">


# Landscape Scripts

Landscape can execute scripts on machines on demand, or at a regular interval for monitoring purposes.

1. Remote execution Scripts
2. Graphs for monitoring over time

To add scripts into Landscape, when you log into dashboard, you will see **Scripts** and **Graphs** in the top navigation bar. Navigating to each of those links will reveal a page with an "Add Scripts" or "Add Graph" link.

All Scripts must produce a successful exit code. If a script produces an exit code indicative of failure, Landscape will report that the script failed to run.

Scripts for tracking numerical data over time in the Monitoring section of the Landscape dashboard have the additional requirement of producing only a numerical output, on success.

## Running remote execution Scripts
Click **Computers** in the black ribbon at the top of the page, and select some computers:

To run scripts on demand: click **Scripts** in the top navigation bar. Select which script you wish to run, for this selection of computers, and click **Next**.

The **Activities** tab in the Landscape dashboard conveys which user is responsible for a particular script, the targeted list of computers, the time it last ran, the terminal output for each computer, and the script's exit code.

## The purpose of this project

Landscape Scripts can be authored in any familiar shell scripting language. Some scripts are easier to implement with bash, others are easier to implement with Python. The goal of this project is to continuously improve and grow a collection of useful scripts that perform systems management or systems monitoring functions.

## How to contribute

If you have an idea for a new script, do not hesitate to submit a pull request to this repository, and to write a companion tutorial.

If you are able to convert a bash script to python, or any other shell scripting language, please 

<img src="https://assets.ubuntu.com/v1/18b87a60-image-intro-dots-desktop.svg" width="100%">

<img src="https://assets.ubuntu.com/v1/c9dc2869-Use-snap-commands.svg" height="48" align="left">

## Systems Management Scripts

### FIPS configurations at scale with Landscape

- [Tutorial](https://ubuntu.com/tutorials/manage-ua-client-fips-configurations-at-scale-with-landscape): Enable and disable the Ubuntu Advantage FIPS entitlement in an auditable manner, through Landscape
    - [`fipsenable.sh`](./management/FIPS/fipsenable.sh)
    - `fispenable.py` - conversion needed
    - [`fipsdisable.sh`](./management/FIPS/fipsdisable.sh)
    - `fipsdisable.py` - conversion needed
- [Tutorial](https://ubuntu.com/tutorials/audit-ua-client-fips-configurations-at-scale-with-landscape): Track the Ubuntu Advantage FIPS entitlement in an auditable manner, through Landscape
    - [`fipsannotations.sh`](./management/FIPS/fipsannotations.sh)

### Blocking Software Package Installation with Landscape

- [Tutorial](https://ubuntu.com/tutorials/blocking-software-package-installation-with-landscape): Granular software restrictions by apt package name.
    - [`bypackagename.sh`](./management/Block%20Installation%20with%20Apt/bypackagename.sh)
    - `bypackagename.py` - conversion needed
- Tutorial: There is a need to programmatically create `.pref` files to block all packages from Universe. This allows tightly regulated environments to lock down their Ubuntu environments, and loosen restrictions as needed. This tutorial and its companion scripts do not yet exist. Feel free to contribute!
    - `allpackages.sh` - pending
    - `allpackages.py` - pending

<img src="https://assets.ubuntu.com/v1/d3aa493c-Build-your-first-snap.svg" height="48" align="left">

## Systems Monitoring Scripts

### Livepatch Graphs

- [Tutorial](https://ubuntu.com/tutorials/add-livepatch-graphs-in-landscape): chart kernel live patching activities over time with Landscape’s custom graphs.
    - [`livepatchcount.sh`](./monitoring/Livepatch/livepatchcount.sh)
    - `livepatchcount.py` - conversion needed