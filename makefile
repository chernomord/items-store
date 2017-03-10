freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

collectstatic:
	python manage.py collectstatic

deploy-heroku:
	git push heroku master