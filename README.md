# Epithet Generator

Create a Flask API to serve random epithets from the [Shakespeare Insult Kit](http://www.pangloss.com/seidel/shake_rule.html).
Each sprint is an assignment with its own deliverables. Please create a pull request to the appropriate branch to submit
assignments. 

## Instructions
Sprint|Description|Commit
---|---|---|
[a](https://github.com/KenzieAcademy/backend-epithet-generator/blob/master/instructions/sprint_a.md)|minimal flask applications|
| |larger applications|
| |unit testing|
| |integration testing|
| |design patterns|

## Important Information
Sprint|Note
---|---|
c|I've added integration testing in `tests.py` using the Flask-Testing extension.
c|I've added an endpoint that generates a random quantity of epithets in `app.py`.
c|You'll notice that `initialize.py` has replaced `__init__.py`. This is a workaround necessary to bypass import issues I was having when running integration tests.

## Expected Payload
Endpoint|Payload
---|---|
/|{"epithet": \<str\>}
/epithets/\<quantity\>|{"epithets": [\<str\>*\<quantity\>] }
/epithets/random|{"random_epithets": [\<random amount of epithets\>]}
/vocabulary|{"vocabulary": {Column 1: [\<values\>],Column 2: [\<values\>], Column 3: [\<values\>]}}



