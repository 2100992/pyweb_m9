def parse_db_url(db_link):
    #парсим строку со ссылкой на базу данных
    #два варианта:
    #1 - 'postgres://admin:oocooSh7@postgres.host:5432/my_db'
    #2 - 'sqlite:///C:/Users/admin/site_db.sqlite3'
    import re
    db = {}
    if ':///' in db_link:
        engine, name  = db_link.split(':///')
        db['ENGINE'] = engine
        db['NAME'] = name

    elif '://' in db_link:
        engine, user, password, host, port, name = re.findall(r"[\w'^'.']+", db_link)
        db['ENGINE'] = engine
        db['USER'] = user
        db['PASSWORD'] = password
        db['HOST'] = host
        db['PORT'] = port
        db['NAME'] = name

    else:
        raise ValueError

    return db