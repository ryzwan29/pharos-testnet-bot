#!/bin/bash

clear
echo -e "\033[1;32m
██████╗ ██╗   ██╗██████╗ ██████╗ ██████╗ ██████╗  █████╗ 
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗╚════██╗██╔══██╗
██████╔╝ ╚████╔╝ ██║  ██║██║  ██║██║  ██║ █████╔╝╚██████║
██╔══██╗  ╚██╔╝  ██║  ██║██║  ██║██║  ██║██╔═══╝  ╚═══██║
██║  ██║   ██║   ██████╔╝██████╔╝██████╔╝███████╗ █████╔╝
╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚════╝ 
\033[0m"
echo -e "\033[1;34m==================================================\033[1;34m"
echo -e "\033[1;34m@Ryddd29 | Testnet, Node Runer, Developer, Retrodrop\033[1;34m"

sleep 4

# Update package
echo -e "\033[1;32m\033[1mUpdate & Upgrade package...\033[0m"
sudo apt update && sudo apt upgrade -y
sudo apt install git -y
clear

# Prompt to ask user if they want to install Node.js
read -p $'\033[1;32m\033[1mDo you want to install python & pip? (y/n) [default: y]: \033[0m' USER_INPUT

# Default to "y" if no input provided
USER_INPUT=${USER_INPUT:-y}

if [[ "$USER_INPUT" =~ ^[Yy]$ ]]; then
  echo -e "\033[1;32m\033[1mInstalling python and pip...\033[0m"

  # Install Python & pip
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt update
  sudo apt install -y python3.12 python3.12-venv python3.10-venv
  sudo curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12

else
  echo -e "\033[0;33mInstallation skipped by user.\033[0m"
fi

# Clone github repository
echo -e "\033[1;32m\033[1mClone github repository...\033[0m"
git clone https://github.com/ryzwan29/pharos-testnet-bot.git
cd pharos-testnet-bot

# Install dependencies
echo -e "\033[1;32m\033[1mInstalling requirements dependencies...\033[0m"
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
