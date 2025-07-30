// Last updated: 7/30/2025, 12:22:22 PM
class Solution {
    public char kthCharacter(int k) {
        return (char)('a' + Integer.bitCount(k-1));
    }
}