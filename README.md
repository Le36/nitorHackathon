# nitorHackathon

# How to? #

To run this project you will need Python and PostgreSQL.

Start by cloning this project. Enter root and create file called ```.env``` and paste the following there:

```
DATABASE_URL=your postgres address
SECRET_KEY=your secret key
```

then do the following commands:

```
python3 -m venv venv
source venv/bin/activate
```

install requirements with:

```pip install -r requirements.txt```

add correct tables to postgres with:

```psql < schema.sql```

and run with:

```flask run```