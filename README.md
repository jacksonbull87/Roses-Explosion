# Sounds of Summer 2020
## An Analytical Approach to Finding The Song of the Summer
<p align="center">
<img src="https://media.giphy.com/media/TKqXCyRwqf0DC/source.gif">
</p>

## Introduction

Summer is typically an exciting time for music fans; as the days get longer and the temperature 
starts to heat up, positive and lively new music releases provide the perfect soundtrack 
to BBQs, trips to the beach, roadtrips, blockparties, and other forms of real life escapism.
Using data from TikTok's weekly music charts, the goal of this project is to examine the most
popular songs as defined by the following KPIs:
- Longevity (Time Spent on Chart)
- Velocity (Biggest Change in Rank Over a 7-Day Period)
- Spotify Popularity (Biggest Increase in Popularity Score)
<p align="center">
<img src="https://media.giphy.com/media/1uBL7nzh9mxXO/source.gif" alt="Sublime's custom image"/>
</p>

## Technology
**Data Source:** [ChartMetric](https://api.chartmetric.com/apidoc/)

**Date Range:** 05/25/20-08/15/20

**Language:** Python

**Visualization:** [Tableau](https://public.tableau.com/views/MostPopularTikTokSongsSummer2020/MostViral?:language=en&:display_count=y&:origin=viz_share_link)



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

Once I extracted all the charts, I concatenated each dataframe along axis 0 to create one master dataframe:
    `master_df.to_csv('datasets/historic_ttwk.csv')`
Each row represents a chart position for a specific week, so there may be duplicate artists is an artists spend more than 
a week onthe charts.

I was able to fetch chart positions from the past 4 months:
- 1500 Chart Position
- 375 Unique Tracks
- 351 Unique Artists
![](/images/numberofsongsartists.png)

#### Feature Engineering
In addition to my primary goals of this project, I also want to analyize the distribution of tracks in terms
of genre and era. So using my api function `from cm_api import get_track_meta`, I grabbed the tags associated with each `cm_id`. 
Then using a dictionary object, I mapped each genre to its `cm_id`, engineering a new feature:

`ttwk_mstr['track_genre'] = ttwk_mstr['cm_id'].map(track_genre)`

Using one of Pandas' built-in datetime methods, I engineered a new feature for era:

`ttwk_mstr['era'] = ttwk_mstr['release_date'].dt.year`


**Dataset Features**
*Note: The features listed below does not represent all features in my master dataframe-these are just
the ones I ended up using for my analysis*

track_name | artist_name | cm_id| label | release_date | rank | add_date | velocity | peak_rank | peak_date | time_on_chart | track_genre|year
-----------|-------------|------|-------|--------------|------|----------|----------|-----------|-----------|---------------|------------|----


### ChartMetric API - Spotify Popularity Data For Artists
In order to show historic trends in popularity score for our TikTok artists, I created another
API helper function to retreive data over the past 12 months, `begin_date = 2019-09-02`, but only
for artists who had a peak rank between 1 and 10.
    `from cm_api import get_fan_metrics`

- Parameters: `api_token`, cm_artist_id, data_source, begin_date, stat_metric
    - For information on value types accepted, see [ChartMetric's Api Documentation](https://api.chartmetric.com/apidoc/#api-Artist-GetArtistorStat)

**Dataset Features**


timestamp | artist | cm_artist_id| popularity
----------|--------|-------------|-----------|


[Data Located Here](https://github.com/jacksonbull87/Roses-Explosion/tree/master/datasets) -->
## Visualizations - Key Performance Metrics
### Longevity (Time On Chart)
The visualization below reveals the top trending TikTok tracks sorted in descending order of time most spent

![](/images/time_spent.png)
[Link To Interactive Vizualization](https://public.tableau.com/views/MostPopularTikTokSongsSummer2020/TimeOnChartTop10?:language=en&:display_count=y&:origin=viz_share_link)


            

