from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
tofu = Pet(name='Tofu', species='cat', age=15)
dilla = Pet(name='Dilla', species='cat', age=10)
kiley = Pet(name='Kiley', species='dog', age=12, available=False)
db.session.add(tofu)
db.session.add(dilla)
db.session.add(kiley)
db.session.commit()
