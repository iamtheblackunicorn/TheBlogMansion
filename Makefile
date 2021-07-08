setup: ; python manage.py makemigrations && python manage.py migrate
serve: ; python manage.py runserver
clean: ; rm -rf db.sqlite3
