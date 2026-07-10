from dataclasses import dataclass, field


RELATIONS = {
    "Vợ chồng": 2000,
    "Anh chị em ruột": 900,
    "Cha mẹ - con": 700,
    "Anh chị em họ": 500,
    "Dì/Chú/Bác - Cháu": 300,
    "Bạn bè": 100,
    "Không quen": 0
}


@dataclass
class Guest:
    name: str


@dataclass
class Relation:
    guest1: str
    guest2: str
    relation_type: str
    score: int


@dataclass
class WeddingData:

    guests: list = field(default_factory=list)

    relations: list = field(default_factory=list)

    def add_guest(self, name):

        name = name.strip()

        if name == "":
            return False

        if name in self.guests:
            return False

        self.guests.append(name)

        return True

    def remove_guest(self, name):

        if name not in self.guests:
            return

        self.guests.remove(name)

        self.relations = [
            r for r in self.relations
            if r.guest1 != name and r.guest2 != name
        ]

    def add_relation(
            self,
            guest1,
            guest2,
            relation_type):

        if guest1 == guest2:
            return False

        score = RELATIONS[relation_type]

        found = False

        for r in self.relations:

            if (
                (r.guest1 == guest1 and r.guest2 == guest2)
                or
                (r.guest1 == guest2 and r.guest2 == guest1)
            ):

                r.relation_type = relation_type
                r.score = score

                found = True

                break

        if not found:

            self.relations.append(
                Relation(
                    guest1,
                    guest2,
                    relation_type,
                    score
                )
            )

        return True

    def get_relation_score(
            self,
            guest1,
            guest2):

        if guest1 == guest2:
            return 0

        for r in self.relations:

            if (
                (r.guest1 == guest1 and r.guest2 == guest2)
                or
                (r.guest1 == guest2 and r.guest2 == guest1)
            ):

                return r.score

        return 0

    def build_matrix(self):

        n = len(self.guests)

        matrix = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        for i in range(n):

            for j in range(n):

                if i == j:
                    continue

                matrix[i][j] = self.get_relation_score(
                    self.guests[i],
                    self.guests[j]
                )

        return matrix

    def to_dict(self):

        return {
            "guests": self.guests,
            "relations": [
                {
                    "guest1": r.guest1,
                    "guest2": r.guest2,
                    "relation_type": r.relation_type,
                    "score": r.score
                }
                for r in self.relations
            ]
        }

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        obj.guests = data.get(
            "guests",
            []
        )

        for r in data.get(
                "relations",
                []):

            obj.relations.append(
                Relation(
                    r["guest1"],
                    r["guest2"],
                    r["relation_type"],
                    r["score"]
                )
            )

        return obj