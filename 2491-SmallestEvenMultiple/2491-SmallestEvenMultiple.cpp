// Last updated: 7/30/2025, 12:22:37 PM
class Solution {
public:
    int smallestEvenMultiple(int n) {
        return (n & 1) ? 2 * n : n;
    }
};