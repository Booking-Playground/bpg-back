superuser:
	docker compose -f docker-compose.dev.yml exec backend python manage.py createsuperuser

run:
	docker compose -f docker-compose.dev.yml up -d