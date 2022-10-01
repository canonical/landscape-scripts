<img src="https://assets.ubuntu.com/v1/bc04c279-landscape-title-logo-white.svg" height="150">


# About Landscape Scripts

Landscape can execute scripts on machines on demand, or at a regular interval for monitoring purposes.

1. Remote execution Scripts
2. Graphs for monitoring over time

To add scripts into Landscape, when you log into dashboard, you will see **Scripts** and **Graphs** in the top navigation bar.

All Scripts must produce a successful exit code. If a script produces an exit code indicative of failure, Landscape will report that the script failed to run.

Scripts for tracking numerical data over time in the Monitoring section of the Landscape dashboard have the additional requirement of producing only a numerical output, on success.

## Running remote execution Scripts
Click **Computers** in the black ribbon at the top of the page, and select some computers:

To run scripts on demand: click **Scripts** in the top navigation bar. Select which script you wish to run, for this selection of computers, and click **Next**.

The **Activities** tab in the Landscape dashboard conveys which user is responsible for a particular script, the targeted list of computers, the time it last ran, the terminal output for each computer, and the script's exit code.

# The purpose of this project

Landscape Scripts can be authored in any familiar shell scripting language. Some scripts are easier to implement with bash, others are easier to implement with Python. The goal of this project is to continuously improve and grow a collection of useful scripts that perform systems management or systems monitoring functions.

<img src="https://assets.ubuntu.com/v1/c9dc2869-Use-snap-commands.svg" height="48" align="left">

## Systems Management Scripts

### Manage UA Client FIPS configurations at scale with Landscape

[Tutorial](https://ubuntu.com/tutorials/manage-ua-client-fips-configurations-at-scale-with-landscape) | Bash Script | Python Script

Use Landscape’s dashboard to identify manage machines with the Ubuntu Advantage FIPS entitlement enabled

### Blocking Software Package Installation with Landscape

[Tutorial](https://ubuntu.com/tutorials/blocking-software-package-installation-with-landscape) | Bash Script | Python Script

Granular software restrictions are a trivial activity with Landscape.

<img src="https://assets.ubuntu.com/v1/d3aa493c-Build-your-first-snap.svg" height="48" align="left">

## Systems Monitoring Scripts

### name of first script

lorem ipsum