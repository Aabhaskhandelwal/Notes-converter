from my_agent.agent import notes_agent
from tools.youtube import get_transcript

video_id = "VIDEO_ID_HERE"

transcript = get_transcript(video_id)

response = notes_agent.run(
    input=f"Create structured notes from this transcript:\n{transcript}"
)

print(response.output)
