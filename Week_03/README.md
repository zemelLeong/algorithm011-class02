学习笔记

# 分治代码模板
```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
    print_result 
    return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)

  # revert the current level states
```

# 体会
这节课做的题，感觉最主要的特征是凑结果，例如：
```rust
fn helper(start: i32, n: i32, k: i32, res_item: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
    if res_item.len() as i32 == k {
        res.push(res_item.clone());
        return;
    }
    ...
}
```

需要的子结果凑出来了，就停止。