
import requests


REFRESH_TOKEN = 'ZT9RCsKBcwHaLCPulKmDFXWPxpwfoYtAdYunn5qgeVWnpzYBEkw5qXzFraNgPIAS'

# data = {'refreshtoken' : REFRESH_TOKEN}
# json = {'Content-Type' : 'application/json'}

def get_api_token(REFRESH_TOKEN):
    api_url = 'https://api.chartmetric.com/api/token'
    
    response = requests.post(url=api_url, data={'refreshtoken' : REFRESH_TOKEN}, 
                             json={'Content-Type' : 'application/json'})
    results = response.json()
    api_token = results['token']
    return api_token

def get_track_metadata(api_token, cm_track_id):
    #cm_track_id refers to the chartmetric track id associated with the song
    #returns a dictionary('id', 'name', 'isrc', 'image_url', 'duration_ms', 'composer_name', 
    #'artists', 'albums', 'tags', 'cm_audio_features', 'release_date', 'lastfm', 'cm_statistics')
    response = requests.get(url='https://api.chartmetric.com/api/track/{}'.format(cm_track_id),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}
                                )
    if response.status_code == 200:

        data = response.json()
        track = data['obj']
    else:
        pass
    return track

def get_chart_data(api_token, cm_track_id, chart_type, date):
    #refer to https://api.chartmetric.com/apidoc/#api-Track-getTrackCharts for allowed values for chart_type
    #date == YYYY-MM-DD
    #returns a list of dictionaries with chart data for each date
    response = requests.get(url='https://api.chartmetric.com/api/track/{}/{}/charts'.format(cm_track_id, chart_type),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'since': date}
                                )
    if response.status_code == 200:
        data = response.json()
        chart = data['obj']
        return chart['data']