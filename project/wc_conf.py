class WooCommerce():
  def __init__(self):
    self.cunsumer_key = 'ck_d30d8e9e39516a408e69a835c112f7121ce31d3e'
    self.consumer_secret = 'cs_416994aa534b9fa7eebdd047ae58deb87eee4e93'

  def get_key(self):
    if type(self.cunsumer_key) == int or type(self.cunsumer_key) == float:
      return 'The key must not numerical value'
  
    elif not (self.cunsumer_key.startswith('ck_')):
      return 'The key starts with ck'

    elif (len(self.cunsumer_key)) < 25:
      return 'The key is too short'

    else:
      return self.cunsumer_key


  def get_secret(self):
    if type(self.consumer_secret) == int or type(self.consumer_secret) == float:
      return 'The secret must not numerical value'
  
    elif not (self.consumer_secret.startswith('cs_')):
      return 'The secret starts with cs'
      
    elif (len(self.consumer_secret)) < 20:
      return 'The secret is too short'
      
    else:
      return self.consumer_secret