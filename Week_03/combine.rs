impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        Self::helper(1, n, k, &mut Vec::new(), &mut res);
        res
    }
    fn helper(start: i32, n: i32, k: i32, res_item: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        if res_item.len() as i32 == k {
            res.push(res_item.clone());
            return;
        }
        for i in start..n - k + res_item.len() as i32 + 2 {
            res_item.push(i);
            Self::helper(i + 1, n, k, res_item, res);
            res_item.pop();
        }
    }
}