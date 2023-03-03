import requests
import time

print("# Exercise 1a")

res_1a = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/ethanol/property/Molecularweight/txt')
print("The molecular weight of ethanol in a txt format", res_1a.text)
# Just change last 3 elements before .txt

# Exercise 1a

res_1b = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/asprin/property/HBondAcceptorCount/txt')
print("The number of hydrogen-bond acceptors of aspirin ", res_1b.text)
# Go to https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest#section=Compound-Property-Tables for all properties

# lesson 2 goes on to explain how you break the last  elements into variables (pugrest, pugin, pugoper, pugout)
# This is easier visually but takes more space
# url can be generated with join(), don't use in on input as variable

pugrest = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
pugin = "compound/name/asprin"
pugoper = "property/HBondAcceptorCount"
pugout = "txt"

url = pugrest + '/' + pugin + '/' + pugoper + '/' + pugout
print("This is the url for Hbondacceptor txt", url)

# Lesson 3
print("Exercise 3a")

Alkanes = ['Methane', 'Ethane', 'Propane', 'Butane', 'Pentane', 'Hexane', 'Heptane', 'Octane', 'Nonane', 'Decane',
           'Undecane', 'Dodecane']

pugrest_alkanes = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
pugoper_alkanes = "property/XLogP"
pugout_alkanes = "txt"

for i in range(len(Alkanes)):
    pugin_alkanes = "compound/name/" + Alkanes[i]
    url = "/".join([pugrest_alkanes, pugin_alkanes, pugoper_alkanes, pugout_alkanes])
    res_alkanes = requests.get(url)
    print(Alkanes[i], ":", res_alkanes.text)
    if i % 5 == 4:  # the % is the modulo operator and returns the remainder of a calculation (if i = 4, 9, ...)
        time.sleep(1)
print("Exercise 3b")

AA = ['Alanine', 'Arginine', 'Asparagine', 'Aspartic acid', 'Cysteine', 'Glutamic acid', 'Glutamine', 'Glycine',
      'Histidine', 'Isoleucine', 'Leucine', 'Lysine', 'Methionine', 'Phenylalanine', 'Proline', 'Serine', 'Threonine',
      'Tryptophan', 'Tyrosine', 'Valine']

pugrest_AA = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
pugoper_AA = "property/CanonicalSMILES"
pugout_AA = "txt"

for i in range(len(AA)):
    pugin_AA = "compound/name/" + AA[i]
    url = "/".join([pugrest_AA, pugin_AA, pugoper_AA, pugout_AA])
    res_AA = requests.get(url)
    print(AA[i], ":", res_AA.text)
    if i % 5 == 4:
        time.sleep(1)

# Exercise 4

pugrest_4 = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
pugoper_4 = "property/HeavyAtomCount,RotatableBondCount,MolecularWeight,HBondDonorCount,HBondAcceptorCount,XLogP,TPSA," \
            "IsomericSMILES"
pugin_4 = "compound/cid/"
pugout_4 = "csv"
csv = ""

