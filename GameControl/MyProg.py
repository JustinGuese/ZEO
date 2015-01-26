import matplotlib.pyplot as plt
import numpy as np

plt.ion()
x = np.arange(7)
freqs = []
medians = [[],[],[],[],[],[],[]]
labels = ["Delta","Theta","Alpha","Low Beta","Beta","High Beta","Gamma"]
labels2 = ['2-4','4-8','8-13','11-14','13-18','18-21','30-50']
concVal = 0

print "Justin's Program ready!"
def getUpdate(object):
	print "Got update"
	freqs.append(object)
	visualize(object)

def visualize(object):
	plt.clf()
	sums = [[],[],[],[],[],[],[]]
	ranges = np.arange(7)
	trials = np.arange(len(freqs))
	for trial in trials:
		current = freqs[trial]
		for i in ranges:
			sums[i].append(current[i])
	
	for i in ranges:
		medians[i]= np.median(sums[i])
	
	plt.plot(medians)
	plt.plot(object,'rx')
	plt.xticks(ranges,labels)
	plt.xlim(-1,7)
	plt.legend()
	
	
	#define if concentrated
	concentrated = False
	relaxation = (object[0]-medians[0])+(object[1]-medians[1])+(object[2]-medians[2])
	concentration = (object[3]-medians[3])+(object[4]-medians[4])+(object[5]-medians[5])
	concVal = relaxation - concentration #concentration value
	if relaxation > 0 and concentration < 0:
		concentrated = False
		plt.title("Surely Not Concentrated")
	elif relaxation < 0 and concentration > 0:
		concentrated = True
		plt.title("Surely Concentrated")
	elif concVal > 0:
		concentrated = False
		plt.title("Not Concentrated ?")
	elif concVal <= 0:
		concentrated = True
		plt.title("Concentrated ?")
	else:
		print "Fail!"

	plt.draw()


	
