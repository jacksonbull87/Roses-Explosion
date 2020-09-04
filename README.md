# How Does TikTok Affect Social Media Growth In Emerging Artists?
<p align="center">
<img src="https://media.giphy.com/media/l1J3orPHZBfwTIOZy/source.gif">
</p>

## Introduction

Despite privacy and national security concerns that have been in the headlnes lately, TikTok
has been a significant driving force behind many emerging artists. The purpose of this project is
to analyze the impact that the viral, hit-making app has on an artist's social media following.
<p align="center">
<img src="https://media.giphy.com/media/xUPN3lFweTO9jnXgCk/source.gif" alt="Sublime's custom image"/>
</p>

## Data Collection
### ChartMetric API - TikTok Weekly Chart Data
With the help of ChartMetric's API, I was able to gather data on the top 100 weekly tracks on TikTok 
from May 2nd to August 15th.
In order to make api calls to CM's server, I'll need an api token 
which I can get by importing it from my config file: 
        `from cm_api import token`.
For security purposes, I locked away the refresh token in a config file (on gitignore).
        `refresh_token = token['refresh_token'] `-
Now that I have a `refresh_token`, I can use the following helper functions:
1. Get my temporary api_token `from cm_api import get_api_token`
    - Parameters: `refresh_token`

2. Get TikTok chart data `from cm_api import get_tiktok_chart_data`
    - Parameters: api_token, chart_type, date, interval
        - For information on value types accepted, see [ChartMetric's Api Documentation](https://api.chartmetric.com/apidoc/#api-Charts-GetTiktokTracksChart)

I was able to fetch chart positions from the past 4 months:
- 1500 Chart Position
- 375 Unique Tracks
- 351 Unique Artists
![](/images/numberofsongsartists.png)

[Data Located Here](https://github.com/jacksonbull87/Roses-Explosion/tree/master/datasets)
### ChartMetric API - Spotify Popularity Metrics
`from cm_api import get_fan_metrics`
- Parameters: `api_token`, cm_artist_id, data_source, begin_date, stat_metric
    - For information on value types accepted, see [ChartMetric's Api Documentation](https://api.chartmetric.com/apidoc/#api-Artist-GetArtistorStat)

[Data Located Here](https://github.com/jacksonbull87/Roses-Explosion/tree/master/datasets)
## EDA
<div class='tableauPlaceholder' id='viz1599179803699' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Mo&#47;MostPopularTikTokSongsSummer2020&#47;TimeOnChartTop10&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='MostPopularTikTokSongsSummer2020&#47;TimeOnChartTop10' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Mo&#47;MostPopularTikTokSongsSummer2020&#47;TimeOnChartTop10&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1599179803699');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

