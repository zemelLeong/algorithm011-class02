use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut ans: HashMap<Vec<u8>, Vec<String>> = HashMap::new();
        for item in strs {
            let mut i = item.as_bytes().to_vec();
            i.sort();
            let grouped_res = ans.entry(i).or_insert(Vec::new());
            grouped_res.push((*item).to_string());
        }
        ans.iter().map(|(_, value)| {value.clone()}).collect()
    }
}