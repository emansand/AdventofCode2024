import re
from pathlib import Path

VALID = ["0","1","2","3","4","5","6","7","8","9",
         "zero","one","two","three","four","five","six","seven","eight","nine"]

CONVERT = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
CONVERT.update({num:int(num) for num in ["0","1","2","3","4","5","6","7","8","9"]})

input_file = Path("input.txt")

calibration_value = 0
with open(input_file) as open_file:
    for input in open_file:
        re_searches = [re.finditer(valid, input) for valid in VALID]

        searches = {s.start():s for s_iter in re_searches for s in s_iter if s}

        search_idx = sorted(searches.keys())

        i = search_idx[0]
        f = search_idx[-1]

        i_num = searches[i].group()
        f_num = searches[f].group()

        calibration_value += 10 * CONVERT[i_num] + CONVERT[f_num]
  
print(calibration_value)
