import json
import sys

# import spacy
# from spacy.matcher import PhraseMatcher

# nlp = spacy.load('en')
# matcher = PhraseMatcher(nlp.vocab)

# Get list of quantifiers
quant_lst = [tok.strip() for tok in open("data/quantifiers.txt")]

# # Generate quantifier patters to match on
# patters = [nlp(quant) for quant in quant_lst]
# matcher.add("quantifiers", None, *patters)

objs_quant = []
objs_other = []

ifile = sys.argv[1]

print("Processing sentence pairs...")

with open(ifile, "r") as data_file:

    for cnt, line in enumerate(data_file):

        if (cnt > 0 and cnt % 2000 == 0):
            print(cnt)

        obj = json.loads(line)

        # sent1 = nlp(obj["sentence1"])
        # sent2 = nlp(obj["sentence2"])

        # matches1 = matcher(sent1)
        # matches2 = matcher(sent2)

        # if (matches1 or matches2):
        #     objs_quant.append(obj)
        # else:
        #     objs_other.append(obj)

        sent1 = obj["sentence1"].lower()
        sent2 = obj["sentence2"].lower()

        # Check if first word in sentence is a quantifier
        if any(quant == sent1.split()[0] for quant in quant_lst):
            objs_quant.append(obj)
            continue

        if any(quant == sent2.split()[0] for quant in quant_lst):
            objs_quant.append(obj)
            continue

        objs_other.append(obj)


print("#quant pairs:", len(objs_quant))
print("#other pairs:", len(objs_other))

print("Writing output files...")

# Write quantifier output file
ofile = open("{0}split.quant.jsonl".format(ifile[:-5]), "w")
for obj in objs_quant:
    ofile.write(json.dumps(obj))
    ofile.write("\n")
ofile.close()

# Write other output file
ofile = open("{0}split.other.jsonl".format(ifile[:-5]), "w")
for obj in objs_other:
    ofile.write(json.dumps(obj))
    ofile.write("\n")
ofile.close()

print("Done")
