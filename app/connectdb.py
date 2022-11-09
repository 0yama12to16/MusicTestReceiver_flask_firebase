import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


cred = credentials.Certificate(".secret/datacollection-for-mer-usinge4-\
firebase-adminsdk-mejle-bd0e263ebb.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def post2db(data):
    subjectName = str(data["subjectName"])
    subjectID = int(data["subjectID"])
    songID = int(data["songID"])
    arousalOrValence = ""
    arousal = data["arousal"]
    arousal_time = data["arousal_time"]
    valence = data["valence"]
    valence_time = data["valence_time"]
    ibi = data["ibi"]
    ibi_time = data["ibi_time"]
    bvp = data["bvp"]
    bvp_time = data["bvp_time"]
    gsr = data["gsr"]
    gsr_time = data["gsr_time"]
    temp = data["temp"]
    temp_time = data["temp_time"]
    subjectAge = data["subjectAge"]
    
    if data["isValence"]:
        arousalOrValence = "valence"
    else:
        arousalOrValence = "arousal"

    #createdATはUTCタイムゾーンで取るため、日本時間とは九時間ずれてる
    dt_now = datetime.datetime.now()
    createdAt = f"{dt_now.year}_{dt_now.month}_{dt_now.day}_{dt_now.hour}_{dt_now.minute}_{dt_now.second}"
    print(dt_now.year)

    doc_name = f"{subjectID}-{songID}-{createdAt}-{arousalOrValence}" 
    doc_ref = db.collection(str(songID)).document(doc_name)
    doc_ref.set({
        'subjectName':subjectName,
        'age':subjectAge,
        'subjectID':subjectID,
        'songID':songID,
        'arousal':arousal,
        'arousal_time':arousal_time,
        'valence':valence,
        'valence_time':valence_time,
        'ibi':ibi,
        'ibi_time':ibi_time,
        'bvp':bvp,
        'bvp_time':bvp_time,
        'gsr':gsr,
        'gsr_time':gsr_time,
        'temp':temp,
        'temp_time':temp_time,
        'createdAt':createdAt
    })
    return True

def getMusicList(numberOfMusics):
    musicList = []
    doc_ref = db.collection('collectedData').list_documents()
    musicList.append(len(list(doc_ref)))
    return musicList
