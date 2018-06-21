#! /usr/bin/env bash

if [ -e ./env ]; then
	echo "Удаление старого env окружения"
	rm -rf env >> log.txt 2>&1
	echo "Создание нового env окружения"
	python3 -m venv env >> log.txt 2>&1
else
	echo "Создание нового env окружения"
	python3 -m venv env >> log.txt 2>&1
fi