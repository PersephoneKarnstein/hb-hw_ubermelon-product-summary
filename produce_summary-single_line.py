def print_deliveries(path):
    for i, line in enumerate(open(path)): print("{3} Delivered {1} {0} for a total of ${2}.".format(*list(line.rstrip().split('|')) + ["\n\n{}/{}/{}\n".format(path[-8:-6], path[-6:-4], path[-12:-8])  if i==1 else ""]))
