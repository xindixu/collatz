from Collatz import collatz_eval_cache
import json

cache = []

def generate_input():
    for i in range(1,1000000-1000,1000):
        (max_cyc_len, num_gen_max_cyc) = collatz_eval_cache(i,i+1000);
        cache.append((max_cyc_len, num_gen_max_cyc))

def write():
    with open('cache.txt','w') as file:
        json.dump(cache,file)



if __name__ == "__main__":
    generate_input()
    write()
