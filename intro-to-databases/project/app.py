from user import User

# my_user = User('leo.f.s.trimble@gmail.com', 'Leo', 'Trimble', None)
my_user = User.load_from_db_by_email('leo.f.s.trimble@gmail.com')

print(my_user)
# my_user.save_to_db()