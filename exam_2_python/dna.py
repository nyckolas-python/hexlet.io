def to_rna(dna):
	d = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
	rna = ''
	for v in dna:
		rna += d[v]
	return rna