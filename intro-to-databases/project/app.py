from database import Database
from user import User

Database.initialize(database="learning",
                    user='sarahschneider',
                    password='Q-@VWfZPUbM3M5xCyRTu',
                    host="localhost")

user = User('test@test.com', 'testFirstName', 'testLastName', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('rifkegribenes@gmail.com')

print(user_from_db)
