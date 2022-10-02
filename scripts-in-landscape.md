<img src="https://assets.ubuntu.com/v1/90fc25a2-landscape-logo.svg" height="50">

# Adding Scripts to Landscape

To add scripts into Landscape, when you log into dashboard, you will see **Scripts** and **Graphs** in the top navigation bar. Navigating to each of those links will reveal a page with an "Add Scripts" or "Add Graph" link.

All Scripts must produce a successful exit code. If a script produces an exit code indicative of failure, Landscape will report that the script failed to run. 

Scripts for tracking numerical data over time in the Monitoring section of the Landscape dashboard have the additional requirement of producing only a numerical output, on success.

## Running Systems Management Scripts

Click **Computers** in the black ribbon at the top of the page, and select some computers:

To run scripts on demand: click **Scripts** in the top navigation bar. Select which script you wish to run, for this selection of computers, and click **Next**.

The **Activities** tab in the Landscape dashboard conveys which user is responsible for a particular script, the targeted list of computers, the time it last ran, the terminal output for each computer, and the script's exit code.

## Running Systems Monitoring Scripts

These scripts will run at the appropriate intervals, and the output will be recorded by Landscape.
