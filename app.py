from flask import Flask, request, jsonify
from googleapiclient.discovery import build
import credentials

app = Flask(__name__)

API_KEY = credentials.YouTube_Data_API_v3_Key

def get_channel_name(channel_id):
    service = build('youtube', 'v3', developerKey=API_KEY)
    request = service.channels().list(id=channel_id, part='snippet')
    response = request.execute()
    return response['items'][0]['snippet']['title']

def get_channel_statistics(channel_id):
    service = build('youtube', 'v3', developerKey=API_KEY)
    request = service.channels().list(id=channel_id, part='statistics')
    response = request.execute()
    return response['items'][0]['statistics']

def get_videos(channel_id):
    service = build('youtube', 'v3', developerKey=API_KEY)
    request = service.search().list(channelId=channel_id, part='id', maxResults=50, order='date')
    response = request.execute()
    videos = response['items']
    return [video['id']['videoId'] for video in videos if video['id']['kind'] == 'youtube#video']

def get_video_statistics(video_id):
    service = build('youtube', 'v3', developerKey=API_KEY)
    request = service.videos().list(id=video_id, part='statistics')
    response = request.execute()
    return response['items'][0]['statistics']

@app.route('/channel_stats', methods=['POST'])
def channel_stats():
    data = request.get_json()
    channel_id = data['channel_id']
    if not channel_id:
        return jsonify({'error': 'Invalid YouTube channel ID'}), 400

    channel_name = get_channel_name(channel_id)
    videos = get_videos(channel_id)
    if not videos:
        return jsonify({'error': 'No videos found for this channel'}), 400

    total_views, total_likes, total_comments, video_count = 0, 0, 0, 0

    for video_id in videos:
        stats = get_video_statistics(video_id)
        total_views += int(stats.get('viewCount', 0))
        total_likes += int(stats.get('likeCount', 0))
        total_comments += int(stats.get('commentCount', 0))
        video_count += 1

    avg_views = total_views / video_count if video_count else 0
    avg_likes = total_likes / video_count if video_count else 0
    avg_comments = total_comments / video_count if video_count else 0

    return jsonify({
        'channel_name': channel_name,
        'average_views': avg_views,
        'average_likes': avg_likes,
        'average_comments': avg_comments
    })

if __name__ == '__main__':
    app.run(debug=True)