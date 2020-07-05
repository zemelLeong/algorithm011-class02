use std::collections::HashMap;
use std::collections::BinaryHeap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        for i in nums {
            let value = map.entry(i).or_insert(0);
            *value += 1;
        }
        let mut heap = BinaryHeap::from(map.iter()
            .map(|(key, value)| {(*value, *key)}).collect::<Vec<(i32, i32)>>());
        let mut ans: Vec<i32> = Vec::new();
        for _ in 0..k as usize {
            ans.push(heap.pop().unwrap().1);
        }
        ans
    }
}