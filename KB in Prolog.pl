% fact

parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').


%rule

grandparent(X,Z):-
	parent(X,Y),parent(Y,Z).


% procedure

findGc:-
	write('Grandparent: '),read(Gp),write('Grandchildren: '),
	grandparent(Gp, Gc),write(Gc),tab(5),fail.
findGc.


%%	%%%%%%%%%%%%%
%
%?-findGc.
%Grandparent: 'Hasib'.
%Grandchildren: Sohel     Rebeka
%
%%	%%%%%%%%%%%%%
%
%	fail is a special symbol that will immediately fail when Prolog
%	encounters it . That may not sound too useful, but
%	when Prolog fails, it tries to backtrack . Thus fail
%	can be viewed as an instruction to force backtracking.
%
%	%%%%%%%%%%%%%
