from datetime import datetime
from random import choice
from app import app, db
from models import User


# Create the application context
app.app_context().push()

# Seeding users
print("👥 Seeding users...")
users = [
    {"name": "John Doe", "email": "john@example.com", "password": "password1"},
    {"name": "Jane Smith", "email": "jane@example.com", "password": "password2"},
    {"name": "Bob Johnson", "email": "bob@example.com", "password": "password3"},
]

for user_data in users:
    user = User(**user_data)
    db.session.add(user)

db.session.commit()

print("👥 Done seeding!")
