from user import User

my_user = User('leo.f.s.trimble@gmail.com', 'Leo', 'Trimble', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('leo.f.s.trimble@gmail.com')

print(user_from_db)

my_user.save_to_db()
