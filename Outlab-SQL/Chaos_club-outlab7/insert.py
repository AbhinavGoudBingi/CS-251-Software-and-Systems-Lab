import sqlite3,pandas
mydb=sqlite3.connect('ipl.db')
my=mydb.cursor()
pandas.read_csv('team.csv').to_sql('TEAM',mydb, if_exists='append', index=False)
pandas.read_csv('player.csv').to_sql('PLAYER',mydb, if_exists='append', index=False)
pandas.read_csv('match.csv').to_sql('MATCH',mydb, if_exists='append', index=False)
pandas.read_csv('player_match.csv').to_sql('PLAYER_MATCH',mydb, if_exists='append', index=False)
pandas.read_csv('ball_by_ball.csv').to_sql('BALL_BY_BALL',mydb, if_exists='append', index=False)
mydb.commit()
mydb.close()