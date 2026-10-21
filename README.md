# Network Traffic Analyzer (Python)

## The Problem
Security analysts use tools like Wireshark to monitor network traffic, but manually reading through thousands of lines of logs to find suspicious IPs is slow.

## The Solution
A Python script that parses network traffic logs, identifies HTTP and DNS requests, and automatically flags traffic coming from a known suspicious IP address.

## How It Works
- Reads a text file containing network logs.
- Iterates line-by-line using Python file I/O.
- Uses conditional logic to alert on specific IP addresses.

## What I Learned
- How to parse text files in Python.
- How to apply basic network security logic (flagging known bad IPs) using code.
- How to output clear, actionable alerts for a SOC team.

## Screenshot
<img width="807" height="267" alt="image" src="https://github.com/user-attachments/assets/1cf6ec68-d2ce-47aa-848a-c23c264e913e" />
