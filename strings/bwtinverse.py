def inverse_BWT(bwt):
    len_of_str = len(bwt)
    bwt_list = [(i, bwt[i]) for i in range(len_of_str)]
    sorted_bwt_list = sorted(bwt_list, key=lambda b: b[1])
    reconstruct = {sorted_bwt_list[i]: bwt_list[i] for i in range(len_of_str)}
    
    dollar_index = bwt.index('$')
    string = '$'
    temp = reconstruct[(dollar_index, '$')]
    while temp != (dollar_index, '$'):
        string += temp[1]
        temp = reconstruct[temp]
    
    return string[::-1]


bwt = input()
print(inverse_BWT(bwt))
