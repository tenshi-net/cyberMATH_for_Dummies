**cyberMATH for Dummies** is a library of Python scripts creating CLI-based calculators for math operations common to cybersecurity professionals. It was inspired by a cryptography lesson on [TryHackMe](https://tryhackme.com/), which recommended using Python to run calculations of _XOR_ and _modulo_ operations instead of a calculator application.

The goal of this library is to create a lightweight way to quickly run these operations without having to leave the CLI. This would be useful if you needed to run these operations on a system that lacks a GUI, for example. Further, it could be very useful to anyone working with cryptography, such as cybersecurity professionals and cypherpunks.

## Tools

- XORmod: `xormod.py`
- RSAmath: (WIP)

## How to use

After you've chosen and downloaded a script, ensure that the script is allowed to execute. On Linux, run `sudo chmod +x [script].py` to give it that permission. Following that, run it from the terminal with `./[script].py`. The script will start off by prompting you to pick which operation type you want to calculate, and then it will ask you for the two numbers you want to calculate.

## Current limitations

As of now, these scripts are barebones and might not support complicated calculations. This is something I might improve upon later, provided I and others find it useful enough. For now, though, it's just for simple calculations, doubling as both proof of concept and Python practice, as a means of getting factors needed for the more advanced calculations.
