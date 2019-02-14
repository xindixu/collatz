#!/usr/bin/env python3

# ---------------------------
# Original:
#       projects/collatz/Collatz.py
#       Copyright (C) 2016
#       Glenn P. Downing
#
# Project 1:
#       CS 329E Software Engineering
#       Xindi Xu (xx2673)
# ---------------------------

cache = [179, 871, 182, 1161, 217, 2919, 238, 3711, 215, 4379, 236, 5567, 262, 6171, 252, 7963, 247, 8959, 260, 9257, 268, 10971, 250, 11945, 263, 12342, 276, 13255, 271, 14695, 271, 15039, 266, 16457, 279, 17647, 261, 18514, 274, 19593, 256, 20830, 269, 21942, 269, 22043, 282, 23529, 264, 24684, 264, 25166, 308, 26623, 259, 27135, 259, 28313, 272, 29257, 272, 30078, 285, 31419, 267, 32415, 267, 33019, 311, 34239, 324, 35655, 249, 36031, 306, 37503, 244, 38075, 306, 39935, 288, 40959, 257, 41641, 288, 42249, 270, 43884, 270, 44025, 314, 45127, 283, 46443, 314, 47329, 296, 48927, 296, 49575, 278, 50815, 309, 51359, 340, 52527, 322, 53483, 260, 54270, 260, 55275, 322, 56095, 304, 57115, 273, 58513, 304, 59903, 335, 60975, 317, 61999, 286, 62745, 330, 63387, 299, 64255, 268, 65511, 268, 66038, 312, 67691, 312, 68187, 299, 69535, 312, 70335, 325, 71310, 263, 72361, 294, 73063, 325, 74791, 307, 75006, 307, 76153, 351, 77031, 338, 78791, 307, 79131, 320, 80225, 320, 81159, 320, 82665, 289, 83503, 320, 84143, 302, 85673, 302, 86175, 333, 87087, 333, 88059, 315, 89119, 315, 90254, 333, 91463, 315, 92999, 284, 93345, 315, 94658, 328, 95081, 297, 96383, 297, 97417, 284, 98971, 328, 99067, 341, 100167, 310, 101537, 310, 102281, 248, 103666, 310, 104617, 341, 105054, 354, 106239, 292, 107065, 279, 108009, 310, 109881, 292, 110087, 323, 111451, 323, 112187, 292, 113511, 305, 114230, 349, 115547, 305, 116551, 305, 117511, 336, 118187, 305, 119017, 318, 120338, 336, 121950, 318, 122815, 331, 123391, 287, 124327, 318, 125383, 331, 126774, 287, 127097, 331, 128251, 344, 129991, 331, 130631, 300, 131103, 331, 132089, 313, 133345, 300, 134783, 344, 135111, 313, 136374, 331, 137195, 313, 138351, 313, 139489, 344, 140073, 326, 141759, 375, 142587, 282, 143007, 326, 144283, 295, 145633, 357, 146599, 295, 147510, 326, 148601, 326, 149582, 370, 150015, 295, 151634, 308, 152306, 308, 153422, 352, 154062, 308, 155401, 383, 156159, 339, 157582, 321, 158433, 352, 159359, 370, 160411, 290, 161895, 339, 162601, 321, 163753, 334, 164521, 321, 165330, 352, 166011, 321, 167177, 321, 168281, 334, 169033, 290, 170031, 334, 171001, 303, 172350, 347, 173321, 334, 174174, 272, 175531, 334, 176118, 334, 177281, 347, 178075, 303, 179375, 365, 180463, 316, 181833, 334, 182926, 254, 183166, 316, 184155, 329, 185087, 347, 186763, 329, 187303, 316, 188075, 360, 189855, 329, 190161, 329, 191559, 347, 192711, 329, 193115, 342, 194987, 360, 195465, 298, 196655, 285, 197942, 329, 198134, 329, 199442, 342, 200334, 311, 201819, 342, 202471, 311, 203074, 311, 204267, 355, 205417, 373, 206847, 311, 207175, 311, 208623, 311, 209223, 342, 210108, 355, 211051, 355, 212478, 373, 213881, 293, 214130, 280, 215177, 386, 216367, 324, 217255, 324, 218337, 355, 219899, 324, 220441, 355, 221353, 324, 222902, 324, 223339, 324, 224374, 368, 225023, 368, 226587, 306, 227047, 355, 228399, 306, 229791, 443, 230631, 350, 231094, 337, 232233, 368, 233191, 381, 234239, 306, 235022, 337, 236374, 350, 237433, 306, 238034, 350, 239039, 368, 240617, 275, 241289, 319, 242443, 337, 243900, 275, 244911, 319, 245630, 332, 246782, 350, 247387, 288, 248654, 350, 249017, 332, 250363, 319, 251257, 319, 252420, 332, 253548, 363, 254911, 288, 255047, 332, 256502, 345, 257001, 301, 258526, 345, 259982, 332, 260847, 332, 261262, 301, 262206, 407, 263103, 332, 264178, 332, 265922, 314, 266689, 345, 267113, 270, 268028, 345, 269083, 407, 270271, 283, 271012, 314, 272748, 358, 273889, 332, 274390, 345, 275239, 314, 276233, 389, 277615, 345, 278311, 314, 279023, 345, 280145, 358, 281401, 314, 282113, 358, 283305, 358, 284783, 376, 285174, 314, 286747, 327, 287339, 389, 288489, 345, 289067, 327, 290727, 327, 291047, 340, 292481, 358, 293198, 296, 294591, 358, 295131, 327, 296391, 327, 297202, 371, 298843, 327, 299164, 371, 300030, 296, 301265, 340, 302719, 340, 303707, 340, 304001, 265, 305035, 309, 306401, 309, 307887, 371, 308071, 340, 309643, 371, 310271, 309, 311291, 384, 312318, 340, 313099, 278, 314089, 340, 315164, 353, 316577, 309, 317378, 353, 318718, 322, 319467, 371, 320822, 353, 321003, 309, 322591, 322, 323199, 384, 324551, 340, 325201, 247, 326110, 322, 327387, 291, 328758, 353, 329151, 322, 330660, 291, 331538, 353, 332022, 335, 333817, 322, 334354, 322, 335009, 366, 336199, 366, 337535, 335, 338065, 366, 339881, 304, 340571, 335, 341671, 353, 342599, 335, 343314, 304, 344687, 441, 345947, 348, 346642, 322, 347278, 335, 348348, 366, 349787, 304, 350203, 379, 351359, 335, 352236, 304, 353065, 348, 354303, 379, 355143, 348, 356150, 304, 357052, 379, 358063, 348, 359967, 410, 360361, 348, 361129, 361, 362343, 317, 363665, 317, 364862, 361, 365185, 348, 366985, 286, 367359, 317, 368310, 361, 369567, 392, 370153, 348, 371081, 317, 372030, 348, 373526, 330, 374606, 361, 375201, 423, 376603, 361, 377739, 330, 378025, 361, 379207, 379, 380233, 374, 381727, 361, 382367, 330, 383118, 330, 384447, 348, 385422, 330, 386230, 299, 387753, 330, 388062, 436, 389191, 361, 390930, 330, 391271, 299, 392135, 361, 393511, 405, 394655, 312, 395263, 330, 396268, 330, 397046, 374, 398457, 299, 399054, 374, 400041, 387, 401151, 268, 402044, 343, 403625, 343, 404942, 405, 405407, 361, 406043, 268, 407177, 312, 408534, 312, 409124, 449, 410011, 330, 411586, 343, 412857, 374, 413694, 374, 414561, 312, 415054, 387, 416423, 343, 417465, 343, 418431, 281, 419503, 343, 420216, 325, 421433, 356, 422102, 418, 423679, 356, 424956, 356, 425503, 356, 426651, 374, 427762, 294, 428260, 281, 429019, 312, 430121, 343, 431899, 387, 432734, 343, 433601, 356, 434919, 281, 435995, 325, 436091, 387, 437247, 400, 438699, 356, 439798, 325, 440859, 294, 441887, 356, 442697, 338, 443977, 325, 444587, 338, 445089, 325, 446678, 325, 447801, 369, 448265, 369, 449479, 387, 450651, 307, 451169, 294, 452777, 369, 453174, 338, 454079, 338, 455561, 356, 456798, 338, 457753, 307, 458281, 307, 459559, 307, 460007, 444, 461262, 369, 462107, 325, 463036, 338, 464415, 369, 465407, 369, 466382, 413, 467739, 382, 468478, 338, 469649, 307, 470044, 276, 471134, 338, 472748, 307, 473086, 382, 474121, 320, 475300, 307, 476068, 382, 477417, 351, 478078, 351, 479931, 413, 480481, 382, 481959, 351, 482239, 307, 483887, 320, 484615, 338, 485887, 382, 486827, 382, 487039, 382, 488127, 351, 489313, 320, 490431, 320, 491081, 426, 492571, 395, 493537, 351, 494774, 320, 495195, 320, 496041, 289, 497308, 351, 498034, 395, 499647, 364, 500271, 320, 501063, 426, 502137, 320, 503777,
         364, 504299, 364, 505609, 382, 506977, 364, 507903, 377, 508969, 364, 509822, 333, 510825, 470, 511935, 333, 512507, 351, 513897, 364, 514671, 395, 515239, 302, 516903, 333, 517417, 439, 518921, 364, 519871, 333, 520683, 364, 521241, 333, 522524, 302, 523903, 364, 524681, 408, 525543, 408, 526206, 377, 527039, 377, 528895, 333, 529394, 346, 530943, 346, 531455, 377, 532715, 377, 533387, 346, 534225, 302, 535580, 333, 536319, 377, 537095, 346, 538166, 346, 539922, 408, 540542, 364, 541390, 346, 542521, 359, 543515, 315, 544713, 346, 545607, 452, 546681, 377, 547681, 333, 548780, 315, 549804, 346, 550478, 377, 551593, 315, 552466, 346, 553631, 421, 554143, 390, 555230, 346, 556622, 315, 557089, 315, 558046, 284, 559337, 359, 560295, 328, 561910, 359, 562802, 328, 563318, 421, 564905, 328, 565151, 359, 566609, 359, 567337, 359, 568807, 359, 569566, 377, 570348, 359, 571551, 372, 572591, 359, 573551, 328, 574678, 346, 575865, 390, 576978, 390, 577230, 346, 578134, 359, 579007, 266, 580967, 328, 581454, 328, 582094, 434, 583787, 372, 584007, 359, 585327, 359, 586396, 328, 587841, 315, 588543, 297, 589182, 359, 590262, 403, 591983, 328, 592782, 328, 593023, 328, 594404, 328, 595570, 372, 596415, 372, 597686, 341, 598255, 372, 599305, 372, 600060, 403, 601327, 297, 602530, 297, 603702, 372, 604233, 341, 605438, 328, 606183, 341, 607414, 403, 608111, 359, 609063, 341, 610215, 354, 611455, 310, 612745, 310, 613319, 310, 614059, 447, 615017, 372, 616142, 372, 617767, 310, 618532, 341, 619286, 372, 620542, 372, 621842, 310, 622183, 354, 623643, 385, 624635, 354, 625206, 509, 626331, 341, 627647, 279, 628127, 279, 629255, 341, 630328, 310, 631161, 385, 632161, 354, 633154, 310, 634159, 416, 635519, 310, 636897, 354, 637436, 354, 638255, 354, 639913, 416, 640641, 372, 641644, 416, 642075, 279, 643436, 279, 644681, 310, 645182, 323, 646153, 341, 647849, 323, 648642, 385, 649051, 341, 650402, 336, 651335, 354, 652379, 385, 653739, 323, 654137, 385, 655871, 429, 656761, 354, 657903, 398, 658049, 354, 659698, 323, 660265, 323, 661281, 292, 662831, 292, 663076, 367, 664063, 442, 665215, 323, 666111, 367, 667375, 323, 668708, 336, 669921, 323, 670018, 323, 671023, 367, 672398, 336, 673115, 367, 674145, 385, 675969, 336, 676129, 336, 677865, 380, 678625, 367, 679762, 336, 680095, 336, 681099, 305, 682023, 380, 683947, 336, 684004, 354, 685195, 398, 686985, 380, 687871, 292, 688977, 336, 689131, 336, 690057, 442, 691894, 323, 692895, 367, 693161, 367, 694987, 336, 695593, 336, 696623, 318, 697371, 367, 698111, 367, 699574, 367, 700385, 411, 701607, 380, 702715, 349, 703358, 504, 704623, 380, 705193, 305, 706129, 349, 707995, 349, 708606, 336, 709124, 380, 710286, 380, 711182, 411, 712683, 380, 713575, 305, 714104, 305, 715433, 380, 716126, 349, 717118, 336, 718439, 349, 719897, 411, 720722, 367, 721852, 411, 722335, 349, 723359, 362, 724686, 305, 725831, 349, 726811, 318, 727199, 362, 728859, 318, 729705, 380, 730183, 336, 731704, 380, 732191, 349, 733927, 349, 734043, 424, 735679, 318, 736367, 380, 737371, 424, 738857, 424, 739143, 393, 740306, 318, 741231, 349, 742162, 318, 743531, 318, 744060, 349, 745711, 287, 746431, 362, 747519, 318, 748086, 393, 749227, 362, 750402, 331, 751090, 318, 752300, 424, 753206, 318, 754843, 362, 755478, 362, 756449, 331, 757167, 362, 758409, 362, 759420, 380, 760465, 362, 761855, 331, 762599, 375, 763454, 362, 764734, 331, 765567, 331, 766191, 468, 767903, 331, 768761, 393, 769305, 349, 770844, 344, 771004, 393, 772859, 362, 773247, 331, 774559, 437, 775035, 331, 776124, 393, 777327, 437, 778382, 362, 779742, 344, 780135, 362, 781860, 331, 782535, 331, 783739, 313, 784543, 375, 785691, 300, 786345, 362, 787017, 406, 788315, 406, 789310, 375, 790555, 344, 791279, 437, 792735, 375, 793343, 331, 794092, 331, 795295, 468, 796095, 344, 797183, 300, 798108, 375, 799023, 375, 800081, 406, 801769, 388, 802302, 300, 803372, 331, 804479, 375, 805643, 344, 806759, 406, 807327, 331, 808274, 344, 809884, 406, 810399, 287, 811241, 362, 812086, 375, 813307, 313, 814719, 357, 815273, 344, 816747, 344, 817663, 450, 818943, 357, 819967, 450, 820022, 375, 821522, 344, 822139, 375, 823689, 326, 824347, 344, 825627, 313, 826395, 419, 827503, 313, 828681, 375, 829119, 344, 830447, 419, 831215, 388, 832839, 357, 833609, 344, 834930, 313, 835633, 344, 836862, 525, 837799, 344, 838683, 388, 839547, 357, 840443, 313, 841041, 388, 842881, 331, 843129, 357, 844204, 401, 845223, 313, 846340, 419, 847358, 313, 848923, 357, 849912, 357, 850433, 357, 851006, 326, 852075, 357, 853211, 419, 854191, 388, 855583, 375, 856551, 357, 857313, 370, 858887, 313, 859135, 357, 860327, 326, 861537, 326, 862018, 344, 863798, 326, 864559, 388, 865401, 326, 866011, 344, 867202, 357, 868511, 388, 869467, 326, 870427, 432, 871915, 326, 872182, 326, 873033, 388, 874494, 432, 875681, 370, 876011, 401, 877398, 326, 878654, 357, 879596, 326, 880347, 326, 881707, 313, 882815, 370, 883903, 295, 884100, 370, 885417, 445, 886953, 401, 887975, 295, 888425, 370, 889371, 339, 890178, 326, 891608, 295, 892073, 326, 893356, 370, 894623, 326, 895602, 370, 896530, 339, 897383, 370, 898855, 295, 899070, 401, 900735, 401, 901991, 383, 902591, 295, 903792, 383, 904833, 295, 905554, 445, 906175, 326, 907129, 370, 908319, 326, 909275, 476, 910107, 383, 911929, 401, 912167, 357, 913593, 370, 914971, 339, 915323, 339, 916295, 383, 917161, 339, 918841, 432, 919791, 339, 920071, 339, 921447, 445, 922524, 308, 923239, 370, 924139, 339, 925659, 370, 926649, 476, 927003, 383, 928191, 339, 929081, 370, 930814, 308, 931382, 370, 932764, 370, 933846, 414, 934299, 414, 935478, 383, 936953, 352, 937810, 445, 938143, 507, 939497, 383, 940257, 339, 941145, 339, 942571, 352, 943899, 383, 944491, 352, 945403, 383, 946623, 383, 947049, 383, 948242, 352, 949732, 414, 950943, 383, 951433, 414, 952479, 414, 953279, 383, 954834, 339, 955657, 352, 956156, 352, 957383, 321, 958290, 352, 959862, 414, 960962, 352, 961145, 383, 962631, 414, 963113, 352, 964287, 321, 965595, 365, 966249, 308, 967215, 321, 968095, 352, 969081, 458, 970599, 352, 971247, 321, 972939, 383, 973577, 383, 974078, 339, 975600, 383, 976254, 334, 977003, 383, 978151, 334, 979547, 427, 980905, 321, 981206, 383, 982663, 383, 983161, 352, 984233, 427, 985142, 352, 986855, 396, 987074, 321, 988487, 352, 989547, 321, 990379, 321, 991374, 352, 992895, 290, 993183, 365, 994395, 365, 995967, 365, 996095, 440, 997823, 396, 998969, 396, 999294]

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read 2 ints as a string
    return a list of 2 ints, representing the beginning and end of a range, [i, j], inclusive
    """
    a = s.split()
    return [int(a[0]), int(a[1])]


# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]

    1. create range object and flip the args if needed
    2. for all numbers in the range:
    3. find the cycle length with:
        while i > 1:
            if odd:
                * 3 + 1
            else:
                >> 1
    3. save & update the max_cyc_len

    """
    # pre-condition
    assert isinstance(i, int), "argument(s) is not an int"
    assert isinstance(j, int), "argument(s) is not an int"

    if i > j:
        assert j > 0, "argument(s) out of range"
        assert i < 1000000, "argument(s) out of range"
        r = range(j, i+1)
    else:
        assert i > 0, "argument(s) out of range"
        assert j < 1000000, "argument(s) out of range"
        r = range(i, j+1)

    max_cyc_len = 0

    for i in r:
        cyc_len = 1
        while i > 1:
            if i % 2 == 0:
                i = i >> 1
            else:
                i = 3 * i + 1
            cyc_len += 1
        if max_cyc_len < cyc_len:
            max_cyc_len = cyc_len

    # post-condition
    assert max_cyc_len >= cyc_len, "max_cyc_len is less than one cyc_len"
    assert max_cyc_len >= 1, "max_cyc_len is less than 1"

    return max_cyc_len


