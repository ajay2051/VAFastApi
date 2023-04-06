pip install fastapi uvicorn fastapi-sqlalchemy pydantic alembic psycopg2 python-dotenv


docker-compose build
docker-compose up


docker-compose build --up

alembic init alembic


docker compose run app alembic revision --autogenerate -m "New Migration"

docker compose run app alembic upgrade head


Relationship between book and author not working.