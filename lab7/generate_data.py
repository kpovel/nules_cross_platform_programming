import psycopg2
from faker import Faker
import random

fake = Faker("uk_UA")


db_connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5433"
)


for _ in range(5):
    cursor = db_connection.cursor()

    cursor.execute(
        """insert into client(type, address, first_name, last_name, middle_name)
        values (%s, %s, %s, %s, %s)""",
        (random.choice(["agency", "individual"]), fake.address(),
         fake.first_name(),
         fake.last_name(),
         fake.middle_name()
         )
    )
    db_connection.commit()
