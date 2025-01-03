from Bio.Seq import Seq

def CountDNAntBiopython(Genome, Pattern):
    """
    Count the number of times a pattern appears in a DNA sequence using Biopython.

    Args:
        Genome (str): The DNA sequence to search within.
        Pattern (str): The DNA pattern to search for.

    Returns:
        int: The count of Pattern occurrences in Genome.
    """
    genome_seq = Seq(Genome)
    count = genome_seq.count_overlap(Pattern)
    return count


# Example usage
Genome = "AGCTCAGAGCCGGGAACTGTTCACTCGGACACGGCCGAGTGTGGGTACTGTTTAGGCTACGAAGTTCCCAGATTCTTCCACGGAATTGCCTCTCCAGAGTCCACCTTATCTTTTTCGAGAGACTTCGGCTTTTAGCTAACTAGAAGTCTGGGTTCTGTCAGTTCCGCCTCGCAGTCAGTCGTGATAATCTACACAGGCGTCATACCAAAGAAAACATCGTGTCAAATCATCGGAACAGATCCTTGCTACTTAATGTGGGACCCGAAGTCCTCATAACCTGCTGTATCAACGGCCACCGCATTTCATCTAGCCATTAACCTATCGTCGTACATTGGGTACCTGAGGGATCACGATTGGACCGACGCCACTGGGTTCAGATTCGAGAAATGCAATCCTGGACAGCTAAATCCATTCCCCTCTTCGCCTCTTGGGTCCGGATTACATGTAAATCCGAAAGGCACGAGCCTGTCAACTCGTGACTTTGCATGTGCGCTGCGCGAAAATGTTTGGGGCGTCAGCTGTAATTAACGGCGCTTGTCACATCGAAACTGGCCACTAGGTTACCACTTCCTAGCCAAATCTACGCTGGTGGGATCGTGTAGCGTTAATTCCTAGGTGGTACGTGTGACCTGGTACGCAAAAACCCGCTACCCAACGATGCGCGAATCTAATTGTCTATGGTGGTGCCTCCGGATTATTGGTACAGGGTATAAACGAATCTTTAATGAAAGACCAAGTGCTAATACATACATGCCTCGCATAGGGGTGCGCCAGGTGTTAGTACTTCTGAAGTCGTCATAAATTATTCTGCAAGTAGAGGGTCCATGTCCAAGTAAATATGGGTTGTCCCTTGAGATTTAGCTTTGAGATCGGGAGGGGTAAGTAAGGCAGGTCCCGGTTTGGCAGTGACCAACTCGACAGAA"
Pattern = "A"
result = CountDNAntBiopython(Genome, Pattern)
print(f"Pattern '{Pattern}' occurs {result} times (Biopython).")
