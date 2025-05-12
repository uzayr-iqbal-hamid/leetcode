## Easy

1. Two Sum
<details>
  <summary>Code!</summary>
  ```java
HashMap<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];

        if (map.containsKey(complement)) {
            return new int[]{map.get(complement), i};
        }

        map.put(nums[i], i);
    }

return new int[0];
```  
</details>


Time Complexity:
```bash
O(N)
```
