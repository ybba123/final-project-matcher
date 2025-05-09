# final-project-matcher

(working on rn)

Some points we might cover:
- How to install required tools (you can link to tool pages for the main instructions).
- How to run your project.
- The general problem your project is tackling.

Also include:
- What tradeoffs did you make in choosing your representation? What else did you try that didn’t work as well?
  - As demonstrated in our presentation slides, some tradeoffs we made in choosing our representation include:
    - That we were unable to figure out how to model the concept of sorting multiple people into groups of 3 with z3 in time for this presentation
    - Some ideas we tried that didn't work/that we abandoned:
      - Generate all possible subsets of size 3 of the set of students and use z3 to check if each set is compatible
      - Use z3 to create a list of students who are all compatible with each other and a list of students who are incompatible with at least one member of the first group: divide the first group into groups of 3          and output these as matchings; try to match the second list again, repeating the same process
- What assumptions did you make about scope? What are the limits of your model?

Additional private components:                                 
Did your goals change at all from your proposal? Did you realize anything you planned was unrealistic, or that anything you thought was unrealistic was doable?
How should we understand an instance of your model, if applicable?
