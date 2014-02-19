import os, shutil, argparse

parser = argparse.ArgumentParser()
parser.add_argument("tbnumber",help="Number of Testbench to use",type=int)
args=parser.parse_args()
n = args.tbnumber

try:
	cwd = os.getcwd()
	srcd = os.path.join(cwd,'benches')
	for i in ["answers","instmem","datamem"]:
		shutil.copy(os.path.join(srcd,i+"_"+str(n)+".txt"),os.path.join(cwd,i+".txt"))
		print "Copied "+i

except:
	print "Activating for n = "+str(n)+" failed. Make sure the testbench being selected exists, and your project folder is set up correctly"
