from button.BaseButton import BaseButton


class Toggle(BaseButton):

    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(**kwargs)
        # BaseButton.__init__(BaseButton(), kwargs)
        self.state = False
        self.color = kwargs["colors"][0]

    def onclick(self):
        if self.state:
            self.color = self.colors[1]
        else:
            self.color = self.colors[0]
        self.state = not self.state