cids = [471, 1981, 2005, 2097, 2151, 2198, 2206, 2214, 2244, 2307, 2308, 2313, 2355, 2396, 2449, 2462, 2466, 2581, 2662,
        2794, 2863, 3000, 3003, 3033, 3056, 3059, 3111, 3177, 3194, 3230, 3242, 3282, 3308, 3332, 3335, 3342, 3360,
        3371, 3379, 3382, 3384, 3394, 3495, 3553, 3612, 3672, 3715, 3716, 3718, 3778, 3824, 3825, 3826, 3935, 3946,
        3965, 4009, 4037, 4038, 4044, 4075, 4159, 4237, 4386, 4409, 4413, 4487, 4488, 4495, 4534, 4553, 4614, 4641,
        4671, 4692, 4781, 4888, 4895, 4921, 5059, 5090, 5147, 5161, 5208, 5228, 5339, 5352, 5359, 5362, 5468, 5469,
        5475, 5480, 5509, 5733, 5743, 5744, 5745, 5753, 5754, 5755, 5834, 5865, 5875, 5876, 5877, 6094, 6213, 6215,
        6247, 6436, 6741, 7090, 7497, 8522, 9053, 9231, 9642, 9782, 9878, 10114, 10154, 10170, 10185, 10206, 12555,
        12938, 13802, 14982, 15209, 16490, 16533, 16623, 16639, 16752, 16923, 17198, 19161, 20469, 21102, 21700, 21800,
        21826, 21975, 22419, 23205, 26098, 26248, 26318, 28718, 28871, 30869, 30870, 30951, 31307, 31378, 31508, 31635,
        31799, 31800, 32153, 32327, 32798, 33958, 35375, 35455, 35935, 36833, 37425, 38081, 38503, 39212, 39941, 40000,
        40632, 41643, 43261, 44219, 47462, 47795, 50294, 50295, 51717, 54445, 54585, 57782, 59757, 60164, 60490, 60542,
        60712, 60726, 60864, 61486, 62074, 62924, 63006, 63019, 64704, 64738, 64746, 64747, 64927, 64945, 64971, 64982,
        65394, 65464, 65655, 65679, 65762, 66249, 67417, 68700, 68704, 68706, 68731, 68749, 68819, 68865, 68869, 68917,
        71246, 71354, 71364, 71386, 71398, 71414, 71415, 71771, 72158, 72300, 73400, 82153, 84003, 84429, 90763, 91626,
        91670, 100472, 102011, 104762, 104943, 107641, 107738, 107793, 108068, 108130, 114753, 114840, 114917, 114999,
        115239, 119032, 119286, 119365, 119607, 119828, 119871, 121928, 121957, 122139, 122179, 122182, 123619, 123673,
        123723, 124978, 128191, 128229, 128571, 133021, 134896, 146364, 151075, 151166, 152165, 155354, 155761, 156391,
        158103, 159557, 162666, 164676, 167928, 168928, 174093, 174277, 176155, 177976, 180604, 183088, 189821, 192156,
        196122, 196840, 196841, 200674, 201587, 219121, 222786, 229860, 235244, 236702, 259846, 263373, 275182, 292331,
        425990, 439503, 439533, 441335, 441336, 442534, 442993, 443943, 443949, 443967, 444036, 445154, 445858, 446925,
        479503, 485711, 490428, 501254, 522325, 546807, 578771, 584547, 610479, 633091, 633097, 636374, 636398, 656604,
        656656, 656852, 657238, 667550, 927704, 969510, 969516, 1548887, 1548910, 2737488, 3033890, 3033980, 3045402,
        3051696, 3055172, 4129359, 4306515, 4483645, 5018304, 5185849, 5280802, 5280914, 5280915, 5281004, 5281071,
        5281515, 5281522, 5281792, 5282183, 5282193, 5282230, 5282387, 5282402, 5282492, 5283542, 5283734, 5284538,
        5284539, 5311051, 5311052, 5311066, 5311067, 5311093, 5311101, 5311108, 5311169, 5311180, 5318517, 5320420,
        5322111, 5352624, 5353725, 5353726, 5353740, 5353864, 5354499, 5377381, 5420804, 5420805, 5458396, 5472495,
        5481958, 5701991, 5702036, 5702148, 5702212, 5702252, 5702287, 5745214, 5942250, 6420050, 6429274, 6437368,
        6437387, 6438873, 6447131, 6453785, 6473881, 6509979, 6708733, 6710677, 6714002, 6917783, 6917852, 6917894,
        6918172, 6918173, 6918332, 6918445, 6918452, 6918612, 6925666, 7060958, 7251185, 9554199, 9798098, 9799453,
        9841438, 9843941, 9846332, 9865808, 9868219, 9869053, 9871508, 9875547, 9883509, 9897518, 9897771, 9907157,
        9913795, 9919776, 9926694, 9934547, 10363606, 10918539, 11158972, 11513733, 11561674, 11616712, 11870423,
        11949636, 11954221, 11954316, 11954353, 11954369, 11957468, 11961431, 11972243, 11972532, 12300053, 12313906,
        12313911, 12606303, 12634263, 12714644, 12874922, 13018150, 13020033, 13041095, 14010989, 14515707, 14798494,
        15895902, 16051947, 16132369, 16213022, 16213698, 16218996, 16219353, 16220118, 16759566, 16760658, 17750985,
        17753757, 18526330, 18632363, 18647121, 18943026, 20054915, 21120116, 21637635, 21637642, 21893738, 21893804,
        21982135, 22141508, 22811280, 23509770, 23631982, 23653552, 23657872, 23663407, 23663409, 23663418, 23663959,
        23663989, 23665411, 23665999, 23667642, 23669636, 23674183, 23674255, 23674745, 23675763, 23680530, 23681059,
        23684814, 23688663, 23693301, 23694214, 23702389, 24181458, 24721429, 24761485, 24799587, 24847961, 24847981,
        24867460, 24867465, 24867475, 24883465, 24916955, 25077872, 25113755, 25796773, 40469526, 44119558, 44202892,
        44260118, 44266812, 44386560, 45006151, 45006158, 45039955, 45356876, 45356931, 45357558, 45357932, 45358013,
        45358120, 45358130, 45358140, 45358148, 45358149, 45488525, 46174093, 46397498, 46780650, 46780910, 46783539,
        46783786, 46783814, 46863906, 46878350, 46882877, 50989825, 51026956, 51340230, 51398089, 53384387, 53394893,
        53486221, 53486290, 53486322, 54194814, 54605501, 54675840, 54676228, 54677470, 54677971, 54677972, 54677977,
        54682045, 54684589, 54690031, 54697648, 54708862, 54714524, 56841932, 56842111, 56845155, 57347755, 57486087,
        67668959, 67804972, 67986221, 70470286, 70678885, 71306882, 71587162, 72774967, 72941490, 72941625, 73758129,
        73759663, 73759808, 74787565, 77906397, 78577433, 90488794, 91711382, 91826463, 91873711, 91881846, 92131836,
        92462493, 102004404, 102601886, 117072385, 117072403, 117072410, 118701141, 118701402, 118984459, 122130078,
        122130111, 122130185, 122130213, 122130768, 122173054, 122173183, 122361610, 123134657, 124081055, 124463365,
        126968472, 126968501, 126968801, 126969212, 126969455, 129009998, 129010022, 129010033, 129010043, 129316829,
        129317859, 129317898, 129628207, 129628892, 129670532, 129735029, 131632430, 131635023, 131676243, 131750284,
        131954647, 131954667, 132399051, 132399058, 133112890, 133126366, 133126370, 133562807, 133659920, 133687604,
        134129698, 134159361, 134460917, 134612785, 134687786, 134688123, 134688323, 134688977, 134689786, 134693106,
        134693125, 134693234, 134694728, 134694860, 135413496, 135413505, 135414247, 135484078, 135515521, 135565709,
        136040192, 137177332, 137699687, 137705034, 137705717, 137705725, 137705994, 137706376, 137706400, 137795135,
        138059757, 138107776, 138113311, 138113507, 138113581, 138114182, 138114743]

chunk_size = 10
if len(cids) % chunk_size == 0:  # check if total number of cids is divisible by 10 with no remainder
    num_chunks = len(cids) // chunk_size  # sets number of chunks
else:  # if divide by 10 results in remainder
    num_chunks = len(cids) // chunk_size + 1  # add one more chunk

print("Exercise 4")
print("Number of CIDs:", len(cids))
print("Number of chunks:", num_chunks)

for i in range(num_chunks):  # sets number of requests to number of data chunks as determined above

    idx1 = chunk_size * i  # sets a variable for a moving window of cids to start in a data chunk
    idx2 = chunk_size * (i + 1)  # sets a variable for a moving window of cids to end ina data chunk

    pugin_4 = "compound/cid/" + ",".join([str(x) for x in cids[idx1:idx2]])  # build pug input for chunks of data
    url = "/".join([pugrest_4, pugin_4, pugoper_4, pugout_4])  # Construct the URL

    res = requests.get(url)

    if i == 0:  # if this is the first request, store result in empty csv variable
        csv = res.text
    else:  # if this is a subsequent request, add the request to the csv variable adding a new line between chunks
        csv = csv + "\n".join(res.text.split()[1:]) + "\n"

    if i % 5 == 4:
        time.sleep(1)

print(csv)
