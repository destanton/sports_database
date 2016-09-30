import psycopg2

connection = psycopg2.connect("dbname=my_sports_team")
cursor = connection.cursor()

print("""Welcome to the Chicago Cubs 2016 Sports Database!
This database allows you to seach the starting line-up by player name,
by player position, and runs-batted-in(rbi).
""")


def search_options():
    choice = input("Would you like to search by [F]irst name or [Last] name\n>").lower() #", [P]osition, [R]BI, or [A]dd player\n> ").lower()
    if choice == "f":
        name = input("What is the first name you want to search for? ").lower()
        cursor.execute("SELECT * FROM cubbies_data WHERE first_name = %s;", (name, ))
        results = cursor.fetchall()
    elif choice == "l":
        last_name = input("last name? ").lower()
        cursor.execute("SELECT * FROM cubbies_data WHERE last_name = %s;", (last_name, ))
        results = cursor.fetchall()
    for row in results:
        print('rank: {}, position: {}, first: {}, last: {}, age: {}, at-bats: {}, runs: {}, hits: {}, hr: {}, rbi: {}'.format(
               row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]).upper())
    stats()
    # elif choice == "r":
    #     rbi = input("rbi? ")
    #     cursor.execute("SELECT first_name, rbi FROM cubbies_data;")
    # elif choice == "a":
    #     add_player(rank)
    # else:
    #     search_options()
    # results = cursor.fetchall()
    # print(results)
def stats():
    choice = input("Do you want to search by [P]osition, see player [S]tats, or [A]dd a player? ").lower()
    if choice == "p":
        position_search()
    elif choice == "s":
        player_stats()


def position_search():
    choice = input("Would you like to sort by position? Y/n ")
    if choice == "p":
        cursor.execute("SELECT first_name, position FROM cubbies_data;")
        results = cursor.fetchall()
        for row in results:
            print('{} {}'.format(row[0], row[1]).upper())


def player_stats():
    choice = input("Which stats do you want to see? ")

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
