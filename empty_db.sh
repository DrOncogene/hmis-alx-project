#!/bin/bash

echo "drop database hmis_dev_db" |  mysql -uroot
mysql -uroot < dev_db_setup.sql
