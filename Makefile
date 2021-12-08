
gp:
	git status
	git add -A .
	text=$(uname -os;date);git commit -m "$text";git push