alphafreq = ["b" , ["d",]*4 , ["f",]*2 , ["g",]*2 , ["h",]*6 , "j"   , "k"   ,
            ["l",]*4  , ["m",]*2 , ["n",]*7,["p",]*2 , "q"   , ["r",]*6 ,
            ["s",]*6  , ["t",]*9, "v"   , ["w",]*2 , "x"   , ["y",]*2 , "z"]

import itertools
print(list(itertools.chain.from_iterable(alphafreq)))
