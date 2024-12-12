from pytube import YouTube

def download_video(url, directory, filename):
    try:
        yt = YouTube(url)
        yt.streams.first().download(directory, filename)
    except Exception as e:
        print(f"An error occurred: {e}")

url = input("Enter the YouTube video URL: ")
directory = input("Enter the directory to save the video (default: current directory): ")
filename = input("Enter the filename to save the video (default: video title): ")

download_video(url, directory, filename)