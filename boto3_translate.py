# Translate (languages)

translate = boto3.client('translate',
region_name = '',
aws_access_key_id = AWS KEY_ID,
aws_secret_access_key=AWS_SECRET)

response = translate.translate_text(
Text = 'Hello, how are you doing?',
SourceLanguage = 'auto', # this is using AWS resource "comprehend"
TargetLanguageCode = 'es')


# Comprehend (language type detection and sentiment)
comprehend = boto3.client('comprehend',
region_name = '',
aws_access_key_id = AWS KEY_ID,
aws_secret_access_key=AWS_SECRET)

response = comprehend.detect_dominant_language(Text = 'Hola amigo!')
top_lanuage = response['Languages'][0]['LanguageCode']

sentiment = comprehend.detect_sentiment(Text = 'I love it!', LanguageCode='en')['Sentiment'])
