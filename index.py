import os

senhaPostgres = input('Senha do postgres:')
loginPgAdmin = input('Login PgAdmin:')
senhaPgAdmin = input('Senha PgAdmin:')

os.system('docker pull postgres')

os.system('docker pull dpage/pgadmin4')

os.system('docker network create --driver bridge postgres-network')

os.system('docker create -v /var/lib/postgresql/data --name PostgresData alpine')

os.system('docker run -p 5432:5432 --network=postgres-network --name PostgresContainer -e POSTGRES_PASSWORD='+ senhaPostgres +' -d --volumes-from PostgresData postgres')

os.system('docker run --name PgAdmin --network=postgres-network -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL='+ loginPgAdmin +'" -e "PGADMIN_DEFAULT_PASSWORD='+ senhaPgAdmin +'" -d dpage/pgadmin4')