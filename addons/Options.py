class Option:
  def __init__(self, _type: int, name, description: str=None, required: bool=True):
    self.name = name
    self.type = _type
    self.description = description
    self.required = required
    self.choices = []

  def add_choice(self, name, value):
    for i in range(0, len(self.choices)):
      if self.choices[i]['name'] == name:
        raise TypeError(name + ' is already a Choice!')
      else:
        pass

    self.choices.append({
      'name': name,
      'value': value
    })

  def to_dict(self):
    x = {
      'name': self.name,
      'type': self.type,
      'required': self.required
    }
    if self.description:
      x['description'] = self.description
    
    if self.choices:
      x['choices'] = self.choices

    return x