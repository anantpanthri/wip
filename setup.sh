pip3 install flask_sqlalchemy
pip3 install flask_cors
pip3 install flask --upgrade
pip3 uninstall flask-socketio
service postgresql start
su -i postgres bash -c "psql < setup.sql"
su -i postgres bash -c "psql bookshelf < books.psql"
