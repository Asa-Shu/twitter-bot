import tweepy
import time
import pandas as pd

# Settings

# TwitterAPI
api_key = '******'
api_key_secret = '******'
access_token = '******'
access_token_secret = '******'

# Exception account
white_list = {'******', '******', '******'}

# CSV file
file_path = '******.csv'

# FF rate
rate = 1.5

# start number
start = 0

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

df = pd.read_csv(file_path)
selected_account_list = df[(df.フォロー数 / df.フォロワー数 > rate)
                           & (~df['スクリーン名'].isin(white_list))][['スクリーン名', '名前']]

selected_account_list['No'] = range(0, len(selected_account_list))

loop_count = 0
for selected_account in list(selected_account_list.itertuples())[start:]:
    screen_name = selected_account[1]
    name = selected_account[2]
    index = selected_account[3]
    print(index, screen_name, name)
    user = client.get_user(username=screen_name,
                           user_fields=['description', 'protected', 'name', 'username', 'public_metrics', 'profile_image_url'], user_auth=True)
    client.unfollow_user(target_user_id=user.data.id)
    loop_count += 1
    if loop_count % 399 == 0:
        time.sleep(24 * 60 * 60)
