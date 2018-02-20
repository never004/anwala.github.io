#!/bin/bash
#
# Fetch HTML for links (using given input), one link per line


usage() {
	echo >&2
	echo >&2 "Usage: $0 file"
}
warning() {
	echo >&2 '[*] Warning: script overwrites data in raw html, 
waiting 10 seconds before starting.'
	echo >&2
	sleep 10
}
fetch() {
	while read uri; do
		local hash=$(echo -n "$uri" | sha1sum | cut -d ' ' -f 1)
		local hash+=".html"
		curl "$uri" > data/raw_html/"$hash"
		if [[ "$?" != 0 ]]
		then
			echo >&2 '[*] Error downloading uri'
		else
			echo >&2 '[*] Done'
		fi
	done < "$FILE"
}

if [ $# != 1 ] ; then
	usage
	exit 1
else
	FILE=$1
	echo >&2
	echo >&2 "[*] Fetch HTML for links in file $FILE"
fi

warning
fetch

exit 0
