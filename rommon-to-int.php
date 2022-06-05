<?php 

class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        $rommon_array = array(
        'I' => 1,
        'V'=> 5,
        "X" => 10,
        "L" => 50,
        "C" => 100,
        "D" => 500,
        "M" => 1000,
        "v"=> 4,
        "x" => 9,
        "l" => 40,
        "c" => 90,
        "d" => 400,
        "m" => 900);
       $rommon_others = array(
           "IV" => 'v',
           "IX" => 'x',
           "XL" => 'l',
           "XC" => 'c',
           "CD" => 'd',
           "CM" => 'm'
       );
       foreach ( $rommon_others as $k => $v) {
           $s = str_replace($k, $v, $s);
       }
       $rommon_string = str_split($s,1);
       $integer_num = 0;
       for($i= 0; $i< strlen($s);$i++){
           $integer_num += $rommon_array[$rommon_string[$i]];
       }
       return $integer_num;
    }
}
?>
