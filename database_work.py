from sqlalchemy import update, select

# TODO: FIX THIS!!!!
def update_login_time(user, time, db):
    print(user.username)
    print(time)
    print(db)
    stmt = (
        select(db.user).
        where(db.user.c.username == user.username)
    )
    print(f'stmt: {stmt}')
