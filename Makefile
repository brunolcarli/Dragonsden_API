install:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:6776

migrate:
	python manage.py makemigrations
	python manage.py migrate
