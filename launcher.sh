#!/bin/bash
# AUTO-UPDATER
cd /home/suraj/.gemini/antigravity/scratch/heavy_suite/zero-mesh-windows
git pull origin main --quiet
python3 zero_mesh_gui.py
