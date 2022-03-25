class Components:
  def __init__(self):
    self.selectmenu = []
    self.buttons = {}

  def to_dict(self):
    x = 1
    comp = []
    for i in range(0, len(self.selectmenu)):
      comp.append({
        'type': 1,
        'components': [self.selectmenu[i]]
      })

    while True:
      if self.buttons.get(x):
        comp.append({
          'type': 1,
          'components': self.buttons[x]
        })
        x += 1
      else:
        break

    return comp

  def add_components(self, args: list):
    x = 1
    y = 1
    for arg in args:
      if type(arg).__name__ == 'SelectMenu':
        self.selectmenu.append(arg.to_dict())

      elif type(arg).__name__ == 'Button':
        if self.buttons.get(x) != None:
          if len(self.buttons[x]) == 5:
            x += 1
            self.buttons[x] = []
            self.buttons[x].append(arg.to_dict())
          else:
            self.buttons[x].append(arg.to_dict())
        else:
          self.buttons[x] = []
          self.buttons[x].append(arg.to_dict())
