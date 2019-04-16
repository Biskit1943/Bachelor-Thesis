open:
	@read -p "Tex filename (wihtout .tex):" tex; \
	chromium $$tex.pdf

clean:
	rm -f bachelor.{log,aux,dvi,lof,lot,bit,idx,glo,bbl,bcf,ilg,toc,ind,out,blg,fdb_latexmk,fls,glg,gls,glsdefs,ist,lol,nlo,nls}
	rm -f expose.{log,aux,dvi,lof,lot,bit,idx,glo,bbl,bcf,ilg,toc,ind,out,blg,fdb_latexmk,fls,glg,gls,glsdefs,ist,lol,nlo,nls}

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
