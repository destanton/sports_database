import psycopg2

connection = psycopg2.connect("dbname=my_sports_team")
cursor = connection.cursor()

print("""Welcome to the Chicago Cubs 2016 Starting Line-Up Sports Database!
You will be allowed to search the database by player name and player stats.

Your 2016 starting line up:
MIGUEL MONTERO    ANTHONY RIZZO     BEN ZOBRIST    ADDISON RUSSELL

KRIS BRYANT    JORGE SOLER    DEXTER FOWLER    JASON HEYWARD
""")


def search_options():
    choice = input("Would you like to search by [F]irst name, [Last] name, [S]tats \n>").lower()
    if choice == "s":
        stats()
    elif choice == "f":
        name = input("What is the first name you want to search for? ").lower()
        cursor.execute("SELECT * FROM cubbies_data WHERE first_name = %s;", (name, ))
        results = cursor.fetchall()
    elif choice == "l":
        last_name = input("last name? ").lower()
        cursor.execute("SELECT * FROM cubbies_data WHERE last_name = %s;", (last_name, ))
        results = cursor.fetchall()
    for row in results:
        print('rank: {}, pos: {}, fn: {}, ln: {}, age: {}, at-bats: {}, runs: {}, hits: {}, hr: {}, rbi: {}\n'.format(
               row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]).upper())
    search_options()


def stats():
    choice = input("Do you want to search by [P]osition, see player [S]tats, or [A]dd a player? ").lower()
    if choice == "p":
        position_search()
    elif choice == "s":
        player_stats()
    elif choice == "a":
        add_player(rank)


def position_search():
    choice = input("""Which position would you like to search?
Enter input as 'c' for catcher, 'lf' for left field, '2b' for second base: """).lower()
    if choice != "c, 1b, 2b, 3b, ss, lf, cf, rf ":
        cursor.execute("SELECT first_name, position FROM cubbies_data;")
        results = cursor.fetchall()
        for row in results:
            print('{} {}'.format(row[0], row[1]).upper())
        search_options()
    else:
        search_options()


def player_stats():
    choice = input("""\nWhich stats do you want to see?
1. [R]bi
2. [A]t-Bats
3. [RU]ns
4. [H]its
5. [HO]meruns
6. [RE]turn to menu\n>""").lower()
    if choice == "r":
        cursor.execute("SELECT first_name, last_name, rbi FROM cubbies_data;")
        results = cursor.fetchall()
        for row in results:
            print('{}, {}, rbi: {}' .format(row[0], row[1], row[2]).upper())
        player_stats()
    elif choice == "a":
        cursor.execute("SELECT first_name, last_name, at_bat FROM cubbies_data;")
        results = cursor.fetchall()
        for row in results:
            print('{}, {}, at-bats: {}' .format(row[0], row[1], row[2]).upper())
        player_stats()
    elif choice == "ru":
        cursor.execute("SELECT first_name, last_name, runs FROM cubbies_data;")
        results = cursor.fetchall()
        for row in results:
            print('{}, {}, runs: {}' .format(row[0], row[1], row[2]).upper())
        player_stats()
    elif choice == "h":
        cursor.execute("SELECT first_name, last_name, hits FROM cubbies_data;")
        results = cursor.fetchall()
        for row in results:
            print('{}, {}, hits: {}' .format(row[0], row[1], row[2]).upper())
        player_stats()
    elif choice == "ho":
        cursor.execute("SELECT first_name, last_name, homeruns FROM cubbies_data;")
        results = cursor.fetchall()
        for row in results:
            print('{}, {}, HR: {}' .format(row[0], row[1], row[2]).upper())
        player_stats()
    elif choice == "re":
        search_options()

rank = 8


def add_player(rank):
    position = input("Player position: ").lower()
    first_name = input("First Name: ").lower()
    last_name = input("Last Name: ").lower()
    age = input("Player Age: ").lower()
    at_bat = input("At bats: ")
    runs = input("Runs: ")
    hits = input("Hits: ")
    homeruns = input("Homeruns: ")
    rbi = input("RBIs: ")
    rank += 1
    cursor.execute("INSERT INTO cubbies_data (rank, position, first_name, last_name, age, at_bat, runs, hits, homeruns, rbi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (rank, position, first_name, last_name, age, at_bat, runs, hits, homeruns, rbi))
    search_options()

search_options()
cursor.close()
connection.close()
