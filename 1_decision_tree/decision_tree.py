from typing import NamedTuple, List, Set


class Choice(NamedTuple):
    name: str
    probability: float
    value: int


class Decision(NamedTuple):
    name: str
    choices: Set[Choice]

    def calculate_utility(self) -> float:
        utility = sum((c.probability * c.value for c in self.choices))
        print(f'{self.name} -> Utility: {utility}')
        return utility


class Tree(NamedTuple):
    name: str
    decisions: List[Decision]

    def __str__(self):
        return f'{self.name} ({len(self.decisions)} decisions)'


if __name__ == '__main__':
    trees = [

        Tree(
            name='Operation',
            decisions=[
                Decision(name='Do not operate', choices={
                    Choice(name='Recover', probability=.3, value=100),
                    Choice(name='Injured', probability=.7, value=20),
                }),
                Decision(name='Operate', choices={
                    Choice(name='success', probability=.65, value=80),
                    Choice(name='failure', probability=.35, value=0),
                }),
            ]
        ),

        Tree(
            name='Gamble',
            decisions=[
                Decision(name='Play gamble (A)', choices={
                    Choice(name='Win', probability=.2, value=45),
                    Choice(name='Loss', probability=.8, value=0),
                }),
                Decision(name='Play gamble (B)', choices={
                    Choice(name='win', probability=.25, value=30),
                    Choice(name='Loss', probability=.75, value=0),
                }),
            ]
        ),

        Tree(
            name='Juror',
            decisions=[
                Decision(name='Acquit', choices={
                    Choice(name='Defendant is truly innocent', probability=.8, value=100),
                    Choice(name='Defendant is truly guilty', probability=.2, value=30),
                }),
                Decision(name='Convict', choices={
                    Choice(name='Defendant is truly innocent', probability=.1, value=0),
                    Choice(name='Defendant is truly guilty', probability=.9, value=80),
                }),
            ]
        )

    ]

    for tree in trees:
        print(tree)
        for decision in tree.decisions:
            decision.calculate_utility()
        print()
