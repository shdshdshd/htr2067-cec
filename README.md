# Yamaha HTR-2067 CEC No Audio Workaround

## Overview

This script provides a workaround for a known issue with the Yamaha HTR-2067 receiver where audio fails to output when HDMI-connected devices (such as Chromecast) begin playback.

## Requirements

- An additional HDMI-connected device (e.g., Raspberry Pi) to run the script
- Device must be connected to an available HDMI input on the receiver

## Setup

The workaround has been tested with the following configuration:
- Script-running device connected to TV HDMI port(first from the left)
- CEC (Consumer Electronics Control) enabled and HDMI controls enabled on the HTR

## Dependencies

- cec-ctl cmd needs to be available

## Usage

[python ./main.py]

## How It Works

Script is listening for a particular CEC message, and triggers an power toggle on the HTR
