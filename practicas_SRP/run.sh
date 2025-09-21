#!/bin/bash
echo "Ejecutando main.py..."
python main.py

echo "Ejecutando tests..."
pytest -v
