#!/usr/bin/env python3

def to_rna(dna):
	d = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
	rna = ''
	for v in dna:
		rna += d[v]
	return rna

def test():

	dna = ('ACGTGGTCTTAA')
	print(to_rna(dna))


if __name__ == '__main__':
	test()