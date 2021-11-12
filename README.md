# spotify-playlist-to-mp3
## instructions

1. go to your playlist in spotify web app with dev tools open
2. open all "tracks?offset=..." requests and export items in response to global variable
3. in console (replace X with index):


	tempX.map(song => song.track.name + song.track.artists.map(artist => ` ${artist.name}`))
	
	
4. paste the result in a json in the following format:
	{
		"songs": <pasted songs>
	}
5. make sure ffmpeg is installed, pip install and run
