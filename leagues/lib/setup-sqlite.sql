[
    { 'name' : 'user',
      'sql' : [
        'CREATE TABLE user',
        '(id INTEGER PRIMARY KEY,',
        'name TEXT,',
        'password TEXT)'
        ]
    },

        cursor.execute("""
            CREATE TABLE team
            (id INTEGER PRIMARY KEY,
            name TEXT,
            ownerId INTEGER,
            FOREIGN KEY(ownerId) REFERENCES user(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE match
            (id INTEGER PRIMARY KEY,
            name TEXT,
            homeTeamId INTEGER,
            awayTeamId INTEGER,
            homeTeamScore INTEGER,
            awayTeamScore INTEGER,
            played INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE fixture
            (id INTEGER PRIMARY KEY,
            name TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE fixtureMatch
            (fixtureId INTEGER,
            matchId INTEGER,
            FOREIGN KEY(fixtureId) REFERENCES fixture(id),
            FOREIGN KEY(matchId) REFERENCES match(id)
            )
        """)
