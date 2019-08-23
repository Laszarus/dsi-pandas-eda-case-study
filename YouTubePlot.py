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
df_id_views.head(10)
df_id_views['views']

df_counts = df_us.set_index(['video_id']).groupby('video_id').count()
df_counts.reset_index(inplace = True)

# Merge columns needed all together
df_trend_views = pd.DataFrame([df_counts['video_id'],df_counts['views'],df_id_views['views']]).T
df_trend_views.columns = ['video_id','days_trending','views']
df_trend_views.head()

if __name__ == '__main__':
    print(df_trend_views.head())