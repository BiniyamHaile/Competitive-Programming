class Solution {
    public int maxArea(int[] height) {
        int left_idx = 0;
        int right_idx = height.length-1;
        int Areamax = 0;
        while(left_idx < right_idx){
            Areamax = ( Math.max (Areamax , Math.min( height[left_idx]  , height[right_idx]) * (right_idx -left_idx))  );
            if(height[right_idx] > height[left_idx]){
                left_idx +=1;
            }
            else{
                right_idx -=1;
            }
           
        }
  return Areamax;
    }
}
