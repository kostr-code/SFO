import parsing


class Worker:

    def __init__(self):
        self.name = None
        self.this_tasks = []
        self.next_tasks = []
        self.this_cards = []
        self.next_cards = []
        self.this_week = []
        self.next_week = []

    def __int__(self, name: str):
        self.name = name
        self.this_tasks = []
        self.next_tasks = []
        self.this_cards = []
        self.next_cards = []
        self.this_week = []
        self.next_week = []

    def week_make(self, tw, flag):
        """Блок с парсингом планов работников на эту и на следующую неделю"""
        if flag == 1:
            self.this_week.append(tw)
        else:
            self.next_week.append(tw)

    def make_tasks(self):
        """Блок с созданием списка номеров карточек для последующего парсинга."""
        for link in self.this_week:
            code = link.split('/')[-1].split(' ')[0]
            if not code.isdigit() or len(code) != 7:
                print(f'Проблема у "{self.name}" с ссылкой {link}, проверьте формат')
            else:
                self.this_cards.append(code)
        for link in self.next_week:
            code = link.split('/')[-1].split(' ')[0]
            if not code.isdigit() or len(code) != 7:
                print(f'Проблема у "{self.name}" с ссылкой {link}, проверьте формат')
            else:
                self.next_cards.append(code)
        self.pars()

    def pars(self):
        self.this_tasks = parsing.parsing(self.this_cards)
        self.next_tasks = parsing.parsing(self.next_cards)


