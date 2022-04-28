import parsing


class Worker:

    def __init__(self):
        self.name = None
        self.links = None
        self.tasks = []
        self.cards = []

    def __int__(self, name: str, links: list[str]):
        self.name = name
        self.links = links
        self.tasks = []
        self.cards = []

    def make_tasks(self):
        for link in self.links:
            self.cards.append(link.split('/')[-1])
        self.pars()

    def pars(self):
        self.tasks = parsing.parsing(self.cards)

    def out(self) -> list:
        tasks = [self.name]
        a = 1
        for i in self.tasks:
            s = '- ' + i
            tasks.append(s)
            a += 1
        return tasks
