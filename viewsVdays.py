import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def views_v_days_scatter(filepath):
  raw_us = pd.read_csv(filepath)
  raw_us.columns

  df_us = raw_us[['video_id', 'trending_date', 'title', 'channel_title', 'category_id','publish_time', 'tags', 'views', 'likes', 'dislikes']]
  df_us.sort_values(['video_id','views'])

  df_counts = df_us.groupby(['video_id','views'])


  df_counts = df_us.set_index(['video_id']).groupby('video_id').count()
  df_counts.reset_index(inplace = True)
  df_counts_2 = df_us.set_index(['video_id']).groupby('video_id').sum()
  df_counts_2.reset_index(inplace = True)

  df_id_views = pd.DataFrame([df_counts['video_id'],df_counts_2['views']]).T
  df_id_views.columns = ['video_id','views']
  df_id_views.head(10)

  df_id_counts = pd.DataFrame([df_counts['video_id'],
                              pd.to_numeric(df_counts['views']),
                              pd.to_numeric(df_id_views['views'])
                              ]).T

  df_id_counts.columns = ['video_id','days_trending','views']
  df_id_counts['views'] = pd.to_numeric(df_id_counts['views'])
  df_id_counts['days_trending'] = pd.to_numeric(df_id_counts['days_trending'])

  ax = df_id_counts.plot(kind = 'scatter', 
                    x = 'days_trending', 
                    y = 'views', 
                    logy = True,
                      figsize = (15,10))
  ax.set_xlabel('Days Trending')
  ax.set_ylabel('Views (Log)')
  ax.set_title('Days trending vs Views')
  plt.savefig('YouTube_Views and Days Trending_US.jpg')
  plt.show()

if __name__ == '__main__':
  views_v_days_scatter('data/youtube-new/CAvideos.csv')