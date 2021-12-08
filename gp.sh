#!/usr/bin/bash

git add -A .;
text=$(date;uname -o);git commit -m "$text";git push