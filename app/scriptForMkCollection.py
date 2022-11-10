import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(".secret/datacollection-for-mer-usinge4-\
firebase-adminsdk-mejle-bd0e263ebb.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


files = './MusicDictionary.csv'

f = open(files, 'r')
data = f.read()
f.close()
lst1 = data.split(',')
print(lst1)


doc_ref = db.collection(str(8)).document("1")
doc_ref.set({
        'subjectName':'1'
})


#最初はこちらのループを回して、ドキュメントとともにコレクションを作成、その後、ブラウザで、ドキュメント"1"を開いた後、ここをコメントアウト、下のループのコメントアウトを外してそれぞれのコレクション内のドキュメントを削除

for file in lst1:
    doc_ref = db.collection(str(file)).document("1")
    doc_ref.set({
        'subjectName':'1'
    })

"""
for file in lst1:
    db.collection(str(file)).document("1").delete()
"""