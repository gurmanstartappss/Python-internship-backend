from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg://postgres:postgres@localhost/company")

with engine.connect() as con:
    result = con.execute(text("select * from employees"))

    for row in result:
        print(row)