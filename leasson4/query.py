from db import User

for user in User.query.all():
    print(user.first_name)

print(User.query.filter(User.first_name=='Фёкла').first())

print(User.query.filter(User.first_name.like('П%')).all())

print(User.query.order_by(User.email).all())

print(User.query.order_by(User.email.desc()).all())

print(User.query.filter(User.last_name.like('%ов%')).order_by(User.first_name).all())

