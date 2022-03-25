class SelectMenu:
  def __init__(self, custom_id, placeholder, min=1, max=1):
    self.custom_id = str(custom_id)
    self.placeholder = str(placeholder)
    self.min = min
    self.max = max
    self.options = None

  def add_option(self, label, value, description=None, emoji=None):
    _data = {
      'label': str(label),
      'value': str(value),
    }
    if emoji:
      if type(emoji).__name__ == 'Emoji':
        emoji = {
          'name': emoji.name,
          'id': str(emoji.id)
        }
      elif emoji.startswith('<'):
        emoji = emoji.split(':')
        emoji = {
          'name': emoji[1],
          'id': str(emoji[2][:-1])
        }
      else:
        emoji = {
          'name': emoji,
          'id': None
        }

      _data['emoji'] = emoji
    
    if description:
      _data['description'] = description

    try:
      self.options.append(_data)
    except:
      self.options = [_data]

  def remove_option(self, index: int) -> None:
    try:
      del self.options[index]
    except:
      return False

  def to_dict(self):
    try:
      return {
        'type': 3,
        'custom_id': self.custom_id,
        'placeholder': self.placeholder,
        'min_values': self.min,
        'max_values': self.max,
        'options': self.options
      }
    except:
      return {
        'type': 3,
        'custom_id': self.custom_id,
        'placeholder': self.placeholder,
        'options': []
      }
