// Last updated: 7/30/2025, 3:38:53 PM
class Solution {
    public boolean checkIfPangram(String sentence) {
        char ch = 'a';
        while(ch<=122){
            if(!sentence.contains(String.valueOf(ch))) return false;
            ch++;
        }
        return true;
    }
}