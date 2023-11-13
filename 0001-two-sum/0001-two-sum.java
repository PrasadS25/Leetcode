import java.util.HashMap;
class Solution {
    
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int diff;
        int size = nums.length;
        int num;
        int[] answer = new int[2];
        for(int i=0;i<size;i++){
            num = nums[i];
            diff = target - num;
            if(map.containsKey(diff)){
                answer[0] = map.get(diff);
                answer[1] = i;
                return answer;
            }
            map.put(num,i);
        }  
        return answer;  
    }
}