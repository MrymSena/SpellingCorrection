import coding as coding
import pymysql
pymysql.install_as_MySQLdb()
coding
#!/usr/bin/python
import json
import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","PASSWORD","nlp",charset="utf8")
# prepare a cursor object using cursor() method
cursor = db.cursor()
db.names="utf8"

Distance=[]
Suggest=[]


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

inputWord = input("Lütfen bir kelime girin: ")

length=len(inputWord)
oneMinus=length-1
onePlus=length+1
FirstTwoChar=inputWord[:2]
sqlforCorpus="SELECT DISTINCT word FROM nlp.xmlfiles where char_length(word) >=%d and char_length(word) <=%d and word like '%s%%'" %(oneMinus,onePlus,FirstTwoChar)
cursor.execute(sqlforCorpus)
db.commit()
WordsArray = cursor.fetchall()

a=0;

for row in WordsArray:
    word=row[0].lower();
    inputw=inputWord.lower();
    dis= levenshtein(word,inputw)
    Distance.append(dis)
    Suggest.append(row[0])
    a = a + 1

if(min(Distance)!=0):
    print "Asagidakilerden birini mi demek istediniz:"
#print minD
    for dist in range(len(Distance)):
        if(Distance[dist]==min(Distance)):
            print Suggest[dist].lower();

