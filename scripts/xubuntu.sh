#!/bin/bash

# Function to check if a package is installed
package_installed() {
    dpkg -l "$1" &> /dev/null
}

# List of packages to install
packages=(
    engrampa
    thunar-archive-plugin
    git
    atril
    ristretto
    xfce4-taskmanager
    texlive-full
    mousepad
    blueman
)

# Iterate through the list of packages
for package in "${packages[@]}"; do
    # Check if the package is already installed
    if package_installed "$package"; then
        echo "$package is already installed."
    else
        # Install the package
        sudo apt install -y "$package"
        # Check if installation was successful
        if [ $? -eq 0 ]; then
            echo "Installed $package successfully."
        else
            echo "Failed to install $package. Exiting."
            exit 1
        fi
    fi
done

echo "All packages installed successfully."
