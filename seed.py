from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
tofu = Pet(name='Tofu', species='cat', age=15, photo_url='https://mylostpetalert.com/wp-content/uploads/pet_photos/c8b99f22c38a53d515fe6f05aeadd874-1.jpeg')
nala = Pet(name='Nala', species='cat', photo_url='https://mylostpetalert.com/wp-content/uploads/pet_photos/cf8b2766fe26e37b536d87ba8158f0fb.jpeg', age=6, available=False)
toot = Pet(name='Toot', species='bird', photo_url='https://mylostpetalert.com/wp-content/uploads/pet_photos/5566b6a88e64a72b64c8d529d27b1a2d.jpg', age=2)
dilla = Pet(name='Dilla', species='cat', age=10)
kiley = Pet(name='Kiley', species='dog', photo_url='https://mylostpetalert.com/wp-content/uploads/pet_photos/f1dd7369c7545e17c8dcd36655ceb31c.jpeg', age=12, available=False)
db.session.add(tofu)
db.session.add(nala)
db.session.add(toot)
db.session.add(dilla)
db.session.add(kiley)
db.session.commit()
