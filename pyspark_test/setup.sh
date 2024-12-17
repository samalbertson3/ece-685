#!/bin/bash

sudo yum update -y
sudo yum install python -y
sudo yum install python3-pip -y

pip install boto3
pip install pandas
pip install pyspark