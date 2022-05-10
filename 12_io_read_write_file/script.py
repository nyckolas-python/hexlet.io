'''
input_file = open("/home/nyckolas/hexlet.io/12_io_read_write_file/input.txt", "r")
output_file = open("/home/nyckolas/hexlet.io/12_io_read_write_file/output.txt", "w")
for i, line in enumerate(input_file, 1):
	output_file.write("{})0 {}".format(i, line))
input_file.close()
output_file.close()
'''


with open("/home/nyckolas/hexlet.io/12_io_read_write_file/input.txt", "r") as input_file:
	with open("/home/nyckolas/hexlet.io/12_io_read_write_file/input.txt", "w") as output_file:
		for i, line in enumerate(input_file, 1):
			output_file.write(
				"{}) {}".format(i, line)
			)