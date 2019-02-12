
import json

cache = []

# ------------------------
# collatz_eval_cache
# use for generating cache
# ------------------------

def collatz_eval_cache(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # pre-condition
    assert isinstance(i, int), "argument(s) is not an int"
    assert isinstance(j, int), "argument(s) is not an int"

    if i > j:
        assert j > 0, "argument(s) out of range"
        assert i <= 1000000, "argument(s) out of range"
        r = range(j, i+1)
    else:
        assert i > 0, "argument(s) out of range"
        assert j <= 1000000, "argument(s) out of range"
        r = range(i, j+1)

    max_cyc_len = 0
    num_gen_max_cyc = 1

    for i in r:
        cyc_len = 1
        ori_num = i
        while i > 1:
            if i % 2 == 0:
                i = i >> 1
            else:
                i = 3 * i + 1
            cyc_len += 1;
        if max_cyc_len < cyc_len:
            max_cyc_len = cyc_len
            num_gen_max_cyc = ori_num

    # post-condition
    assert max_cyc_len >= cyc_len, "max_cyc_len is less than one cyc_len"
    assert max_cyc_len >= 1, "max_cyc_len is less than 1"

    return max_cyc_len, num_gen_max_cyc


def generate_input():
    '''
    cache structure: [max_cyc_len,num_gen_max_cyc]
    index 0, 1 for [1,   1000]
    index 2, 3 for [1001,2000]
    index 4, 5 for [2001,3000]
    index 6, 7 for [3001,4000]
    '''

    for i in range(1,1000000+1,1000):
        (max_cyc_len, num_gen_max_cyc) = collatz_eval_cache(i,i+999);
        cache.append(max_cyc_len)
        cache.append(num_gen_max_cyc)

def write():
    with open('cache.txt','w') as file:
        json.dump(cache,file)


if __name__ == "__main__":
    generate_input()
    write()
