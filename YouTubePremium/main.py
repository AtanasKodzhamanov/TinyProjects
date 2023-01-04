from pytube import YouTube
import os


# Set output folder to be default where the script is located as a default
output_folder = os.path.dirname(os.path.abspath(__file__))

print("Files will be stored here: " + output_folder)


# Ask the user for a list of URLs
urls = input("Enter a list of YouTube URLs, separated by commas: ")

# Split the list of URLs into individual URLs
url_list = urls.split(', ')

# Define a callback function that will be called with the download progress
def progress_function(stream, chunk, bytes_remaining):
  # Calculate the percentage of the download that is complete
  percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize

  # Print the percentage to the console
  print(f"{percent:.0f}% complete")

# Create an empty list to store the URLs of successfully downloaded videos
downloaded_videos = []

# Loop through the list of URLs and download each video
for url in url_list:
    
  try:
    # Create a YouTube object with the URL of the video
    video = YouTube(url).streams.filter(resolution="1080p").first()
    video.download()
    # Add the URL to the list of downloaded videos
    downloaded_videos.append(url)
  except:
    # If there is an error, print a message and continue to the next URL
    print(f"Error downloading {url}")
    continue

# Print a list of successfully downloaded videos
print("The following videos were downloaded:")
print(downloaded_videos)