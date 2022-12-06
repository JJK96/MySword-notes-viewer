#!/usr/bin/env bash
dir=$(dirname "$0")
output_file=$dir/tmp.sqlite
database=$dir/versenotes.mybible
gdown 11EnVESX8w3v7aVQIWfBY-cD-BWc7UkcL -O $output_file && \
mv $output_file $database
