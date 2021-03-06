def decode(physical_signal):
	# List physical signals
	high_signal = '¯'
	low_signal = '_'
	pipe_signal = '|'

	bits = ''  # if no matter start with
#	bits = '0' # start with bit 0
	def check_health() -> None:
		# Check validators on physical signal

		if not physical_signal:
			raise Exception('Physical signal is empty')

		for token in physical_signal:
			if token not in [low_signal, high_signal, pipe_signal]:
				raise Exception(
					'Token {} is invalid int physical signal segment'.
					format(token))
#			if physical_signal[0] not in [low_signal, high_signal]:
#			# Validate high and low signal
#			raise Exception(
#				'Physical signal {} does not start with high or low signal'.
#				format(physical_signal[0]))
	check_health()

	# Get a bool bit
	def give_bit(λ): return str((0, 1)[λ])
	change_signal = False

	# Skip first element, if first bit always is 0
#	for token in physical_signal[1:]:
	for token in physical_signal:

		# If changed singal return bit 1
		current_bit = give_bit(change_signal)

		if token == pipe_signal:
			# When change signal is identified the next bit should be 1
			change_signal = True
			continue
		else:
			# Bit should be 0
			change_signal = False

		bits += current_bit
	print(bits)
	return bits

# Test Program
print(decode('_|¯|____|¯|__|¯¯¯') == '011000110100')
print(decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111')
print(decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111')