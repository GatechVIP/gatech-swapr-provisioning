#!/bin/bash

echo -e "$2\n$2" | smbpasswd -s -a $1
