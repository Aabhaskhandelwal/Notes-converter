from my_agent.agent import youtube_notes_agent
from my_agent.tools.youtube import fetch_transcript


def youtube_to_notes(video_id: str):
    transcript = fetch_transcript(video_id)

    response = youtube_notes_agent.run(
        input=f"Generate study notes from this transcript:\n{transcript}"
    )

    return response.output


if __name__ == "__main__":
    video_id = "dQw4w9WgXcQ"
    notes = youtube_to_notes(video_id)
    print(notes)
