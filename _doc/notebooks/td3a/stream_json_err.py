
import sys, os
for row in sys.stdin:
    sys.stdout.write(sys.executable + "\n")
    sys.stdout.write(str(sys.version) + "\n")
    sys.stdout.write(row + "\n")
    # pour obtenir les variables d'environnement
    #for k in os.environ:
    #    sys.stdout.write("%s=%s\n" % (k,os.environ[k]))
    sys.stdout.flush()