install:
	pip install -r requirements.txt

run:
	docker compose up

stop:
	docker compose down

test:
	pytest tests/

format:
	black .

lint:
	flake8 .

clean:
	rm -rf __pycache__