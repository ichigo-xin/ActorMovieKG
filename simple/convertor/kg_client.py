from py2neo.ogm import Repository

from simple.custom_model.neo4j_model import Actor


class KGClient:

    def __init__(self):
        self.repo = Repository("bolt://neo4j@127.0.0.1:7687", password="123456")

    def build_graph(self):
        cypher = """CALL gds.graph.project(
            'ActorMovieGraph',
            ['Actor', 'Movie'],
            'ACTED_IN'
        );
        """
        self.repo.graph.run(cypher)

    def query_similarity(self, name: str):
        """找出演员中的紧密程度"""
        cypher = f"""CALL gds.nodeSimilarity.stream('ActorMovieGraph')
        YIELD node1, node2, similarity 
        WITH gds.util.asNode(node1) AS actor1, gds.util.asNode(node2) AS actor2, similarity
        WHERE actor1.actor_chName = '{name}'
        RETURN actor1.actor_chName, actor2.actor_chName, similarity
        ORDER BY similarity DESCENDING
        """
        result = self.repo.graph.run(cypher).data()
        print(result)

    def query_all_movies(self, name: str):
        actor = self.repo.match(Actor).where(
            actor_chName=name
        ).first()
        if actor is None:
            raise ValueError('input error!')
        for movie in actor.acted_in:
            print(movie.movie_chName)


if __name__ == '__main__':
    kg_client = KGClient()
    # kg_client.build_graph()
    # kg_client.query_all_movies("张家辉")
    kg_client.query_similarity("鲍方")
