# __FILE SUMMARY__: This file is meant to shorten the data. Each dataset (both bot and human) has
# 50 usernames with around 110,000 tweets (give or take a couple thousand) in total, with around 3200 
# (give or take a couple hundred) tweets per username. This will take the first 200 tweets of each username 
# username and put it into a new file giving us 10,000 tweets in total. 
#
# __NOTE__: You can change the amount of tweets to transfer to the new file. For example, where it says 
# ".head(200).reset_index(drop=True)" if changed to --> ".head(10).reset_index(drop=True)" 
# each of the 50 usernames will have only 10 tweets giving us 500 tweets in total

import pandas as pd

# Load the dataset and replace "your_input_file.csv" with the filename --> "all_50_bot_tweets.csv"
df = pd.read_csv("your_input_file.csv")

# In both datasets, the username column is called Twitter_User_Name
# this keeps only the first 200 tweets, WHICH you can change but see __NOTE__ before doing so.
df_limited = df.groupby("Twitter_User_Name").head(200).reset_index(drop=True)

# Confirms the new stats. This is for error purposes
print("Finished! Unique bot usernames:", df_limited["Twitter_User_Name"].nunique())
print("Finished! Total rows in output:", len(df_limited))

# The new shortened dataset will save to a new csv file.
# You can change the name to whatever but be consistant, the current 
# name of the new file is "bots_limited_200_per_user.csv"
df_limited.to_csv("bots_limited_200_per_user.csv", index=False)
