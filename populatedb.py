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

session.query(Item).delete()
session.commit()

Fashion = Category(name = "Bed & Bath")

session.add(Fashion)
session.commit()

Sports = Category(name = "Travel Essentials")

session.add(Sports)
session.commit()

Music = Category(name = "Electronics")

session.add(Music)
session.commit()



print("added items!")
