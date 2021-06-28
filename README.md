#### Python package for epidemiological models relevant to modeling Covid-19 infections

**Pre-requisite**: Python 3.6 and above

To run the following models, execute (from the top-level covimath directory):
- **SIS** model: `python3 -m covimath.models.sis N=1000 lambda=0.05 mu=0.15 gamma=0.1 I0=1 tau=30`	
- **SIR** model: `python3 -m covimath.models.sir N=1000 I0=1 R0=0 beta=0.2 gamma=0.1 tau=150`
-  **SEIR** model: `python3 -m covimath.models.seir N=1000 E0=1 I0=1 R0=0 beta=1.38 sigma=0.19 gamma=0.34 tau=150`
- **SEIRD** model: `python3 -m covimath.models.seird N=1000 E0=1 I0=1 R0=0 D0=0 beta=1.38 sigma=0.19 gamma=0.34 mu=0.03 tau=150` 

To run the tests, from the top-level covimath directory, run:
`pytest`

A simple method to estimate beta for SIR model has been provided.

Example code can be found in a [gist](https://gist.github.com/techyugadi/1217c16c37d889b4d2204dff067388b2).

**Installation**: To install this package, run: `pip3 install covimath`
