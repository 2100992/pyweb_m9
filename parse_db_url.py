def parse_db_url(db_link):
    #парсим строку со ссылкой на базу данных
    #два варианта:
    #1 - 'postgres://admin:oocooSh7@postgres.host:5432/my_db'
    #2 - 'sqlite:///C:/Users/admin/site_db.sqlite3'
    import re
    db = {}
    engine = db_link.split('://')[0]
    if engine == 'postgres':
        engine, user, password, host, port, name = re.findall(r"[\w'^'.']+", db_link)
        db['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        db['USER'] = user
        db['PASSWORD'] = password
        db['HOST'] = host
        db['PORT'] = port
        db['NAME'] = name
    elif engine == 'sqlite':
        engine, name  = db_link.split(':///')
        db['ENGINE'] = 'django.db.backends.sqlite3'
        db['NAME'] = name
    else:
        raise ValueError
    return db