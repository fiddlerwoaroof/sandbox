GOAL = 17

POP = 30

a = [encode(sensify_list(decode(get_n_genes()))) for x in range(POP)]

from functools import partial

cp = partial(compare_seqs, goal=GOAL)

a.sort(cp)

b = [evaluate(decode(x)) for x in a]

b

sorted(b)



a = [encode(sensify_list(decode(cross(*a[:2])))) for _ in range(POP)]
