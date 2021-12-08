#!/usr/bin/bash

git add -A .;
text=$(uname -o;date);git commit -m "$text";git push