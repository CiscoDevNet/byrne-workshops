import sys
import cli

intf = sys.argv[1:]
intf = ''.join(intf[0])

cli.configurep(["int %s" % intf, "no shutdown", "end"])