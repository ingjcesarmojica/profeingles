#!/usr/bin/env bash
# Script de build para Render
set -e

echo "=== Instalando dependencias ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Creando carpetas necesarias ==="
mkdir -p data
mkdir -p data/instance

echo "=== Build completado ==="
