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

#http://docs.sqlalchemy.org/en/rel_1_0/orm/session_basics.html#basics-of-using-a-session

# a = session.query(Movie).all()

# for i in a:
#     print i.id, i.title

# a = session.query(Features).all()

# for i in a:
#     print i.id, i.filename, i.description, i.year, i.director, i.trailer

# title = session.query(Features).filter_by(id='1').one()
# print title.id

# j = session.query(Features).filter_by(id='1').one()
# print j.description
# j.description = "After a space merchant vessel perceives an unknown transmission as distress call, \
# their landing on the source planet finds one of the crew attacked by a mysterious lifeform. \
# Continuing their journey back to Earth with the attacked crew having recovered and the critter \
# deceased, they soon realize that its life cycle has merely begun."
# print j.description
# session.add(j)
# session.commit()

# j = session.query(Features).filter_by(id='3').one()
# j.trailer = "4zbpL3LeW7k"
# j.description = "A civilian diving team is enlisted to search for a lost nuclear submarine and face danger while encountering an alien aquatic species."

# session.add(j)
# session.commit()

# j = session.query(Features).filter_by(id='4').one()
# j.description="In a dystopic and crime-ridden Detroit, a terminally wounded cop returns to the force as a powerful cyborg haunted by submerged memories."
# j.trailer="6tC_5mp3udE"
# session.add(j)
# session.commit()

# j = session.query(Features).filter_by(id='5').one()
# j.description="It's the first week of winter in 1982. An American Research Base is greeted by an alien force, that can assimilate anything it touches. It's up to the members to stay alive, and be sure of who is human, and who has become one of the Things."
# j.trailer="ymJ1jrNLgT0"
# session.add(j)
# session.commit()

# j = session.query(Features).filter_by(id='6').one()
# j.description="A blade runner must pursue and try to terminate four replicants who stole a ship in space and have returned to Earth to find their creator."
# j.trailer="eogpIG53Cis"
# session.add(j)
# session.commit()

# j = session.query(Features).filter_by(id='7').one()
# j.description="In the post-apocalyptic Australian wasteland, a cynical drifter agrees to help a small, gasoline rich, community escape a band of bandits."
# j.trailer="UlwtiOyaoo0"
# session.add(j)
# session.commit()

# j = session.query(Features).filter_by(id='8').one()
# j.description="A team of commandos on a mission in a Central American jungle find themselves hunted by an extra-terrestrial warrior."
# j.trailer="Y1txEAywdiw"
# session.add(j)
# session.commit()

# j = session.query(Features).filter_by(id='9').one()
# j.description="Following clues to the origin of mankind a team journey across the universe and find a structure on a distant planet containing a monolithic statue of a humanoid head and stone cylinders of alien blood but they soon find they are not alone."
# j.trailer="nmJOO6D5RvA"
# session.add(j)
# session.commit()