from urllib import request
from pippi import dsp
from pippi import tune

accession = "NC_012920.1"
url = f"https://www.ncbi.nlm.nih.gov/search/api/sequence/{accession}"
lines = [x.decode('UTF-8').rstrip() for x in request.urlopen(url).readlines()]
string = "".join(lines[1:])
N = len(string)

def getbase(string,N,i):
    return(string[i%N])

print(getbase(string,N,16569))

guitar = dsp.read('sounds/guitar10s.wav')

#freqs = tune.chord('I', key='C', octave=3, ratios=tune.just)
#print('Cmaj: %s' % freqs)
#original_freq = tune.ntf('A2')

original_freq = 110.0
freqs = [130.81,146.83,164.81,174.61,196.0]


#speeds = [ new_freq / original_freq for new_freq in freqs ]
translate={"A":freqs[0]/original_freq,"T":freqs[1]/original_freq,"C":freqs[2]/original_freq,"G":freqs[3]/original_freq,"N":freqs[4]/original_freq}

pos = 0  
bigbeat = 0.05
smallbeat = 0.0

out = dsp.buffer()
for i,character in enumerate("ATCGATCG"):
    note = guitar.speed(translate[character])
    out.dub(note,i*bigbeat)
out.write("output/test.wav")

out = dsp.buffer()
#for speed in speeds:
#for character in string[0:1000]:
for i in range(0,2100,3):
    triplet = string[i:(i+3)]
    #print(triplet)
    for character in triplet:
        # Create a pitch-shifted copy of the original guitar
        note = guitar.speed(translate[character])
        # Dub it into the output buffer at the current position 
        out.dub(note, pos)
        pos += smallbeat
        
    pos = i*bigbeat/3

# Save this output buffer
out.write('output/mtdna_chord.wav')

# How to choose four notes that sounds good together in threes?
# How to use pippi to generate them?
# How to make a better font than guitar?
