import json
import argparse

from datetime import datetime


def get_arguments():
    all_args = argparse.ArgumentParser()

    all_args.add_argument("-i", "--Json", required=True,
                          help="Choose the JSON file with the comment data")
    all_args.add_argument("-v", "--Video", required=False,
                          help="OPTIONAL: Choose the video file")

    args = vars(all_args.parse_args())

    return args


def view_json_video(cli_args):
    with open(cli_args['Json']) as f:
        json_load = json.load(f)
    data = json_load['comments']

    video = cli_args['Video']

    return data, video


def create_html(data_comments, data_video):
    # Beginning of the html file
    with open('index.html', 'w') as index:
        index.write(f"""<!DOCTYPE html>
<html>
<head>
<title>CommentViewer</title>
<style type='text/css'>
body {{
    font-family: monospace;
    background-color: #181818;
    color: #FFFFFF;
}}
h1 {{
    text-align: center;
    font-size: 30px;
}}
video {{
    display: block;
    margin-left: auto;
    margin-right: auto;
}}
.authorThumbnail {{
    width: 35px;
    border-radius: 50%;
}}
.timeText {{
    color: #AAAAAA;
    font-size: 10px;
}}
.commentText {{
    font-size: 14px;
}}
</style>
</head>
<body>
<h1>Yamabiko</h1>
<h1>yt-dlp CommentViewer</h1>
<video width='720' height='480' controls>
<source src='{data_video}' type='video/mp4'>
</video>
""")

    # Loading all the comments
    for i in data_comments:
        with open('index.html', 'a') as index:
            index.write(f"""
<div class='comment'>
<hr>
<h3><img src={i['author_thumbnail']} class=authorThumbnail> {i['author']} <small class=timeText>{i['time_text']}</small></h3>
<p class=commentText>{i['text']}</p>
<p><small>Date commented: {datetime.fromtimestamp(i['timestamp']).strftime('%d-%m-%Y')}</small></p>
<p>👍 {i['like_count']}</p>
</div>
""")

    # Closing the html file
    with open('index.html', 'a') as index:
        index.write(f"""</body>
</html>""")


if __name__ == '__main__':
    arguments = get_arguments()
    comments, video_file = view_json_video(arguments)
    create_html(comments, video_file)
