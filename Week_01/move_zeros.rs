impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut zero_index = 0;
        for i in 0..nums.len() {
            if (nums[i] != 0) {
                nums[zero_index] = nums[i];
                if (zero_index != i) {
                    nums[i] = 0;
                }
                zero_index += 1;
            }
        }
    }
}