import io

# not in use

class IOProtecter(io):
	
	@classmethod
	def open(self, file, mode, buffering = -1):
		io.open
