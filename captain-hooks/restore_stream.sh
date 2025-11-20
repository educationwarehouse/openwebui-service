#!/bin/bash
# recover the backup from the stream snapshot and save it in the migrate/data directory where edwh-migrate will pick it
# up and restore it to the database. Instead of saving the file, you could also pipe the output to the psql application
# make sure the filename (postgres.sql) matches the one used in the backup script.
source __tinkerbell__.sh

restic $HOST -r $URI dump $SNAPSHOT --tag stream database.sqlofzo > ./path/to/destination
