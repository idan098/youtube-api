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
    audio_stream_url = audio_stream.url
    media = vlc.Media(audio_stream_url)
    player.set_media(media)
    player.play()
    player.get_instance()


def main():
    player = vlc.MediaPlayer()
    playlist = []

    for phrase in LiveSpeech():
        phrase = str(phrase)
        print(phrase)

        if "playist" in phrase:
            pass

        elif "play" in phrase:
            try:
                phrase = phrase.split(" ", 1)[1]
            except IndexError:
                print("only one word")
            print(f"playing {phrase}")
            video_url = search_video(phrase)
            stream_audio(video_url, player)
            while not player.is_playing():
                time.sleep(0.1)

        elif player.is_playing() and "stop" in phrase:
            player.set_pause(1)

        elif "resume" in phrase and not player.is_playing():
            player.set_pause(0)
    return


if __name__ == '__main__':
    main()
