import sqlite3

# connecting to a database
conn = sqlite3.connect('user.db')

# creating a cursor
c = conn.cursor()

# creating a client table
c.execute("""CREATE TABLE client(
user_name text,
first_name text,
last_name text,
password text,
gender text,
date_of_birth text,
mobile_number integer,
email text,
minute_remaining integer
    )""")

# creating a payment table
c.execute("""CREATE TABLE payment(
payment_id integer,
date text,
offer_no integer
    )""")

# creating a offer table
c.execute("""CREATE TABLE offer(
offer_number integer,
minute integer,
last_date text
    )""")

# creating a log_in_instance table
c.execute("""CREATE TABLE log_in_instance(
log_in_time text,
last_active text
    )""")

# creating a request_state table
c.execute("""CREATE TABLE request_state(
dial_takes integer,
status text,
selected_category text,
start_time text,
connection_start_time text,
end_time text
    )""")

# creating an agent table
c.execute("""CREATE TABLE agent(
agent_id integer,
first_name text,
last_name text,
category text,
call_received text,
status text,
call_duration integer,
shift_start_time text,
shift_end_time text
    )""")

# # inserting data in the table manually
# c.execute("INSERT INTO client VALUES ('BigC', 'Shoabur Rahman', 'Chishty', 'abc234', 'Male', '01/01/1999', 01712121212, 'chishty828rahman@gmail.com', 23)")

# commit command
conn.commit()

# close connection
conn.close()

