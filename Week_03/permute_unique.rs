use std::collections::HashSet;

impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = Vec::new();
        Self::helper(&nums, &mut Vec::new(), nums.len(), &mut ans);
        ans
    }
    fn helper(nums: &Vec<i32>, res_item: &mut Vec<i32>, length: usize, ans: &mut Vec<Vec<i32>>) {
        let mut cache: HashSet<i32> = HashSet::new();
        if res_item.len() == length {
            ans.push(res_item.clone());
            return;
        }
        for i in 0..nums.len() {
            if cache.contains(&nums[i]) {continue;}
            cache.insert(nums[i]);
            res_item.push(nums[i]);
            let mut tmp = Vec::with_capacity(nums.len() - 1);
            tmp.extend_from_slice(&nums[..i]);
            tmp.extend_from_slice(&nums[i + 1..]);
            Self::helper(&tmp, res_item, length, ans);
            res_item.pop();
        }
    }
}