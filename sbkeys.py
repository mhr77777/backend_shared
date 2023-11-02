sbbase = open(".dbkeys")
keys = sbbase.read().split("=")
sbkey = keys[0]
sbwritekey = keys[1]
sbbase.close()