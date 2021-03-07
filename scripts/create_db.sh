#!/bin/sh
user="bff"
database="bff"
password="bff"

PGPASSWORD=$password dropdb -U $user -h localhost -p 5433 --echo $database

psql -U postgres -c "DROP USER IF EXISTS $user;"
psql -U postgres -c "create user $user with password '$password';"
psql -U postgres -c "alter user $user with valid until 'infinity';"
psql -U postgres -c "alter user $user with createdb;"

PGPASSWORD=$password createdb -U $user -h localhost -p 5433 --echo $database

psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $database TO $user;"
