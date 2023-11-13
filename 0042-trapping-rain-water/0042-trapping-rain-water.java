class Solution {
    public int trap(int[] height) {
        int size = height.length;
        int maxl=height[0],maxr = height[size-1];
        int l=0,r=size-1,sum=0;
        int add = 0;
        while(l<r){
            if(maxl<=maxr){
                l++;
                if(height[l]>maxl)
                    maxl = height[l];            
                sum += maxl - height[l];            
            }
            else{
                r--;
                if(height[r]>maxr)
                    maxr = height[r];                  
                sum += maxr - height[r];
                
            }
        }
        return sum;
    }
}