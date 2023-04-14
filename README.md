# **virus_evo**

### *Current Representations :*

```
INITIALIZATION

Virus :
% initial structure of the virus and vaccine

Vir : [ [0,0,0,0,0,0,0,0]x8 , [Lethal Point : index] , [Properties] , [Mut_Val] ]
Vac : [ 0,0,0,0,0,0,0,0 ] (global var.vaccine)

    Lethal Points :
    % initialize the lethal points of the virus

        Choose x = randint ( 1 , 3 )
        Choose x randint ( 0 , 7 ) to be index non repeating
        Append indexes to Var : Lethal Point Array

    Properties :
    % store virus related information
        index 0:
            Threatened:
            % indicates whether or not a virus is threatened by vaccine
            Append 0 to Var : Properties Array

        index 1:
            Fitness Value:
            % store and update the fitness of a virus with each generation
            Append 0 to Var : Properties Array

        index 2:
            Virility Value:
            % store and update the virality of a virus based on mutations
            Append 0 to Var : Properties Array


    Mutation Value :
    % store virus mutation values
        % stores the value of a mutation so that it can be reversed
        index 0->(virus length * virus node length)

        initialize array of 0's size => (virus length * virus node length)

```

```
VIRUS
% get virus threat binary
def get_virus_threat (virus):
    return value of virus threat parameter

% set virus threat binary
def set_virus_threat (virus, value):
    set the virus threat parameter to value

% get virus lp as an array
def get_virus_lp (virus):
    for each value in lp array:
        return array associated with lp index

% threaten a virus
def virus_threat_check (virus):
    for each lethal point in a virus:
        check if any match the VACCINE

    if lp match vaccine:
        if the virus was already threatened:
            kill the virus
        otherwise threaten the virus
    otherwise remove / reset threat

% set a virus to empty set
def virus_null(virus):
    virus = []

% clean a virus_pop of all empty sets
def virus_pop_clean (virus_pop):

```

```
VACCINE
% determine ways to threaten a virus

% set vaccine value
def set_vaccine (vaccine) :
    set the global var vaccine to be the new vaccine

% method 1: avg of all LP array columns
def avg_lp_virus_string (lethal points)
    for each column in a virus LP array:
        for each LP array in LP arrays:
            determine the most common value in a column
            append to avg array
        return average

```

```
MUTATION
*implementation*

```

```
SELECTION

Parent Selection
*implementation*
```

```
FUNCTIONS


```

### EA ALG STRUCTURE
```
INITIALIZE
virus_pop = initialization.initialize_virus_population()
var.vaccine = initialization.initialize_vaccine()

FITNESS
fit_scores = fitness.temp(virus_pop)

GENERATIONAL LOOP


```

### *Functions TODO :*
The following are functions that are to be done:
```
Virus:
- [] Translate Tree <-> Translate String
- [] Initialize Virus String
- [] Alter Lethal Points of Tree / String
- [] Alter Genetic Code of Virus Nodes
- [x] Virus Threatened Property
- [] Virus Mutate Lethal Points
- []

Vaccine:
- [] Initialize String
- [] Alter Vaccine Genetic Code
- [] Vaccine Fitness  
- [] Collect all Lethal Nodes
```
## Timeline

```
Tasks:
Lavi    : init vacine (x) / threat (x)/ avg LP string (x)
Cyril   : mutation / set + get helper for LP (x)
Priyank : init parent selection
```
