female(kani).						%kani is female.
female(priya).						%priya is female.	
female(pavi).						%pavi is female.
female(ann).						%ann is female.

male(arun).						%arun is male.
male(chandru).					%chandru is male.
male(hari).						%hari is male.
male(thamizh).					%thamizh is male.

parent(kani,chandru).					%kani is a parent of chandru.
parent(hari,chandru).					%hari is a parent of chandru.
parent(hari,priya).					%hari is a parent of priya.
parent(chandru,ann).					%chandru is a parent of ann.

parent(chandru,pavi).					%chandru is a parent of pavi.
parent(pavi,arun).					%pavi is a parent of arun.
parent(chandru,thamizh).				%chandru is a parent of  thamizh.
parent(thamizh,arun).					%thamizh is a parent of arun.

%Rules:.
mother(X,Y):- parent(X,Y),female(X).			
father(X,Y):-parent(X,Y),male(X).			
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.	
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.	
grandparent(X,Y):-parent(X,Z),parent(Z,Y).		
grandmother(X,Z):-mother(X,Y),parent(Y,Z).		
grandfather(X,Z):-father(X,Y),parent(Y,Z).		
wife(X,Y):-parent(X,Z),parent(Y,Z),female(X),male(Y).	
uncle(X,Z):-brother(X,Y),parent(Y,Z).
