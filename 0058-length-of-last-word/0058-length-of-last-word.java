class Solution {
    public int lengthOfLastWord(String s) {
        int n = s.split(" ").length;
        System.out.println(n);
        String arr[] = new String[n];
        arr = s.split(" ");
        return arr[n-1].length(); 
    }
}