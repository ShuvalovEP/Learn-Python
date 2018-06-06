from db import db_session, User

authors = [
{
    'first_name': 'Фёкла',
    'last_name': 'Ильинишна',
    'email': 'FI@gmail.com'
},
{
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'email': 'II@gmail.com'
},
{
    'first_name': 'Петр',
    'last_name': 'Петров',
    'email': 'PP@gmail.com'
}
]

for row in authors:
    author = User(row['first_name'], row['last_name'], row['email'])
    db_session.add(author)

db_session.commit()