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

clean:
	@read -p "Tex filename (wihtout .tex):" tex; \
	rm -f $$tex.{log,aux,dvi,lof,lot,bit,idx,glo,bbl,bcf,ilg,toc,ind,out,blg,fdb_latexmk,fls}

ba:
	pdflatex bachelor && \
	makeindex bachelor.nlo -s latex_einstellungen/abkuezungen/nomencl.ist -o bachelor.nls && \
	makeglossaries bachelor && \
	biber bachelor && \
	pdflatex bachelor

expose:
	pdflatex expose && \
	makeindex expose.nlo -s latex_einstellungen/abkuezungen/nomencl.ist -o expose.nls && \
	makeglossaries expose && \
	bibtex expose.aux && \
	pdflatex expose
