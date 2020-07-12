impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = Vec::new();
        Self::helper(0usize, nums.clone(), &mut Vec::new(), nums.len(), &mut ans);
        ans
    }
    fn helper(index: usize, nums: Vec<i32>, res_item: &mut Vec<i32>, length: usize, ans: &mut Vec<Vec<i32>>) {
        if res_item.len() == length {
            ans.push(res_item.clone());
            return;
        }
        for i in 0..nums.len() {
            res_item.push(nums[i]);
            let (mut tmp1, mut tmp2) = (nums[..i].to_vec(), nums[i + 1..].to_vec());
            tmp1.append(&mut tmp2);
            Self::helper(i, tmp1, res_item, length, ans);
            res_item.pop();
        }
    }
}