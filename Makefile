pdf:
	@read -p "Tex filename (wihtout .tex):" tex; \
	pdflatex $$tex && \
	makeindex $$tex.nlo -s latex_einstellungen/abkuezungen/nomencl.ist -o $$tex.nls && \
	makeglossaries $$tex && \
	bibtex $$tex.aux && \
	pdflatex $$tex

open:
	@read -p "Tex filename (wihtout .tex):" tex; \
		chromium $$tex.pdf
