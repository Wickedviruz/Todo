## databas migrering ##

python -m flask db init
python -m flask db migrate -m "migrerings information"
python -m flask db upgrade

## create requirements.txt ##
pip freeze > requirements.txt