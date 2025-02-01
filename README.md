# RelEvent

The project contains the code for the Master thesis on Event Sequence Visualization titled ``RelEvent, A Visualization Tool for Relationships in Multivariate Heterogeneous Event Sequence``.



The project is created using:
- Python 3.11.6
- Flask 3.0.3
- Werkzeug 3.0.3
- npm 10.8.1

See `requirements.txt`, `package.json` and `documentation/venv packages.txt` for more details.

The dataset is RealityMining by N. Eagle, A. Pentland, and D. Lazer (2009), "Inferring Social Network Structure using Mobile Phone Data", Proceedings of the National Academy of Sciences, 106(36), pp. 15274-15278. The exact preprocessing steps can be found in a seperate [repository](https://github.com/Rianne5/PreprocessingRelEvent).

Create new environment with Python 3.11.6 and install ``requirements.txt``
<!-- Create environment when choosing python interpreter in Visual Studio Code or run ``python -m venv /path/to/new/virtual/environment`` or  conda create -n name_env python 3.11.6` and `conda activate name_env`-->
<!-- pip install -r requirements.txt -->

<!-- Activate environment, for example with ```.venv\Scripts\activate```   -->
<!-- or .venv\Scripts\activate.bat -->
<!-- and ```deactivate``` to remove virtual environment. -->

If requirements are not yet installed use:
`pip install -r requirements.txt`
and 
`npm install`



<!-- Additional installations.
`npm install d3`
`npm install @types/d3`
`npm i react` -->
<!-- `npm i neo4j-driver` -->
<!-- `npm install crossfilter2`  -->
<!-- `npm i d3@5.16.0`
crossfilter requirement for crossWidget -->


To run dashboard run commands:

```
python flask/app.py
```
```
npm run dev
```


With the data present it will result in a visualization tool like:

![RelEvent visualization tool](<documentation/RelEvent visualization tool.png>)

Many thanks to [D3.js graph gallery](https://d3-graph-gallery.com/index.html) and [Learn Svelte dev](https://learn.svelte.dev/tutorial/welcome-to-svelte)

For more information on the data see:
https://www.jeremykun.com/2014/01/21/realitymining-a-case-study-in-the-woes-of-data-processing/



Note, if no data is present the visualization will remain empty and return missing data errors.

![Error caused by missing data](<documentation/Data undefined.png>)


