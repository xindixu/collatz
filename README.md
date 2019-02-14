# Collatz 3n+1 Problem with Cache Optimization

## Description
See Sphere Online Judge for more detail
https://www.spoj.com/problems/PROBTNPO/

> Consider the following algorithm:
> 1. input n
> 2. print n
> 3. if n = 1 then STOP
> 		3.1 if n is odd then n = 3n + 1
> 		3.2 else n = n / 2
> 6. GOTO 2

> Sample Input:
1 10 <br>
100 200<br>
201 210<br>
900 1000<br>

> Sample Output:
1 10 20<br>
100 200 125<br>
201 210 89<br>
900 1000 174<br>


## Cache Optimization
use cache to calculate
### if:
   abs(i-j) < 1000, use collatz_eval(i,j)
### else:
#### 1. compute the max_cyc_len in complete ranges
##### 1.1 compute lowest_complete_range_index & highest_complete_range_index
        (lowest & highest index for complete ranges)
        i.e. args 537 have indexes of 2, representing [1001,2000]
             args 3099 have indexes of 4, representing [2001,3000]
##### 1.2 retrieve the max_cyc_len in these ranges and find maximum

#### 2. compute the max_cyc_len in incomplete ranges
    i.e. [537, 3099] has incomplete ranges of [537, 1000] and [3001,3099]
##### 2.1 compute indexes for number that generate the max_cyc_len in lower and upper incompelte ranges
        i.e. args 537 have indexes of 1, representing num_gen_max_cyc in [1,1000]
             args 3099 have indexes of 7, representing num_gen_max_cyc in [3001,4000]
##### 2.2 for i (lower end):
        if num_gen_max_cyc is within [537,1000]:
            save the number
        else:
            use collatz_eval(537,1000)
##### 2.3 for j (upper end):
        if num_gen_max_cyc is within [3001,3099]:
            save the number
        else:
            use collatz_eval(3000,3099)

#### 3. find the maximum among max_cyc_len in complete ranges, lower incomplete range and upper incomplete range

## Documentation
See Collatz.html for detailed interface doc
