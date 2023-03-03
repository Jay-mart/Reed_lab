fasta_file = ">histone_H3\nMARTKQTARKSTGGKAPRKQLATKAARKSAPATGGVKKPHRYRPGTVALREIRRYQKSTE\
LLIRKLPFQRLVREIAQDFKTDLRFQSSAVMALQEACEAYLVGLFEDTNLCAIHAKRVTIMPKDIQLARRIRGERA"
print(fasta_file)

# Two lines in the fasta file, let us separate the lines
fasta_lines = fasta_file.split('\n')
type(fasta_lines)
print(fasta_lines)

for i in fasta_lines:
    if i.startswith('>'):
        seq_name = i
    else:
        seq = i
print("Seq name:\t" + seq_name + "\nSeq:\t\t" + seq)
for i in fasta_lines:
    if i.startswith('>'):  # replacing
        seq_name = i
    else:
        seq = i
        # Count the positive residues
        count = seq.count('K') + seq.count('R') + seq.count('H')
        # print the results
        print("Seq name:\t" + seq_name + "\nSeq:\t\t" + seq + "\nCount of Positive Residues:" + str(count))
        for i in fasta_lines:
            if i.startswith('>'):
                seq_name = i
            else:
                seq = i
                # Count the positive residues
                count = seq.count('K') + seq.count('R') + seq.count('H')
                percent_positive = count * 100 / len(seq)
                #  Round to limit decimals
                print("Seq name:\t" + seq_name + "\nSeq:\t\t" + seq + "\n% of Positive Residues:" + str(
                    round(percent_positive, 1)))

fasta_file = ">histone_H3\nMARTKQTARKSTGGKAPRKQLATKAARKSAPATGGVKKPHRYRPGTVALREIRRYQKSTELLIRKLPFQRLVREIAQDFKTDLR\
FQSSAVMALQEACEAYLVGLFEDTNLCAIHAKRVTIMPKDIQLARRIRGERA\n>Actin\nMDDDIAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMG\
QKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKMTQIMFETFNTPAMYVAIQAVLSLYASGRTTGIVMDSGDG\
VTHTVPIYEGYALPHAILRLDLAGRDLTDYLMKILTERGYSFTTTAEREIVRDIKEKLCYVALDFEQEMATAASSSSLEKSYELPDGQVITIGNERFRCPEALFQPSFLG\
MESCGIHETTFNSIMKCDVDIRKDLYANTVLSGGTTMYPGIADRMQKEITALAPSTMKIKIIAPPERKYSVWIGGSILASLSTFQQMWISKQEYDESGPSIVHRKCF\n>\
Gapdh\nMGKVKVGVNGFGRIGRLVTRAAFNSGKVDIVAINDPFIDLNYMVYMFQYDSTHGKFHGTVKAENGKLVINGNPITIFQERDPSKIKWGDAGAEYVVESTGVFT\
TMEKAGAHLQGGAKRVIISAPSADAPMFVMGVNHEKYDNSLKIISNASCTTNCLAPLAKVIHDNFGIVEGLMTTVHAITATQKTVDGPSGKLWRDGRGALQNIIPASTGA\
AKAVGKVIPELNGKLTGMAFRVPTANVSVVDLTCRLEKPAKYDDIKKVVKQASEGPLKGILGYTEHQVVSSDFNSDTHSSTFDAGAGIALNDHFVKLISWYDNEFGYSNRV\
VDLMAHMASKE\n>HuR\nMSNGYEDHMAEDCRGDIGRTNLIVNYLPQNMTQDELRSLFSSIGEVESAKLIRDKVAGHSLGYGFVNYVTAKDAERAINTLNGLRLQSKTIK\
VSYARPSSEVIKDANLYISGLPRTMTQKDVEDMFSRFGRIINSRVLVDQTTGLSRGVAFIRFDKRSEAEEAITSFNGHKPPGSSEPITVKFAANPNQNKNVALLSQLYHSP\
ARRFGGPVHHQAQRFRFSPMGVDHMSGLSGVNVPGNASSGWCIFIYNLGQDADEGILWQMFGPFGAVTNVKVIRDFNTNKCKGFGFVTMTNYEEAAMAIASLNGYRLGDKI\
LQVSFKTNKSHK"
print(fasta_file)
seq_name = seq_name.replace(">", '')
print(seq_name)


# Finding sequence motifs
seq = 'AUGCAUGCAGCUAGCUAAACCCGGGUUAUAUAGAAUUUUUAAAGUAGUAGGGCCGAGUAGAUUUUUAAGAGAGAUAUUUUUAGAGAGAUAGAUGAGAGG'
print(seq.find('AUUUUUA'))

index = 0
while index < len(seq):
    index = seq.find('AUUUUUA', index)
    if index == -1:
        break
    print('Motif found at', index)
    index += len('AUUUUUA')