## Final Project: Herd Immunity Simulation.

As discussed in class, we're going to be creating a basic simulation of herd immunity
by modeling how a virus moves through a population where some (but not all) of a population
is vaccinated against this virus.  

This is just a rough README for now, to help unblock you so that you can get started
started on the project.  I'll update this with more detail in the near future.

### Getting Started

To get started on this project, fork this repo and then clone the directory from *your own*
fork.  You'll find instructions for what you need to do marked within the files themselves.
Anything  that you explicitly need to code should be marked with a comment that starts with `#TODO`.  

### Running the program

The program is designed to be run from the command line.  You can do this by running
`python3 simulation.py` followed by the command line arguments in the following order,
separated by spaces:
 {population size} {vacc_percentage} {virus_name} {mortality_rate} {basic_repro_num} {optional: number of initially infected people (default is 1)}

 Let's look at an example:

 Population Size: 100,000
 Vacc_percentage: 90%
 Virus Name: Ebola
 Mortality Rate:  70%
 Basic Reproduction Number: 25%
 Initial Infected: 10

 Then I would type `python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10` in the terminal.

### Basic Structure of the program

The program consists of 3 Classes:  Simulation, Logger, and Person.  

* Simulation: Highest level of abstraction. The main class that runs the entire simulation.
* Person: Represents the people that make up the population that the virus is spreading through.
* Logger: A helper class for logging all events that happen in the simulation.

*NOTE*: Although our original in-class discussion for the project noted that we should
also have an Abstract Superclass called Virus and corresponding subclasses for each actual
virus we wanted to simulate, after playing around with the simulation I decided that this wasn't the best approach. Since viruses are static in this simulation and all we really care about is the name of the virus, the mortality rate of the virus, and the rate at which the virus spreads through a population ("Basic Reproduction Number"), I've decided it makes more sense to just store that data as attributes at the Simulation level.

When you run `simulation.py` (with the corresponding command-line arguments necessary for a simulation), a simulation object is created.  This simulation object then calls the `.run()` method.  This method should continually check if the simulation needs to run another step using a helper method contained in the class, and then call `.time_step()` if the simulation has not ended yet.  Within the `time_step()` method, you'll find all the logic necessary for actually simulating everything--that is, once you write it.  As is, the file just contains a bunch of method stubs, as well as numerous comments for explaining what you need to do to get everything working.  

### Some Notes For Being Successful On This Project

First, take a look at each of the files.  Get a feel for the methods and attributes in each.  Feel overwhelmed? Don't panic.  Instead, get out a piece of paper or a whiteboard and try to diagram needs to happen and when using each of the objects and method names.

*_If you don't understand something, ask for help!_*

I'm available on slack all week.  Ask your classmates for clarification/help/code reviews as needed.  Just make sure that your work is still your own!

*Found a bug or a problem? No Problem! Let me know!*

 The template code was written in a cottage on the coast of Ireland with spotty power during the strongest hurricane Ireland has seen in 61 years, so there are probably some bugs in the template code. If you think something doesn't make sense, double check with your classmates and/or me.  If you feel the need to modify the template code to make it work another way, that's totally fine! The template code is there to help you, but it isn't a requirement that you use any/all of it.  

*WRITE TESTS!*

This is a big project.  There's no way that all the code you write is going to work the first time.  Also, see the paragraph above about Mike coding all of this on a mountain during a 50 year storm while fighting off mountain lions with only a soup-ladle to defend himself.  Starting by thinking about your test cases and aiming for good test coverage is a great way to vaccinate yourself against any pre-existing bugs in the template.

*Bugs in the template code? But Mike, you're always telling us to start by writing tests for our code! Are you really trying to tell us that you are giving us template code that you haven't tested yourself yet? Isn't that a bit hypocritical?!*

uh, good point.  But, you see, uh....oops wifi is going out and THERES ANOTHER HURRICANE IT CAME OUT OF NOWHERE UH OH I GOTTA GO NO TIME TO ANSWER THIS QUESTIO___

*What Will I Be Expected To Turn in?*

Great question.  In order for this project to be considered complete, I expect you to slack me a link to a git repo containing working code for the simulation.  Please do not change the random seed set in the Simulation class! It is currently set to 42, and I will be using this to double check that your simulation works and spits out the expected results.  

Your repo should contain:
  * Completed classes for logger.py, simulation.py, and person.py.
  * At least 1 log file generated from running your simulation.  

*What Were the Stretch Challenges for this Project?*

You'll find some of the smaller, individual stretch challenges contained with the comments of the code on the logger class.  Other stretch challenges include:

  * Extending functionality so that we can test the spread of multiple viruses through a given population at the same time. (Difficulty Level: Hard)
  * Create a Visualizer class that can spit out visualizations of the spread of the virus based on the log files of a simulation.  HINT: You'll want to use Matplotlib for visualization stuff, because its easy to use and generally awesome at this sort of thing.  You may also want to consider using a library like Pandas for organizing and cleaning your data in a more professional way, especially if you want to visualize answers to more complex questions.  Matplotlib and Pandas play very nicely together! (Difficulty Level: Medium)

  *As always, I'm available on slack or over email if you have any questions or concerns. Good luck, and happy coding!*

  --Mike 
  
