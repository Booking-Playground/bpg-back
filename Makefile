build_statics:
	sudo docker compose exec backend python manage.py collectstatic

migrate: build_statics
	sudo docker compose exec backend python manage.py migrate

superuser:
	sudo docker compose exec backend python manage.py createsuperuser

run_production_docker:
	sudo docker compose -f docker-compose.production.yml up -d

run_dev_docker:
	docker compose -f docker-compose.dev.yml up -d