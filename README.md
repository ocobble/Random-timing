# Random timing assignment

This repository holds the code for our group's random timing assignment.

The code can be run from the command line with: "python pyTiming.py " followed by a list of the websites you want to test

The code may need to be run twice to give an accurate representation of the time it takes to get the numbers,
as app engine websites may need to start up if they are in an idle state

## Results Summary

## Java VM Documentation

## Java App Engine Documentation

## Python VM Documentation
This documentation assumes that you already have access to Google Cloud and money to spend on a virtual machine instance.

### 1. Go to https://console.cloud.google.com/compute/ 
Log in to your Google account if you haven't already.

### 2. Create a new Instance 
Press the "Create Instance" button at the top of the page.

Name your instance something appropriate.

In the "machine type" field, select "f1 micro".

In the "Boot Disk" box, select "change", then select "Ubuntu 18.04 LTS".

Under "Firewall", check the box next to "Allow HTTP Traffic".

Select "Create" and wait for your VM to start up.

### 3. SSH into your VM
Select "SSH" or choose "Open in Browser Window" from the dropdown. If you are presented by a black screen, try again until you see a "Connecting" message displayed.

### 4. Install necessary software
Run the following commands:

```
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install Flask
```

This installs python and all its accoutrements, creates a virtual environment, and installs Flask into that environment.

### 5. Clone this git repository
Run the following command:

```
git clone https://github.com/ocobble/Number-Generator.git
```

### 6. Add correct firewall settings
Access the main hamburger menu in the upper-right-hand corner of the google cloud console.

Go to VPC Network -> Firewall Rules.

Select "Create Firewall Rule".

Name your new rule.

Enter "http-server" in the "Target tags" box.

Enter "0.0.0.0/0" in the "Source IP ranges" box.

Select the "tcp" checkbox under "Protocols and ports".

Enter "5000" in the corresponding box.

Click create.

### 7. Get a Static External IP
Click "External IP addresses" in the sidebar of the "VPC Network" view.

Click "Reserve Static Address".

Name the static address, and select the virtual machine we are working with under "Attached to".

Click "Reserve".

### 6. Start Your Web Server

Open a tmux session in your virtual machine with the command `tmux new`. If you no longer see `(venv)` before your prompt, use the command `source venv/bin/activate` to get it back. This creates a virtual terminal that will keep running after you log out of your instance.

Navigate to `Number-Generator/pythonVM/`.

Run the command `python randomGenerator.py`. This should start the server, and the terminal will not be able to accept any more commands.

Exit the tmux session while keeping it running in the background by pressing `Ctrl-b`, then `d`. You should be back at a notmal-looking terminal.

Log out of your VM.

### 7. Test
The URL to reach your web server will be `http://YOUR.STATIC.EXTERNAL.IP:5000/`. Test it yourself by typing that into a browser, or use the automated test method described in the main README.


## Python App Engine Documentation
