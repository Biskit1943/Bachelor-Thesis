pdf:
	@read -p "Tex filename (wihtout .tex):" tex; \
	pdflatex $$tex \
	makeindex $$tex.nlo -s latex_einstellungen/abkuerzungen/nomencl.ist -o $$tex.nls \
	makeglossaries $$tex \
	pdflatex $$tex
