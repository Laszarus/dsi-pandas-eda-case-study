import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_us = pd.read_csv('data/youtube-new/USvideos.csv')
raw_us.columns

df_us = raw_us[['video_id', 'trending_date', 'title', 'channel_title', 'category_id','publish_time', 'tags', 'views', 'likes', 'dislikes']]
df_us.info

df_us.sort_values(['video_id','views'])
df_counts = df_us.groupby(['video_id','views'])

df_counts = df_us.set_index(['video_id']).groupby('video_id').sum()
df_counts.reset_index(inplace = True)

df_id_views = pd.DataFrame([df_counts['video_id'],df_counts['views']]).T
df_id_views.columns = ['video_id','views']

df_id_counts = pd.DataFrame([df_counts['video_id'],
                             pd.to_numeric(df_counts['views']),
                             pd.to_numeric(df_id_views['views'])
                            ]).T
df_id_counts.columns = ['video_id','days_trending','views']
# df_id_counts = pd.DataFrame([df_id_counts['video_id'],
#                              pd.to_numeric(df_id_counts['days_trending']),
#                              pd.to_numeric(df_id_counts['views'])
#                             ])
df_id_counts['views'] = pd.to_numeric(df_id_counts['views'])
df_id_counts['days_trending'] = pd.to_numeric(df_id_counts['days_trending'])

if __name__ == '__main__':
    print(df_id_counts.head())