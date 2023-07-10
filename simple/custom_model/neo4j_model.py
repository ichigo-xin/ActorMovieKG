from py2neo.ogm import Model, Property, RelatedFrom, RelatedTo


class Movie(Model):
    __primarylabel__ = 'Movie'

    movie_id = Property()
    movie_bio = Property()
    movie_chName = Property()
    movie_foreName = Property()
    movie_prodTime = Property()
    movie_prodCompany = Property()
    movie_director = Property()
    movie_screenwriter = Property()
    movie_genre = Property()
    movie_star = Property()
    movie_length = Property()
    movie_rekeaseTime = Property()
    movie_length = Property()
    movie_achiem = Property()

    actors = RelatedFrom("Actor", "ACTED_IN")


class Actor(Model):
    # 标签
    __primarylabel__ = "Actor"

    # 属性
    actor_id = Property()
    actor_bio = Property()
    actor_chName = Property()
    actor_foreName = Property()
    actor_nationality = Property()
    actor_constellation = Property()
    actor_birthPlace = Property()
    actor_birthDay = Property()
    actor_repWorks = Property()
    actor_achiem = Property()
    actor_brokerage = Property()

    acted_in = RelatedTo(Movie)
