// Last updated: 7/31/2025, 2:03:36 PM
class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int index = (ruleKey.equals("type")) ? 0 : (ruleKey.equals("color")) ? 1 : 2;
        int out = 0;
        for(List<String> value : items){
            if(value.get(index).equals(ruleValue)) out++;
        }
        return out;
    }
}