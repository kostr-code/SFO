import parsing


class Worker:

    def __init__(self):
        self.name = None
        self.links = None
        self.this_tasks = []
        self.next_tasks = []
        self.this_cards = []
        self.next_cards = []
        self.this_week = []
        self.next_week = []


    def make_tasks(self):
        for link in self.this_week:
            self.this_cards.append(link.split('/')[-1].split(' ')[0])
        for link in self.next_week:
            self.next_cards.append(link.split('/')[-1].split(' ')[0])
        self.pars()

    def pars(self):
        self.this_tasks = parsing.parsing(self.this_cards)
        self.next_tasks = parsing.parsing(self.next_cards)

    def out(self) -> list:
        tasks = [self.name, 'Эта неделя:']
        for i in self.this_tasks:
            s = '- ' + i
            tasks.append(s)
        tasks.append('Следующая неделя:')
        for i in self.next_tasks:
            s = '- ' + i
            tasks.append(s)
        return tasks
