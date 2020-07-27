'''export FLASK_APP=flaskr
export FLASK_ENV=development

pip3 install flask_sqlalchemy
pip3 install flask_cors
pip3 install flask --upgrade
pip3 uninstall flask-socketio -y


su - postgres bash -c "psql < /home/workspace/backend/setup.sql"
su - postgres bash -c "psql bookshelf < /home/workspace/backend/books.psql"root@6cc3b5d0f099:/home/w
/home/workspace/backend/setup.sql
-----------------
pagination logic
-----------------

    def paginate_books(request,selection):
        page=request.args.get('page',1,type=int)
        start=(page-1)*BOOKS_PER_SHELF
        end=start+BOOKS_PER_SHELF
        books=[book.format() for book in selection]
        cur_book= books[start:end]
        print(cur_book)
        return cur_book




        '''
