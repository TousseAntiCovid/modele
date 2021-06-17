mp3towav(){
	[[ $# -eq 0 ]] && { echo "mp3wav mp3file"; exit 1; }
	for i in "$@"
	do
		# create .wav file name
		local out="${i%/*}.wav"
		[[ -f "$i" ]] && { echo -n "Processing ${i}..."; mpg123 -w "${out}" "$i" &>/dev/null  && echo "done." || echo "failed."; }
	done	
}
