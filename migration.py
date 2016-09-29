import csv
import psycopg2

connection = psycopg2.connect("dbname=my_sports_team user=my_sports_team")
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS cubbies_data;")

create_table_command = """
CREATE TABLE cubbies_data (
    rank serial PRIMARY KEY,
    position VARCHAR(30),
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age NUMERIC(2),
    at_bat NUMERIC(4),
    runs NUMERIC(4),
    hits NUMERIC(4),
    homeruns NUMERIC(4),
    rbi NUMERIC(4)
);
"""

cursor.execute(create_table_command)
with open("cubs_2016.csv") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=["rank", "position", "first_name", "last_name", "age", "at_bat", "runs", "hits", "homeruns", "rbi"])
        for row in reader:
            cursor.execute("INSERT INTO cubbies_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (row ["rank"], row["position"], row["first_name"], row["last_name"], row["age"], row["at_bat"], row["runs"], row["hits"], row["homeruns"], row["rbi"]))
        # cursor.execute("INSERT INTO cubbies_data VALUES (1, 'catcher', 'miguel', 'montero', 32, 237, 31, 50, 7, 31)")
        # cursor.execute("INSERT INTO cubbies_data VALUES (2, 'sarah', 'safety', 1982, 'joel')")
connection.commit()
cursor.close()
connection.close()
