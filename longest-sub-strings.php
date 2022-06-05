<?php 

// vertical approach 

class Solution {

    /**
     * @param String[] $strs
     * @return String
     */
    function longestCommonPrefix($strs) {
        if( $strs == null || count($strs) == 0 ) return "";
        $split_str = str_split($strs[0],1);
        for($i =0; $i<strlen($strs[0]);$i++){
            
            $c = $split_str[$i];
            for($j=1; $j < count($strs); $j++){
                $split_other_str = str_split($strs[$j],1);
                if( $i == strlen($strs[$j]) || $split_other_str[$i] != $c){
                    return substr($strs[0],0,$i);
                }
            }
        }
        return $strs[0];
    }
}
?>
