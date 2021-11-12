# spotify-playlist-to-mp3
## instructions

1. go to your playlist in spotify web app with dev tools open
2. open all "tracks?offset=..." requests and export items in response to global variable
3. in console (replace X with index):


	```tempX.map(song => song.track.name + song.track.artists.map(artist => ` ${artist.name}`))```
	
	
4. paste the result in a json in the following format:


	```
	{
		"songs": <pasted songs>
	}
	```
5. make sure python and ffmpeg are installed
6. pip install and run specifying input json path and output songs dir, for example

``` python main.py --output_dir=C:/path/to/songs/dir/songs --input_path=C:/path\to\songs\input.json ```
