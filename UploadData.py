import MySQLdb
import xml.etree.ElementTree as ET


files= open('namelist.txt','r')

filesName=files.read().split()


# Open database connection
db = MySQLdb.connect("localhost","root","PASSWORD","nlp",charset="utf8")
# prepare a cursor object using cursor() method
cursor = db.cursor()
db.names="utf8"
# execute SQL query using execute() method.

#cursor.execute("DROP TABLE IF EXISTS XmlFiles")

# Create table as per requirement
sql1 = """CREATE TABLE xmlfiles (
         FileName LONGTEXT NOT NULL,
         SentenceNo LONGTEXT,
         IX LONGTEXT,  
         LEM LONGTEXT,
         MORPH LONGTEXT,
         IG LONGTEXT,
         REL LONGTEXT,
         Word LONGTEXT)"""

cursor.execute(sql1)

for file in range(len(filesName)):

  tree = ET.parse('YOUR_FILE_PATH' + filesName[file])
  FileNAME= filesName[file]
  root = tree.getroot()
  root.tag
  'sentences'
  root.attrib
  {}

  for counter1 in range(len(root)):
    SentenceNumber=counter1+1
    for counter2 in range(len(root[counter1])):
      for ch in root[counter1][counter2].iter('W'):
        IX=ch.get('IX')
        LEM=ch.get('LEM')
        MORPH=ch.get('MORPH')
        IG=ch.get('IG')
        REL=ch.get('REL')
        WORD=root[counter1][counter2].text.strip()

# Prepare SQL query to INSERT a record into the database.
        sql2 = "INSERT INTO XmlFiles(FileName,SentenceNo,IX,LEM,MORPH,IG,REL,Word)\
         VALUES ("'"%s"'", "'"%s"'", "'"%s"'", "'"%s"'", "'"%s"'",'%s', "'"%s"'", "'"%s"'")" % \
               (FileNAME, SentenceNumber, IX, LEM, MORPH, IG, REL, WORD)
        try:
# Execute the SQL command
          cursor.execute(sql2)

# Commit your changes in the database
          db.commit()
        except:
          # Rollback in case there is any error
         db.rollback()

# disconnect from server
db.close()
