// 1.CONTAINS DUPLICATE
// [1,2,3,1]
// true.
//[1,2,3,4]
// false.
import java.util.*;
class Solution1A{
    public boolean containsDuplicate(int[] nums){
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]==nums[j]) return true;
            }
        }
        return false;
    }
}
class Solution1B{
    public boolean containsDuplicate(int[] nums){
        Set<Integer> set = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(set.contains(nums[i])) return true;
        }
        return false;
    }
}
class Solution1C{
    public boolean containsDuplicate(int[] nums){
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i++){
            if(nums[i]==nums[i+1]) return true;
        }
        return false;
    }
}
class Solution1D{
    public boolean containsDuplicate(int[]nums){
        Set<Integer> set = new HashSet<>();
        for(int n:nums){
            if(set.contains(n)) return true;
        }
        return false;
    }
}
class Solution1E{
    public boolean containsDuplicate(int[] nums){
        Map<Integer,Integer> map = new HashMap<>();
        for(int n: nums){
            if(map.containsKey(n)) return true;
        }
        return false;
    }
}
// 2. Valid Anagram
// s= "anagram" t= "nagnram"
// true
// s = "rat" t = "car"
// false
class Solution2A{
    public boolean isAnagram(String s, String t){
        if(s.length()!=t.length()) return false;
        for(char c : s.toCharArray()){
            boolean contains= false;
            for(char d : t.toCharArray()){
                if(c==d) contains = true;
            }
            if(contains == false) return false;
        }
        return true;
    }
}
class Solution2B{
    public boolean isAnagram(String s, String t){
        if(s.length()!=t.length()) return false;
        int[] freq = new int[26];
        for(int i=0;i<s.length();i++){
            freq[s.charAt(i)-'a']++;
            freq[t.charAt(i)-'a']--;
        }
        for(int n:freq){
            if (n>0) return false;
        }
        return true;
    }
}
class Solution2C{
    public boolean isAnagram(String s, String t){
        if(s.length()!=t.length()) return false;
        char[] a = s.toCharArray();
        char[] b = t.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a,b);
    }
}
// 3.Two SUM
// nums = [9,8,7,6] T = 13
// [2,3]
class Solution3A{
    public int[] twoSum(int[] nums, int target){
        for(int i = 0; i< nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                if(nums[i]+nums[j]==target) return new int[] {i,j};
            }
        }
        return new int[] {};
    }
}
class Solution3B{
    public int[] twoSum(int[] nums, int target){
        Map<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int compliment = target - nums[i];
            if(map.containsKey(compliment)) return new int[] {map.get(compliment),i};
            map.put(nums[i],i);
        }
        return new int[] {};
    }
}
class Solution3C{
    public boolean twoSum(int[] nums, int target){
        Arrays.sort(nums);
        int l=0,r=nums.length;
        while(l<r){
            if(nums[l]+nums[r]==target) return true;
            if(nums[l]+nums[r]>target) r--;
            else l++;
        }
        return false;
    }
}
class Solution3D{
    public int[] twoSum(int[] nums, int target){
        int[][] newNums = new int[nums.length][2];
        for(int i=0; i<nums.length; i++){
            newNums[i][0]=nums[i];
            newNums[i][1]=i;
        }
        Arrays.sort(newNums, (a, b) -> a[0] - b[0]);
        int l=0,r=nums.length-1;
        while(l<r){
            if(newNums[l][0]+newNums[r][0]==target) return new int[] {newNums[l][1],newNums[r][1]};
            if(newNums[l][0]+newNums[r][0]>target) r--;
            else l++;

        }
        return new int[] {};
    }
}
// 4. GROUP ANAGRAMS
// strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
// [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
// strs = [""]
// [[""]]
// strs = ["a"]
// [["a"]]
class Solution4A{
    public List<List<String>> groupAnagrams(String[] stars){
        Map<String,List<String>> map = new HashMap<>();
        for(String s: stars){
            char[] c = s.toCharArray();
            Arrays.sort(c);
            String ss = new String(c);
            if(!map.containsKey(ss)){
                map.put(ss,new ArrayList<>());
            }
            else{
                map.get(ss).add(s);
            }
        }
        return new ArrayList<>(map.values());
    }
}