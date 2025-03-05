#!/bin/bash

for pdf in papers/*.pdf; do
    echo "Procesando: $pdf"
    python3 script1.py "$pdf" > "$pdf"1.txt
    python3 script2.py "$pdf" > "$pdf"2.txt
    python3 script3.py "$pdf" > "$pdf"3.txt
done
