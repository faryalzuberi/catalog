from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_database_setup import Category, Base, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

Fashion = Category(name = "Fashion")

session.add(Fashion)
session.commit()

Travel = Category(name = "Travel Essentials")

session.add(Travel)
session.commit()

Music = Category(name = "Music")

session.add(Music)
session.commit()

Electronics = Category(name = "Electronics")

session.add(Electronics)
session.commit()

BedBath = Category(name = "Bed & Bath")

session.add(BedBath)
session.commit()

Sports = Category(name = "Sports")

session.add(Sports)
session.commit()

item = Item(name = "Flat Screen TV", description="Make your friday nights a little less lonely by watching your favourite characters come to life", category_id=4)
session.add(item)
session.commit()

item = Item(name = "Speakers", description="Music so loud your neighbours will definitely hate you", category_id=4)
session.add(item)
session.commit()

item = Item(name="Tennis Shoes", description="You won't even need a new dress with these shoes. You'll have beyonce crazy in love", category_id=6)
session.add(item)
session.commit()

item = Item(name="Golf Balls", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." ,category_id=6)
session.add(item)
session.commit()

item = Item(name="Cricket Bats", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." ,category_id=6)
session.add(item)
session.commit()

item = Item(name="Baseball Bats", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." ,category_id=6)
session.add(item)
session.commit()

item = Item(name="Bath Bombs", description="Available in all your favourite colours!", category_id=5)
session.add(item)
session.commit()

item = Item(name="Fairy Lights", description="Tranform you room with a warm & cozy glow. Perfect for that wintet Xmas vibe", category_id=5)
session.add(item)
session.commit()

item = Item(name="Violin", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." ,category_id=3)
session.add(item)
session.commit()

item = Item(name="Guitar", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." ,category_id=3)
session.add(item)
session.commit()

item = Item(name="Cello", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", category_id=3)
session.add(item)
session.commit()

item = Item(name="Neck Rest", description="Say goodbye to stiff necks forever. A must have travel buddy to accompany you on your adventures to comfortville.", category_id=2)
session.add(item)
session.commit()

item = Item(name="Eyeshadow Palette", description="Create a gorgeous summer look with our earthy pastels", category_id=1)
session.add(item)
session.commit()

item = Item(name="Stilletos", description="You'll never look better dismantling the patriarchy if you're wearing these babies", category_id=1)
session.add(item)
session.commit()
print("added items!")
