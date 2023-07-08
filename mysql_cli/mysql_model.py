"""实体类文件."""
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Actor(Base):
    __tablename__ = 'actor'
    actor_id: Mapped[int] = mapped_column(primary_key=True)
    actor_bio: Mapped[str] = mapped_column(Text)
    actor_chName: Mapped[str] = mapped_column(String(100))
    actor_foreName: Mapped[str] = mapped_column(String(100))
    actor_nationality: Mapped[str] = mapped_column(String(100))
    actor_constellation: Mapped[str] = mapped_column(String(100))
    actor_birthPlace: Mapped[str] = mapped_column(String(100))
    actor_birthDay: Mapped[str] = mapped_column(String(100))
    actor_repWorks: Mapped[str] = mapped_column(String(100))
    actor_achiem: Mapped[str] = mapped_column(Text)
    actor_brokerage: Mapped[str] = mapped_column(String(100))


class Movie(Base):
    __tablename__ = 'movie'
    movie_id: Mapped[int] = mapped_column(primary_key=True)
    movie_bio: Mapped[str] = mapped_column(Text)
    movie_chName: Mapped[str] = mapped_column(String(100))
    movie_foreName: Mapped[str] = mapped_column(String(100))
    movie_prodTime: Mapped[str] = mapped_column(String(100))
    movie_prodCompany: Mapped[str] = mapped_column(String(100))
    movie_director: Mapped[str] = mapped_column(String(100))
    movie_screenwriter: Mapped[str] = mapped_column(String(100))
    movie_genre: Mapped[str] = mapped_column(String(100))
    movie_star: Mapped[str] = mapped_column(Text)
    movie_length: Mapped[str] = mapped_column(String(100))
    movie_rekeaseTime: Mapped[str] = mapped_column(String(100))
    movie_length: Mapped[str] = mapped_column(String(100))
    movie_achiem: Mapped[str] = mapped_column(Text)

