text=$(uname -os;date)
gp:
	git status --porcelain
	git add -A .
	git commit -am {{text}}
	git push