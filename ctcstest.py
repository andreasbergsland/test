import ctcsound
c = ctcsound.Csound()        # Create an instance of the Csound object
# Defining our Csound ORC code within a triple-quoted, multiline String
orc = """
sr=44100
ksmps=32
nchnls=2
0dbfs=1
instr 1 
aout vco2 0.5, 440
outs aout, aout
endin"""


# Defining our Csound SCO code 
sco = "i1 0 1"

c.setOption("-odac")  # Using SetOption() to configure Csound
                      # Note: use only one commandline flag at a time

c.compileOrc(orc)     # Compile the Csound Orchestra string
c.readScore(sco)      # Compile the Csound SCO String
c.start()  # When compiling from strings, this call is necessary before doing any performing
#c.perform()  # Run Csound to completion

# The following is our main performance loop. We will perform one block of sound at a time 
# and continue to do so while it returns 0, which signifies to keep processing.  We will
# explore this loop technique in further examples.

while (c.performKsmps() == 0):
    pass
c.stop()