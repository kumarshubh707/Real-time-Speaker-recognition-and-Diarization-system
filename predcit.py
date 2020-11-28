import requests

headers = {'Authorization' : 'Token 3715119fd7753d33bedbd3c2832752ee7b0a10c7'}
data = {'user' : '310' ,'language' : 'EN'}
files = {'audio_file' : open('wavs/final_primary_speaker_audio.mp3','rb')}
url = 'https://dev.liv.ai/liv_transcription_api/recordings/'
res = requests.post(url, headers = headers, data = data, files = files)
print(res.content)
with open('outputfile.json', 'wb') as outf:
    outf.write(res.content)
