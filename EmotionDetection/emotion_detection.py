
import requests  
import json

def emotion_detector(text_to_analyse):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    myobj= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy":None,
            "sadness":None,
            "dominant_emotion":None
            }
    res =  json.loads(response.text)['emotionPredictions'][0]['emotion']  # Return the response text from the API
    Keymax = max(res, key= lambda x: res[x])
    res['dominant_emotion'] = Keymax
    return res
    
