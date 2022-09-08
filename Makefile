start_dev_webservice:
	cd ./frontend && docker-compose -f docker-compose.dev.yml up

stop_dev_webservice:
	cd ./frontend && docker-compose -f docker-compose.dev.yml down

start_prod_webservice:
	cd ./frontend && docker-compose -f docker-compose.prod.yml up -d

stop_prod_webservice:
	cd ./frontend && docker-compose -f docker-compose.prod.yml down

start_db:
	cd ./backend/postgres && docker-compose -f docker-compose.yml up -d

start_backend:
	cd ./backend/card_service && docker-compose -f docker-compose.yml up --force-recreate \
	--remove-orphans --build --renew-anon-volumes