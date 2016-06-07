from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Movie, Features, Base

engine = create_engine('sqlite:///app.db')
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


# movie1 = Movie(title="Alien")

# session.add(movie1)
# session.commit()

# features1 = Features(filename='alien.jpg', description='Placeholder', year='1979', director='Ridley Scott', trailer='jQ5lPt9edzQ', movie=movie1)

# session.add(features1)
# session.commit()

# movie2 = Movie(title="Terminator")

# session.add(movie2)
# session.commit()

# features2 = Features(filename='terminator.jpg', description='Placeholder', year='1984', director='James Cameron', trailer='jQ5lPt9edzQ', movie=movie2)

# session.add(features2)
# session.commit()

# t = Movie(title="Abyss")

# session.add(t)
# session.commit()

# f = Features(filename='abyss.jpg', description='Placeholder', year='1989', director='James Cameron', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()

# t = Movie(title="Robocop")

# session.add(t)
# session.commit()

# f = Features(filename='robocop.jpg', description='Placeholder', year='1987', director='Paul Verhoeven', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()

# t = Movie(title="The Thing")

# session.add(t)
# session.commit()

# f = Features(filename='thing.jpg', description='Placeholder', year='1982', director='John Carpenter', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()

# t = Movie(title="Bladerunner")

# session.add(t)
# session.commit()

# f = Features(filename='bladerunner.jpg', description='Placeholder', year='1982', director='Ridley Scott', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()

# t = Movie(title="Mad Max: The Road Warrior")

# session.add(t)
# session.commit()

# f = Features(filename='madmax2.jpg', description='Placeholder', year='1979', director='George Miller', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()

# t = Movie(title="Predator")

# session.add(t)
# session.commit()

# f = Features(filename='predator.jpg', description='Placeholder', year='1987', director='John McTiernan', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()

# t = Movie(title="Predator")

# session.add(t)
# session.commit()

# f = Features(filename='predator.jpg', description='Placeholder', year='1987', director='John McTiernan', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()

# t = Movie(title="Prometheus")

# session.add(t)
# session.commit()

# f = Features(filename='prometheus.jpg', description='Placeholder', year='2012', director='Ridley Scott', trailer='jQ5lPt9edzQ', movie=t)

# session.add(f)
# session.commit()



print "added items!"