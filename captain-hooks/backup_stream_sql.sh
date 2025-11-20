# docker-compose run -T  --rm pg-0 pg_dump --format=p --dbname=backend --clean --create -h pgpool -U postgres | restic $HOST -r $URI backup --tag stream --stdin --stdin-filename pg_dump.sql
source ./__tinkerbell__.sh

echorun echo "hi" | restic $HOST -r $URI backup --tag stream --stdin --stdin-filename pg_dump.sql