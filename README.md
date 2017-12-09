# SpellingCorrection
Program gives a suggestion for that misspelled word

To download all dataset: https://ii.metu.edu.tr/metu-corpus-development-group (METU-Sabanci Turkish Treebank)

This project gives suggestion word for that misspelled word.

- User enters a word

- Program calculates a length of entered word

- " SELECT DISTINCT word FROM nlp.xmlfiles where char_length(word) >=%d and char_length(word) <=%d and word like '%s%%'" %(oneMinus,onePlus,FirstTwoChar) "

with this sql command, takes words which are greater than one minus lengnt of word, smaller than one plus length of word and first two char is equal of entered word.

- Levenshtein distance algorithm is used that calculate distances between entered word and datasets that already takes with sql command. 

- If Minimum Distance is not equal Zero, it means that entered word misspelled and the program suggest words which are equal minimum distance
