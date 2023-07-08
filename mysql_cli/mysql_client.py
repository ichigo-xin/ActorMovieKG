from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

# 初始化数据库连接，修改为你的数据库用户名和密码
from mysql_cli.mysql_model import Actor

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/kg')
session = Session(engine)

stmt = select(Actor).where(Actor.actor_chName.in_(["周星驰", "朱茵"]))
for actor in session.scalars(stmt):
    print(actor.actor_repWorks)
