## Pandas-EDA-Case-Study

# Global Youtube Trends
There were files for stats on US, Russia, Mexico, Korea, Japan, India, Great Britain, Denmark, and Canada. In the columns for each file, you could see the video ID, dates the video trended, the title, when it was published, and engagement metrics such as likes, views, likes, dislikes, comments, etc.

## Trending Videos across Multiple Countries

We took the Video ID column across data for the US, Great Britain, France, Germany, and Canada. We wanted to find which videos trended in multiple countries. Specifically, which countries shared the most common trending videos. 



The Video ID datatype was text and luckily, no data was missing for our countries. Each ID appeared on a date when the video trended, so some Video IDs appeared on many different rows. We developed lists for each country showing its Video ID, Category ID and count of how many times each Category ID trended. We did more with this is the next section.

US:
![alt text](/images/list.png)

Canada:
![alt text](/images/ca_head.png)


We looped through this list and inner joined the lists with each other finding the amount of videos that trended in multiple countries. The result was a matrix with columns and rows representing the countries.

![alt text](/images/matrix.png)

 The value in each cell represented the amount a videos the trended in that cell’s column country and that cell’s row country. The result can be seen in a heat map below. As you can see the pairs with the most over lap were [Germany, France], [Canada, France], and [Canada, Germany]. 

![alt text](/images/heatmap.png)


Interpretation:
![alt text](/images/us_trends.png)
![alt text](/images/ca_trends.png)




## Most Popular Categories in US

To explore the most popular categories of YouTube videos in the US, we grouped the dataset on title to remove duplicates, summing the count category IDs for each video. We then grouped by category ID to get a final count of how many trending instances were seen from each category over the time period this dataset covers.
 
With more time, we could repeat this process for each country, and also with a combined world dataset, allowing us to compare the video category preferences of each country versus those of the world as a whole. 

![alt text](/images/category_legend.jpg)
![alt text](/images/top_US_video_categories.jpg)

## Days Trending vs Views

Although it’s apparent a video trending for a longer amount of time will get more views, we were curious about comparing this trend between countries. The videos trended over different time lengths, so we summed the total views and compared it against the total number of days the video trended. Here is a scatter plot showing this information for US:
![alt text](/images/YouTube_Views_and_Days_Trending_US.jpg)

When we first went to plot anything, we quickly realized that we had to redefine the data types from ‘objects’ to ‘numeric’. Once we updated the views, we identified an outlier that made the views so large and varied. We decided to group the views by log10. 
