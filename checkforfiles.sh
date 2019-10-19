#!/bin/bash

dir=/home/USERNAME/Downloads/

inotifywait -m -r -e create "$dir" | while read f

do
    python main.py
done