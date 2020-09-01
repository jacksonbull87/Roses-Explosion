
import requests
import re


REFRESH_TOKEN = 'ZT9RCsKBcwHaLCPulKmDFXWPxpwfoYtAdYunn5qgeVWnpzYBEkw5qXzFraNgPIAS'


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

def get_tiktok_chart_data(api_token, chart_type, date, interval):
    #for apitoken import get_import_token
    #for chart_type, accepted values include 'tracks', 'videos', 'users'
    #date == YYYY-MM-DD
    #for interval, accepted values include 'daily', 'weekly'
    #returns a list of song metadata
    response = requests.get(url='https://api.chartmetric.com/api/charts/tiktok/{}'.format(chart_type),
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'date': date, 'interval': interval}
                                )
    if response.status_code == 200:
        data = response.json()
        chart = data['obj']
        return chart['data']

def get_artist_id(api_token, q, search_type):
    #return tuple (artist name, artist cm id)
    response = requests.get(url='https://api.chartmetric.com/api/search',
                            headers={'Authorization' : 'Bearer {}'.format(api_token)}, params={'q': q, 'type': search_type}
                                )
    if response.status_code == 200:
        data = response.json()
        cm_id = []
        try:
            chart = data['obj']
            for artist in chart['artists']:
                if re.fullmatch(q.lower(), artist['name'].lower()):
                    # print(artist['name'])
                    # print('Chartmetric ID: ',artist['id'])
                    return artist['id']
                else:
                    continue
            
        except TypeError:
            return "None"
    else:
        print(response.status_code)
        print(response.text)
