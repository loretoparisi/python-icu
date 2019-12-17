import polyglot
from polyglot.text import Text, Word


# japanese
s = u'退屈であくびばっかしていた毎日'
t = Text(s)
print(s, " = ", t.words)

# simplified chinese
s = u'天啊你的闪耀我亲眼所见'
t = Text(s)
print(s," = ", t.words)

# traditional chinese
s = u'親愛的牽起你的手 並將他們放在我手中'
t = Text(s)
print(s," = ", t.words)


