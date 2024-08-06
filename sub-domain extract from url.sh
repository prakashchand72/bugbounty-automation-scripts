cat $1 | sed -e 's|^https\?://||' -e 's|/.*||' | sort -u | uniq -u
