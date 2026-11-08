#!/usr/bin/env bash
set -euo pipefail
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip git curl
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
printf '%s\n' 'Cài Ollama theo https://docs.ollama.com/linux; kiểm tra script cài trước khi chạy.'
printf '%s\n' 'Sao chép .env.example thành .env và điền model/digest/endpoint thực tế.'
