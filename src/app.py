import json
import boto3

#Using boto3 to call the Comprehend API
client = boto3.client('comprehend')

#Lambda function to work with Comprehend
def lambda_handler(event, context):
    
    body = json.loads(event.get('body', '{}'))
    text = body['message']
    print ("El texto a analizar es:", text)
 
    print("\ndetectando idioma....")
    res_lang = client.detect_dominant_language(Text=text)
    languages = res_lang['Languages']
    lang_code = languages[0]['LanguageCode']
    print("Idioma detectado:", lang_code)

    print("\niniciando analisis de sentimiento....")
    #print(json.dumps(client.detect_sentiment(Text=text, LanguageCode=lang_code), sort_keys=True, indent=4))
    sentiment = client.detect_sentiment(Text=text, LanguageCode=lang_code) #API call for sentiment analysis
    sentRes = sentiment['Sentiment'] #Positive, Neutral, or Negative
    sentScore = sentiment['SentimentScore'] #Percentage of Positive, Neutral, and Negative
    print(sentRes)
    print(sentScore)

    print("\niniciando extraccion de entidades....")
    entities = client.detect_entities(Text=text, LanguageCode=lang_code) #API call for entity extraction
    entities = entities['Entities'] #all entities
    #print(entities)
    textEntities = [dict_item['Text'] for dict_item in entities] #the text that has been identified as entities
    typeEntities = [dict_item['Type'] for dict_item in entities] #the type of entity the text is
    print(textEntities)
    print(typeEntities)

    return {
        'statusCode': 200,
        'body': str(sentiment) + str(entities)  #body returned from our function
    }
