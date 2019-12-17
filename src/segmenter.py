# ICU examples
# @see http://site.icu-project.org/
# @author loretoparisi at gmail dot com
#
import icu
from icu import Locale,BreakIterator

def wordBreakIterator(lang):
    return BreakIterator.createWordInstance(Locale(lang))

def charBreakIterator(lang):
    return BreakIterator.createCharacterInstance(Locale(lang))

def printBoundaries(txt, bi):
    bi.setText(txt)
    start = bi.first()
    tokens = []
    try:
        while True:
            end = next(bi)
            print("[{}, {})".format(start, end))
            tokens.append(txt[start:end])
            start = end
    except StopIteration:
        pass

def wordSegmenter(txt, bi):
    '''
        segment word into boundaries
    '''
    tokens = []
    bi.setText(txt)
    start = bi.first()
    try:
        while True:
            end = next(bi)
            tokens.append(txt[start:end])
            start = end
    except StopIteration:
        pass
    return tokens

if __name__ == "__main__":
    text = u'退屈であくびばっかしていた毎日'

    print("Word boundaries:", text)
    printBoundaries(text, wordBreakIterator("ja"))
    tokens = wordSegmenter(text, wordBreakIterator("ja"))
    print(tokens)

    print("Character boundaries:", text)
    printBoundaries(text, charBreakIterator("ja"))