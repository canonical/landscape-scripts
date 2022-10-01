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

Do not hesitate to fork this repository, and submit a pull request with your improvements. If appropriate, you are encouraged to [**write a companion tutorial**](https://ubuntu.com/tutorials/tutorial-guidelines) for your contribution, or suggest updates to the existing tutorials.

---

<img src="https://assets.ubuntu.com/v1/c9dc2869-Use-snap-commands.svg" height="48" align="left">

## Systems Management Scripts

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

---

<img src="https://assets.ubuntu.com/v1/d3aa493c-Build-your-first-snap.svg" height="48" align="left">

## Systems Monitoring Scripts

### Livepatch Graphs

- [**Tutorial**](https://ubuntu.com/tutorials/add-livepatch-graphs-in-landscape): chart kernel live patching activities over time with Landscape’s custom graphs.
    - [**livepatchcount.sh**](./monitoring/Livepatch/livepatchcount.sh)
    - **livepatchcount.py** - conversion needed