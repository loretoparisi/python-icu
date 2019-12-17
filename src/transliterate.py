from polyglot.transliteration import Transliterator
from polyglot.downloader import downloader

print(downloader.supported_languages_table("transliteration2"))

# traditional chinese
s = u'親愛的牽起你的手 並將他們放在我手中'

s = u"Hello"
transliterator = Transliterator(source_lang="en", target_lang="zh")
print(s, "--->", transliterator.transliterate(u"Hello"))