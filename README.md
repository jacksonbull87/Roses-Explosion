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
### ChartMetric API
    With the help of ChartMetric's API, I was able to gather data on the top 100 weekly tracks on TikTok 
    from May 2nd to August 15th.
    In order to make api calls to CM's server, I'll need an api token 
    which I can get by importing it from my config file: 
        `from cm_api import token`
    For security purposes, I locked away the refresh token in a config file (on gitignore).
        `refresh_token = token['refresh_token'] ` 
    Now that I haven a `refresh_token`, I can use the following helper functions to
    <ol>
    <li>Get my temporary api_token `from cm_api import get_api_token`</li>
    <li>Get TikTok chart data `from cm_api import get_tiktok_chart_data`</li>
    I was able to fetch chart positions from the past 4 months, 
    which included 1500 chart positions, 375 unique tracks, 351 unique artists.
![](/images/numberofsongsartists.png)
