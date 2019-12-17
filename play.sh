#!/bin/bash
docker build -t python3_playground .
docker run --rm -it -v $(PWD)/src:/root python3_playground