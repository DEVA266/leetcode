// Last updated: 7/30/2025, 12:23:26 PM
class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        int dx1=points[1][0]-points[0][0],dy1=points[1][1]-points[0][1],dx2=points[2][0]-points[1][0],dy2=points[2][1]-points[1][1];
        return dx1*dy2!=dx2*dy1;
    }
};