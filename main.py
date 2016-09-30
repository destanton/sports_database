import psycopg2

connection = psycopg2.connect("dbname=my_sports_team")
cursor = connection.cursor()

print("""Welcome to the Chicago Cubs 2016 Sports Database!
This database allows you to seach the starting line-up by player name,
by player position, and runs-batted-in(rbi).
""")


def search_options():
    choice = input("Would you like to search by [F]irst name, [Last] name, [P]osition, [R]BI, or [A]dd player\n> ").lower()
    if choice == "f":
        name = input("What is the first name you want to search for? ").lower()
        cursor.execute("SELECT * FROM cubbies_data WHERE first_name = %s;", (name, ))
    elif choice == "l":
        last_name = input("last name? ").lower()
        cursor.execute("SELECT * FROM cubbies_data WHERE last_name = %s;", (last_name, ))
    elif choice == "p":
        position = input("Would you like to sort by position? Y/n ")
        cursor.execute("SELECT first_name, position FROM cubbies_data;")
    elif choice == "r":
        rbi = input("rbi? ")
        cursor.execute("SELECT first_name, rbi FROM cubbies_data;")
    elif choice == "a":
        add_player()
    else:
        search_options()
    results = cursor.fetchall()
    results = list(results)
    print(results)


def next_search():
    option = input("What would you like to do next? ")


def add_player():
    first_name = input("First Name: ").lower()
    last_name = input("Last Name: ").lower()

    cursor.execute("INSERT INTO first_name, last_name VALUES (%s,%s)", (first_name, last_name))

search_options()
cursor.close()
connection.close()
