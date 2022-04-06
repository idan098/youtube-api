import time
import vlc
import pafy
from youtubesearchpython import VideosSearch
from pocketsphinx import LiveSpeech


def query_user_for_video():
    video_name = input("Please type the video name:\r\n")
    return video_name


def voice_query_user_for_video():
    print("what song would you like to play?")
    for phrase in LiveSpeech():
        phrase = str(phrase)
        print(phrase)
        return phrase


def search_video(video_name):
    videos_search = VideosSearch(video_name, limit=1)
    search_result = videos_search.result().get("result")[0]
    video_url = search_result.get("link")
    print(video_url)
    return video_url


def stream_audio(file_name, player):
    stream = pafy.new(file_name)
    audio_stream = stream.getbestaudio()
    print(audio_stream)
    audio_stream_url = audio_stream.url
    print(audio_stream_url)
    media = vlc.Media(audio_stream_url)
    player.set_media(media)
    player.play()
    player.get_instance()


def main():
    player = vlc.MediaPlayer()

    for phrase in LiveSpeech():
        phrase = str(phrase)
        print(phrase)
        if "play" in phrase:
            phrase = phrase.split(" ", 1)[1]
            print(f"playing {phrase}")
            video_url = search_video(phrase)
            stream_audio(video_url, player)
            while not player.is_playing():
                time.sleep(0.1)

        elif player.is_playing() and "stop" in phrase:
            player.pause()

        elif ""

    if player.is_playing():
        time.sleep(1)

    # video_name = voice_query_user_for_video()
    # video_url = search_video(video_name)
    # stream_audio(video_url)

    # while True:
    #     pass
    return


if __name__ == '__main__':
    main()
