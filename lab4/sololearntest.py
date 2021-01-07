class GameObject:
  class_name = ""
  desc = ""
  objects = {}
  health = 3

  def __init__(self, name):

    self.health = 3
    self._desc = " A foul creature"



  @property
  def desc(self):
    print("kkkk")
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    print ("ggg")
    self._desc = value

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

class Elf(GameObject):
  class_name = "elf"
  desc = "A wonderful creature"

goblin = Goblin("Gobbly")
elf = Elf("Elly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

def finde(noun):
  if noun == "here":
    x = "here is " +" and ".join(list(GameObject.objects.keys()))
    return x
  else:
    return "There is nobody."

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    print (thing)
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      print (thing.health)
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else:
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun)
  return msg

def get_input():
#  print (GameObject.objects)
  command = input(": ").split()
  try:
    verb_word = command[0]
  except IndexError:
    print("You said nothing")
    return
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return
  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
  "examine": examine,
  "finde": finde,
  "hit": hit,
}

while True:
  get_input()