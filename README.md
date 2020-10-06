## Code Challenge: Assign Cookies
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

**Note:** 
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.

#### Example 1:
```
Input: 
    children = [1, 2, 3]
    cookies = [1, 1]
Output: 1
Explanation: You have 3 children and 2 cookies. Even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content. 
```

#### Example 2:
```
Input: 
    children = [1, 2]
    cookies = [1, 2, 3]
Output: 2
```

Source: Leetcode