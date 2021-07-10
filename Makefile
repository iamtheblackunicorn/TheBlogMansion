setup: ; python manage.py makemigrations && python manage.py migrate
su: ; python manage.py createsuperuser
serve: ; python manage.py runserver
clean: ; rm -rf db.sqlite3
