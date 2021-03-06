*****
Zelus
*****

Platform set-up:
################
#. Install Raspbian Stretch Lite OS on Raspberry Pi and setup network connection
#. Create user with root privileges. Caution with keyboard layout when setting password.
    * adduser username
    * usermod -aG sudo username
    * sudo adduser username gpio
#. Log-out of user pi and into the new one
#. Delete pi user (to avoid username guessing)
    * deluser --remove-home pi
#. Update packages, distro and firmware if needed
    * sudo apt-get update
    * sudo apt-get upgrade
    * sudo a+t-get dist-upgrade
    * sudo rpi-update  # Apparently this is now discouraged
#. Start OpenSSH server and enable it to start on boot
    * sudo systemctl start ssh
    * sudo systemctl enable ssh
#. Connect using SSH
#. Set up Python3 environment
    * sudo apt-get install python3 python3-pip
    * pip3 install rpi.gpio "picamera[array]"  # "array" option downloads numpy dependency
#. Enable Camera
    * sudo raspi-config
    * (go to advanced and set memory split to 128MB)
    * (enable camera using menu)
    * sudo chmod 777 /dev/vchiq
