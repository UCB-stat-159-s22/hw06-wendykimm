env:
	mamba env create -f environment.yml -p ~/envs/ligo
	bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "IPython - ligo"'
    
html:
	jupyter-book build .
    
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html && python -m http.server

clean:
	rm -r figurs/
	rm -r audio/     
	mkdir figurs
	mkdir audio

    
all:
	jupyter execute index.ipynb
