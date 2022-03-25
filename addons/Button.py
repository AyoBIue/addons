from typing import Optional, Union
import discord

class Button:
  def __init__(self, style: Optional[int], label='None', custom_id=None, url=None, emoji: Optional[Union[str, discord.Emoji]]=None):
    self.label = label
    self.style = style
    self.custom_id = custom_id
    self.url = url
    self.emoji = emoji
    
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

      self.emoji = emoji

  def to_dict(self):
    data = {
      'type': 2
    }
    if self.style:
      data['style'] = self.style

    if self.label:
      data['label'] = self.label

    if self.custom_id:
      data['custom_id'] = self.custom_id

    if self.url:
      data['url'] = self.url

    if self.emoji:
      data['emoji'] = self.emoji

    return data