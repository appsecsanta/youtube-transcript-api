from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "YouTube Transcript API",
        "usage": "/transcript?video_id=VIDEO_ID"
    })

@app.route('/transcript')
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({"error": "video_id parameter is required"}), 400
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify({"transcript": transcript})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
