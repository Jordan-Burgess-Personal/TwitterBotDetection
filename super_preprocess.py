import pandas as pd

# Load your full dataset
df = pd.read_csv("your_input_file.csv")  # Replace with your filename

# For each Twitter_User_Name, keep only the first 200 tweets
df_limited = df.groupby("Twitter_User_Name").head(200).reset_index(drop=True)

# Confirm stats
print(":white_check_mark: Unique bot usernames:", df_limited["Twitter_User_Name"].nunique())
print(":white_check_mark: Total rows in output:", len(df_limited))

# Save to CSV
df_limited.to_csv("bots_limited_200_per_user.csv", index=False)
