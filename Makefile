superuser:
	sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser

superuser_dev:
	docker compose -f docker-compose.dev.yml exec backend python manage.py createsuperuser

run:
	sudo docker compose -f docker-compose.production.yml up -d

run_dev:
	docker compose -f docker-compose.dev.yml up -d