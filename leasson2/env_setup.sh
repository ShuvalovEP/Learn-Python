#! /usr/bin/env bash

if [ -e ./env ]; then
	echo "Удаление старого env"
	rm -rf env >> log.txt 2>&1
	echo "Создание нового env"
	python3 -m venv env >> log.txt 2>&1
else
	echo "Создание env"
	python3 -m venv env >> log.txt 2>&1
fi