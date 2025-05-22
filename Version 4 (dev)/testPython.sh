#!/bin/bash
exec > /tmp/test_python_log.txt 2>&1
cd "/mnt/DATA/Documents/Github/musicGenerator/Version 4 (dev)"
/home/hunter/.pyenv/shims/python3 RunSongGen.py