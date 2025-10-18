#!/bin/bash
rm dist/bad_ls
rm ansible/bad_ls
pyinstaller --onefile --collect-all netifaces --hidden-import=netifaces --add-binary "/usr/lib/x86_64-linux-gnu/libc.so.6:." bad_ls.py
cp dist/bad_ls ansible/
chmod u+x dist/bad_ls