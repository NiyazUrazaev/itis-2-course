import psycopg2

conn = psycopg2.connect(
    host='postgresql',
    port=15432,
    user='backlog',
    password='backlog',
    dbname='backlog',
)

cur = conn.cursor()

cur.execute('select id, status, comment from public.offer limit 10;')
a = cur.fetchall()
print(a)

cur.execute("insert into public.table_name (name) values ('qwe');")
conn.commit()

cur.close()
conn.close()