**XORmod for Dummies** is a CLI-based calculator for _XOR_ and _modulo_ operations. It was inspired by a cryptography lesson on [TryHackMe](https://tryhackme.com/), which recommended using Python to run calculations instead of a calculator application.

The goal of this script was to create a lightweight way to quickly run XOR and modulo operations without having to leave the CLI. This would be useful if you needed to run these operations on a system that lacks a GUI, for example. Further, it would be very useful to anyone working with cryptography, such as cybersecurity professionals and cypherpunks.

## How to use

First, ensure that the script is allowed to execute. On Linux, run `sudo chmod +x xormod.py` to give it that permission. Following that, run it from the terminal with `./xormod.py`. The script will start off by prompting you to pick which operation type you want to calculate, and then it will ask you for the two numbers you want to calculate.

## Current limitations

As of now, it's very barebones and can't calculate between more than standard integer pairs, meaning it currently doesn't support floating point numbers or more complicated equations. This is something I might improve upon later, provided I and others find it useful enough. For now, though, it's just for simple calculations, doubling as both proof of concept and Python practice.
