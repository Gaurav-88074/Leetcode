class Solution {
    int[][] dp;

    public int maximumScore(int[] nums, int[] multipliers) {
        int m = multipliers.length;
        dp = new int[m][m];

        return help(0, multipliers, nums, 0);
    }

    public int help(int i, int[] mul, int[] nums, int start) {
        if (i == mul.length) return 0;

        if (dp[i][start] != 0) return dp[i][start];

        int end = nums.length - (i - start) - 1;

        int option1 = mul[i] * nums[start] + help(i + 1, mul, nums, start + 1);
        int option2 = mul[i] * nums[end] + help(i + 1, mul, nums, start);

        return dp[i][start] = Math.max(option1, option2);
    }
}