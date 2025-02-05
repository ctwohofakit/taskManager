
#This environment variable tells Flask how to find your app(so it can run it)
export FLASK_APP=app/routes.py

#set enviroment to development
export FLASK_ENV=developemnt
#enables debug mode, ehich will also trigger :auto-reload:(server restarts when you save changes)
export FLASK_DEBUG=1

flask run