import os


def query_pritty_print(query):
    os.system(
        'echo "{query}" | PGPASSWORD="password" psql -h localhost -p 5433 -U postgres -d postgres'
        .format(query=query)
    )

# Відобразити всіх клієнтів, які є фізичними особами. Відсортувати по прізвищу
# клієнта;


query_pritty_print("""
select *
from client
where type = 'individual'
order by last_name;
""")

# Порахувати кількість клієнтів, які є фізичними особами, та кількість
# клієнтів, які являються відомством(підсумковий запит)

query_pritty_print("""
select count(*)
from client
where type = 'individual';
""")


query_pritty_print("""
select count(*)
from client
where type = 'agency';
""")

# Порахувати вартість кожної розмови (запит з обчислювальним полем);

query_pritty_print("""
select c.duration_minutes, c.phone_id, t.call_type, c.duration_minutes * t.price_per_minute_cent as call_price
from conversation as c
         join tariff t on c.tariff_id = t.id;
""")

# Відобразити список всіх розмов з обраним типом дзвінка (запит з параметром);

query_pritty_print("""select c.* from conversation as c
join tariff t on c.tariff_id = t.id
where t.call_type = 'внутрішній';""")

# Порахувати загальну вартість всіх розмов для кожного клієнта (підсумковий запит);

query_pritty_print("""
with client_total_spent as (select client.id,
                                   sum(c.duration_minutes * t.price_per_minute_cent) as client_total_spent
                            from client
                                     join phone p on client.id = p.client_id
                                     join conversation c on p.id = c.phone_id
                                     join tariff t on t.id = c.tariff_id
                            group by client.id)


select first_name, last_name, client_total_spent
from client_total_spent as cts
         join client on client.id = cts.id;
""")

# Порахувати кількість хвилин кожного типу дзвінків для кожного клієнта (перехресний запит).

query_pritty_print("""select client.id as client_id, t.call_type, sum(c.duration_minutes) as conversation_minuts from client
                  join phone p on client.id = p.client_id
                  join conversation c on p.id = c.phone_id
                  join tariff t on t.id = c.tariff_id
group by client.id, t.id
order by client.id;""")
