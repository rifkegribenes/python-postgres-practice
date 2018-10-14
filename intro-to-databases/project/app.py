from user import User

# my_user = User('max.v.s.trimble@gmail.com', 'Max', 'Trimble', None)
my_user = User.load_from_db_by_email('max.v.s.trimble@gmail.com')

print(my_user)
# my_user.save_to_db()