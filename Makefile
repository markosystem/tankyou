setup:
	@echo "Instaling dependences..."
	pip install -r requirements.txt
	@echo ""

migrate:
	@echo "Running migrations..."
	python manage.py migrate
	@echo ""

tests:
	@echo "Run the tests to analyze the integrity of the database..."
	python manage.py test
	@echo ""

createuser:
	@echo "Admin user creation. Please provide the requested information..."
	python manage.py createsuperuser
	@echo ""

run:
	@echo "Initialize server..."
	python manage.py runserver
	@echo ""

all: setup migrate tests run