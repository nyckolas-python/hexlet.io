#!/usr/bin/env python3

def to_rna(dna):
	d = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
	rna = ''
	for v in dna:
		rna += d[v]
	return rna

def build_query_string(param):
	result = ''
	for i in param:
		result =''.join(str(i)+str(param[i])) + result
	return print(result)


def test():

	param = {'per': 10, 'page': 1}
	build_query_string(param)


if __name__ == '__main__':
	test()