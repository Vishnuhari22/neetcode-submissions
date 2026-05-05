class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numsUnique = new HashSet<Integer>();
        for (int num: nums) {
            numsUnique.add(num);
        }
        if(numsUnique.size() == nums.length){
            return false;
        } else{
            return true;
        }
    }
}