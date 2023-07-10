from py2neo import Relationship
from py2neo.ogm import Repository
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

from simple.custom_model import neo4j_model, mysql_model


def covertor_actor(mysql_actor: mysql_model.Actor):
    neo4j_actor = neo4j_model.Actor()
    neo4j_actor.actor_id = mysql_actor.actor_id
    neo4j_actor.actor_bio = mysql_actor.actor_bio
    neo4j_actor.actor_chName = mysql_actor.actor_chName
    neo4j_actor.actor_foreName = mysql_actor.actor_foreName
    neo4j_actor.actor_nationality = mysql_actor.actor_nationality
    neo4j_actor.actor_constellation = mysql_actor.actor_constellation
    neo4j_actor.actor_birthPlace = mysql_actor.actor_birthPlace
    neo4j_actor.actor_birthDay = mysql_actor.actor_birthDay
    neo4j_actor.actor_repWorks = mysql_actor.actor_repWorks
    neo4j_actor.actor_achiem = mysql_actor.actor_achiem
    neo4j_actor.actor_brokerage = mysql_actor.actor_brokerage
    return neo4j_actor


def covertor_movie(actor_movie: mysql_model.Movie):
    neo4j_movie = neo4j_model.Movie()
    neo4j_movie.movie_id = actor_movie.movie_id
    neo4j_movie.movie_bio = actor_movie.movie_bio
    neo4j_movie.movie_chName = actor_movie.movie_chName
    neo4j_movie.movie_foreName = actor_movie.movie_foreName
    neo4j_movie.movie_prodTime = actor_movie.movie_prodTime
    neo4j_movie.movie_prodCompany = actor_movie.movie_prodCompany
    neo4j_movie.movie_director = actor_movie.movie_director
    neo4j_movie.movie_screenwriter = actor_movie.movie_screenwriter
    neo4j_movie.movie_genre = actor_movie.movie_genre
    neo4j_movie.movie_star = actor_movie.movie_star
    neo4j_movie.movie_length = actor_movie.movie_length
    neo4j_movie.movie_rekeaseTime = actor_movie.movie_rekeaseTime
    neo4j_movie.movie_length = actor_movie.movie_length
    neo4j_movie.movie_achiem = actor_movie.movie_achiem
    return neo4j_movie


class ActorMovieKG:

    def __init__(self):
        self.repo = Repository("bolt://neo4j@127.0.0.1:7687", password="123456")
        self.engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/kg')
        self.session = Session(self.engine)

    def build_graph(self):
        # self.build_actor()
        # self.build_movie()
        self.build_rel()

    def build_movie(self):
        stmt_movie = select(mysql_model.Movie)
        for actor_movie in self.session.scalars(stmt_movie):
            neo4j_movie = covertor_movie(actor_movie)
            self.repo.save(neo4j_movie)
        print('build movie success')

    def build_actor(self):
        stmt_actor = select(mysql_model.Actor)
        for actor_mysql in self.session.scalars(stmt_actor):
            neo4j_actor = covertor_actor(actor_mysql)
            self.repo.save(neo4j_actor)
        print('build actor success')

    def build_rel(self):
        stmt = select(mysql_model.ActorToMovie)
        for element in self.session.scalars(stmt):
            actor = self.repo.match(neo4j_model.Actor).where(actor_id=element.actor_id).first().__node__
            movie = self.repo.match(neo4j_model.Movie).where(movie_id=element.movie_id).first().__node__
            relation_ship = Relationship(actor, "ACTED_IN", movie)
            self.repo.create(relation_ship)
        print('build relation success')

    def test(self):
        actor = self.repo.match(neo4j_model.Actor).where(actor_id=3).first().__node__
        movie = self.repo.match(neo4j_model.Movie).where(movie_id=6493).first().__node__
        relation_ship = Relationship(actor, "ACTED_IN", movie)
        self.repo.create(relation_ship)


if __name__ == '__main__':
    kg = ActorMovieKG()
    # kg.test()
    kg.build_graph()
    print("建立知识图谱完成")
