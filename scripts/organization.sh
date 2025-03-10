#!/bin/bash

ROOT_DIR="ingresso-bounty"
DIRECTORIES=(
	"$ROOT_DIR/Pre-Engagement"
	"$ROOT_DIR/Reconnaissance/Subdomains"
	"$ROOT_DIR/Reconnaissance/Ports-Services"
	"$ROOT_DIR/Reconnaissance/Technologies"
	"$ROOT_DIR/WebApp-Pentesting/Information-Gathering"
	"$ROOT_DIR/WebApp-Pentesting/Vulnerablity-Assessment"
	"$ROOT_DIR/WebApp-Pentesting/Exploitation"
	"$ROOT_DIR/Reporting"
	"$ROOT_DIR/Results"
	"$ROOT_DIR/Tools"
	"$ROOT_DIR/Notes"
	)
for dir in "${DIRECTORIES[@]}"; do
	mkdir -p "$dir"
	echo "Criado: $dir"
done

touch "$ROOT_DIR/Notes/README.md"
touch "$ROOT_DIR/Reporting/bug-report-template.md"
echo "Estruturas de diretórios criada com sucesso!"
