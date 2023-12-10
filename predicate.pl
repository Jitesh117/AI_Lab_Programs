/* 1. Convert to CNF and extract clausescIdea:  Find the conjucntive normal form Extract the clauses from the cnf. Distributive law to convert disjunctions */
distribute((X /\ Y) \/ Z, (X \/ Z) /\ (Y \/ Z), true) :- !.
distribute(X \/ (Y /\ Z), (X \/ Y) /\ (X \/ Z), true) :- !.
distribute(X,X,fail).
/* If the given input is of the form X /\ Y, we recursively
   find the cnf of X and Y until they become atoms */
cnf((X /\ Y), (A /\ B)) :-
 !,
 cnf(X,A),
 cnf(Y,B).
/* If the given input is of the form X \/ Y, we recursively find the cnf of X and Y and apply distributive law. If further conversion required after applying distributive law recursively find the cnf of result */
cnf((X \/ Y), Z) :-
  !,
  cnf(X,A),
  cnf(Y,B),
  distribute((A \/ B), Res, Flag),
  (Flag
  -> cnf(Res, Z)
  ; Z = Res
  ).
/* Demorgan's law */
cnf(not(X /\ Y), R) :-
 !,
 cnf(not(X) \/ not(Y), R).

/* Demorgan's law */
cnf(not(X \/ Y), R) :-
 !,
 cnf(not(X) /\ not(Y), R).
/* converting not(not(X)) as X */
cnf(not(not(X)), R) :-
 !,
 cnf(X, R).
/* Base case */
cnf(A, A).
myappend([],L2,L2).
myappend([F1|T1],L2,[F1|L3]) :-
  myappend(T1, L2, L3).
/* Extracting disjuctions out of the individual clauses in CNF */
/* This step is simple because we already know that each clauses in CNF is a disjunction of atomic elements. So, just recursively extracting until we get atomic elements of the clause */
extract_or(A \/ B, Out) :-
  !,
  extract_or(A, X),
  extract_or(B, Y),
  myappend(X, Y, Out).
extract_or(not(A), [not(A)]).
extract_or(A,[A]).
/* Dividing the CNFs one Clause at a time and appending the results in a list */
extract_clauses(A /\ B, Out) :-
  !,
  extract_clauses(A, Out1),
  extract_clauses(B, Out2),
  myappend(Out1, Out2, Out).
/* Base case. A clause having just one atomic element. */
extract_clauses(A, Out) :-
   atom(A),
   Out = [[A]].
/* Base case. A clause having just one atomic negative element */
extract_clauses(not(A), Out) :-
   atom(A),
   Out = [[not(A)]].
/* Calling extract_or to extract individual atomic elements in a clause and then append them in one single list */
extract_clauses(A \/ B, Out) :-
  !,
  extract_or(A, Out1),
  extract_or(B, Out2),
  myappend(Out1, Out2, Inter),
  Out = [Inter].

/* Entry point. Find the CNF then Extract the clauses */
prop_clause(A, X) :-
  cnf(A, Res),
  extract_clauses(Res, X),
  !.
/* Test run
prop_clause(p \/ q, C).
C = [[p,q]];
no
prop_clause((p/\q) \/ r \/ (s/\t) , S).
S = [[p,r,s],[p,r,t],[q,r,s],[q,r,t]];
no
prop_clause(p /\ (not(q) \/ r), S).
S = [[p],[not q,r]];
no
prop_clause(p,R).
R = [[p]];
no
*/
/* 2 (a). Resolution */
/* Idea:
   Recursively choose two different clauses from the input list, Resolve them and add the resolvent to input list. If we get a [] empty list in any step, report true.  If we have exhausted all possible combinations of input clauses, report no.*/
mymember(Element,[Element|_List]).
mymember(Element,[_First|Tail]) :- mymember(Element,Tail).
mydelete(X,[Fi|Li],Lo) :-
  Fi = X,
  Li = Lo.
mydelete(X,[Fi|Li],[Fo|Lo]) :-
  Fi = Fo,
  Fi \= X,
  delete(X,Li,Lo).
/* Sort individual clauses */

sortClauses([], []).
sortClauses([H|List], [H1|Out]) :-
  sort(H,H1),
  sortClauses(List, Out).
/* Sort the independent clauses of input list and call resolve */
/* Why do we sort individual clauses ?
       Since we check whether a clause is already a member of input list,we need to keep the clauses uniform everywhere. Hence the sorting. E.g [p,q] is same as that of [q,p]. */

resolve(List) :-
  sortClauses(List, L),
  do_resolve(L).
/* Find a resolvent and if it is empty, the given input is unsatisfiable. Else append the resolvent to the input list and continue resolving */

do_resolve(List) :-
  once(get_resolvent(List, Resolvent)),
  (Resolvent = []
  -> true
  ;resolve([Resolvent|List])).
/* Taking two clauses A and B from List, and resolve them */
get_resolvent(List, Resolvent) :-
  mymember(A, List),
  mymember(B, List),
  A \= B,
  res(A, B, T),
  (T = false
  -> false
  ;(mymember(T, List)
  -> false
  ; Resolvent = T)).
/* We have two clauses A and B here. We try to find an atomic element in both the clauses which is of the form  x, not(x) and cancel them. Append the rest of the atoms to form a resolvent. Then sort the final resolvent */
res(A, B, T) :-
  mymember(A1, A),
  (A1 = X
  -> B1 = not(X)
  ; not(B1) = A1),
  (mymember(B1, B)
  -> mydelete(A1, A, TempA),
     mydelete(B1, B, TempB),
     myappend(TempA, TempB, Ans),
     sort(Ans, T)
  ; false ).
/* Test run
resolve([[p],[not(p)]]).
yes
resolve([[p,not(q)],[q, not(p)]]).
no
resolve([[p, r], [q, not(r)], [not(p)], [not(q)]]).
yes
*/
/* 2(b) printing resolvents and source clauses */
/* Same logic as 2 (a) */
resolve_pr(List) :-
  sortClauses(List, L),
  do_resolve_pr(L).
do_resolve_pr(List) :-
  once(get_resolvent_pr(List, Resolvent)),
  (Resolvent = []
  -> true
  ; resolve_pr([Resolvent|List]) ).
/* Printing once we resolve something and get a valid resolvent */
get_resolvent_pr(List, Resolvent) :-
  mymember(A, List),
  mymember(B, List),
  A \= B,
  res(A, B, T),
  (T = false
  -> false
  ;(mymember(T, List)
  -> false
  ;
  Resolvent = T),
  write('Source 1 : '),writeln(A),
  write('Source 2 : '),writeln(B),
  write('Resolvent : '),writeln(Resolvent),writeln('') ).

