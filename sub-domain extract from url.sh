cat $1 | sed -e 's|^https\?://||' -e 's|/.*||' -e 's|:.*||' | sort -u | uniq -u
