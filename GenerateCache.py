from Collatz import collatz_eval_cache
import json

cache = []

def generate_input():
    # cache structure: [max_cyc_len,num_gen_max_cyc]
    # index 0, 1 for [1-1000]; index 2, 3 for [1001,2000]
    for i in range(1,1000000-1000,1000):
        (max_cyc_len, num_gen_max_cyc) = collatz_eval_cache(i,i+999);
        cache.append(max_cyc_len)
        cache.append(num_gen_max_cyc)

def write():
    with open('cache.txt','w') as file:
        json.dump(cache,file)


if __name__ == "__main__":
    generate_input()
    write()