# ------------------
# collatz_eval_use_cache
# ------------------

def collatz_eval_use_cache(i, j):
    """
    use cache to calculate

    if:
         abs(i-j) < 1000, use collatz_eval(i,j)
     else:
        1. compute the max_cyc_len in complete ranges
            1.1 compute lowest_complete_range_index & highest_complete_range_index
                (lowest & highest index for complete ranges)
                i.e. args 537 have indexs of 2, representing [1001,2000]
                     args 3099 have indexs of 4, representing [2001,3000]
            1.2 retrieve the max_cyc_len in these ranges and find maximum

        2. compute the max_cyc_len in incomplete ranges
            i.e. [537, 3099] has incomplete ranges of [537, 1000] and [3001,3099]
            2.1 compute indexs for number that generate the max_cyc_len in lower and upper incompelte ranges
                i.e. args 537 have indexs of 1, representing num_gen_max_cyc in [1,1000]
                     args 3099 have indexs of 7, representing num_gen_max_cyc in [3001,4000]
            2.2 for i (lower end):
                if num_gen_max_cyc is within [537,1000]:
                    save the number
                else:
                    use collatz_eval(537,1000)
            2.3 for j (upper end):
                if num_gen_max_cyc is within [3001,3099]:
                    save the number
                else:
                    use collatz_eval(3000,3099)

        3. find the maximum among max_cyc_len in complete ranges, lower incomplete range and upper incomplete range

    """

    # pre-condition
    assert isinstance(i, int), "argument(s) is not an int"
    assert isinstance(j, int), "argument(s) is not an int"

    if abs(i - j) < 1000:
        return collatz_eval(i, j)

    if i > j:
        assert j > 0, "argument(s) out of range"
        assert i < 1000000, "argument(s) out of range"
        lower_range = j
        upper_range = i
    else:
        assert i > 0, "argument(s) out of range"
        assert j < 1000000, "argument(s) out of range"
        lower_range = i
        upper_range = j

    # ---------------------------------------
    # find the max_cyc_len in cache in the complete ranges
    lowest_complete_range_index = lower_range // 1000 * 2 + 2
    highest_complete_range_index = upper_range // 1000 * 2 - 2

    # find the max_cyc_len in cache in the complete ranges
    max_cyc_len_in_cache = 0

    for k in range(lowest_complete_range_index, highest_complete_range_index+1, 2):
        if cache[k] > max_cyc_len_in_cache:
            max_cyc_len_in_cache = cache[k]

    # -----------------------------------------
    # find the max_cyc_len in cache in lower & upper incomplete ranges

    lower_num_with_max_cyc_len_index = lowest_complete_range_index - 1
    higher_num_with_max_cyc_len_index = highest_complete_range_index + 3

    # if the number produces the max_cyc_len is in the range of [lower_range,nearest 000]
    if cache[lower_num_with_max_cyc_len_index] >= lower_range:
        # get the max_cyc_len from cache
        max_cyc_len_lower = cache[lower_num_with_max_cyc_len_index-1]
    else:
        # caculate max_cyc_len in range
        max_cyc_len_lower = collatz_eval(
            lower_range, (lower_range//1000 * 1000 + 1000))

    # if the number produces the max_cyc_len is in the range of [nearest 000,upper_range]
    if cache[higher_num_with_max_cyc_len_index] <= upper_range:
        # get the max_cyc_len from cache
        max_cyc_len_upper = cache[higher_num_with_max_cyc_len_index-1]
    else:
        # caculate max_cyc_len in range
        max_cyc_len_upper = collatz_eval(
            upper_range, (upper_range//1000 * 1000))

    # find maximum number in max_cyc_len_in_cache, max_cyc_len_lower, max_cyc_len_upper
    if max_cyc_len_in_cache > max_cyc_len_lower:
        if max_cyc_len_in_cache > max_cyc_len_upper:
            return max_cyc_len_in_cache
        else:
            return max_cyc_len_upper
    else:
        if max_cyc_len_lower > max_cyc_len_upper:
            return max_cyc_len_lower
        else:
            return max_cyc_len_upper


# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print 3 ints: beginning & end of the range and result
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval_use_cache(i, j)
        collatz_print(w, i, j, v)


# ------------------------------------------------------------------------
# helper functions, do not call directly
# ------------------------------------------------------------------------

# ------------------------
# collatz_eval_cache
# ------------------------

def collatz_eval_cache(i, j):
    """
    helper function
    generate cache, same as collatz_eval() but return a tuple (max_cyc_len, num_gen_max_cyc)
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
            cyc_len += 1
        if max_cyc_len < cyc_len:
            max_cyc_len = cyc_len
            num_gen_max_cyc = ori_num

    # post-condition
    assert max_cyc_len >= cyc_len, "max_cyc_len is less than one cyc_len"
    assert max_cyc_len >= 1, "max_cyc_len is less than 1"

    return max_cyc_len, num_gen_max_cyc


# ------------------------
# generate_input
# ------------------------
def generate_cache():
    """
    cache:
    max_cyc_len: max cycle length in the ranges of 1000
    num_gen_max_cyc: number that generate the max cycle length

    structure: [max_cyc_len,num_gen_max_cyc]

    index 0, 1 for [1,   1000]
    index 2, 3 for [1001,2000]
    index 4, 5 for [2001,3000]
    index 6, 7 for [3001,4000]
    ...
    index 1998, 1999 for [999001,1000000]
    """

    for i in range(1, 1000000+1, 1000):
        (max_cyc_len, num_gen_max_cyc) = collatz_eval_cache(i, i+999)
        cache.append(max_cyc_len)
        cache.append(num_gen_max_cyc)
