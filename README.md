Install Raspbian Stretch Lite OS on Raspberry Pi and setup network connection
Create user with root privileges. Caution with keyboard layout when setting password.
  adduser username
  usermod -aG sudo username
  sudo adduser username gpio
Prevent need to reenter password when sudoing from username
  sudo visudo
  - Add line "username ALL=(ALL) NOPASSWD: ALL"
  Press CTRL+X and hit 'y' to save file
Log-out of user pi and into the new one
Delete pi user (to avoid username guessing)
  deluser --remove-home pi
Update packages, distro and firmware if needed
  sudo apt-get update
  sudo apt-get upgrade
  sudo a+t-get dist-upgrade
  sudo rpi-update
Start OpenSSH server and enable it to start on boot
  sudo systemctl start ssh
  sudo systemctl enable ssh
Connect using SSH
Set up Python3 environment
  sudo apt-get install python3 python3-pip 
  pip3 install rpi.gpio "picamera[array]"  # "array" option downloads numpy dependency
