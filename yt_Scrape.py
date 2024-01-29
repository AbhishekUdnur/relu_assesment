from googleapiclient.discovery import build
from datetime import datetime, timedelta

def list_of_dates(start_date,end_date):

    date_list = []
    current_date = start_date

    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return date_list

def videos_by_date(youtube, channel_id, date):
    
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        publishedAfter=f"{date}T00:00:00Z",
        publishedBefore=f"{date}T23:59:59Z",
        type="video",
        maxResults=100 
    )

    response = request.execute()
    # print(response)

    video_ids = [item['id']['videoId'] for item in response['items']]
    # print(video_ids)
        
    return video_ids

api_key = 'AIzaSyC6EoxxsbRR47ui3VUDBaYAsSabotAJFMY'
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = 'UCq-Fj5jknLsUf-MWSy4_brA'  

start_date = '2023-05-22'
end_date  = '2023-08-08'

start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.strptime(end_date, '%Y-%m-%d')

ls = list_of_dates(start_date,end_date)

date_video = {}

for i in ls:
    date_video[i] = videos_by_date(youtube, channel_id, i)

actual_posted_dates = date_video.keys()
# print(actual_posted_dates)

video_ids = date_video.values()
ls = []
for  i in video_ids:
    ls+=i
ls = [i.lower() for i in ls]

output = {}

for i in ls:
    for j in i:

        if j in output:
            output[j] +=1
        else:
            output[j] = 1

val = output.values()
mx = max(val)

for key,value in output.items():
    if output[key] == mx:
        print(f"key:{key}  value:{value}")

