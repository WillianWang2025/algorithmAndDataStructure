"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）
输入: N = 332
输出: 299
输入: N = 1234
输出: 1234

"""


class Solution:
    # 1、把数字N变成list，从右往左遍历，用一个[]存结果res；
    # 2、如果当前元素大于或等于前一个元素，则将当前元素加入res；否则把刚刚加入res的所有值全变成'9'，并将前一个元素减1；
    # 3、最后考虑第一个元素是否为0，不为0，则加入res，返回res的逆序。
    #
    # 作者：leaf_ye
    # 链接：https://leetcode-cn.com/problems/monotone-increasing-digits/solution/99-by-leaf_ye-ecf4/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def monotoneIncreasingDigits(self, N):
        list_n = list(str(N))
        r = len(list_n) - 1
        res = []
        while r - 1 >= 0:
            if list_n[r] >= list_n[r - 1]:
                res.append(list_n[r])
            else:
                list_n[r - 1] = str(int(list_n[r - 1]) - 1)
                res = ['9'] * (len(res) + 1)
            r -= 1
        if list_n[r] != '0':
            res.append(list_n[r])
        return int(''.join(res[::-1]))

    """
        网上看到的好的解法
        这是一道很明显的贪心题目。既然要尽可能的大，那么这个数从高位开始要尽可能地保持不变。那么我们找到从高到低第一个满足 str[i] > str[i+1]str[i]>str[i+1] 的位置，然后把 str[i] - 1str[i]−1 ，再把后面的位置都变成 99 即可。对应可看下面的例子。
    n   = 1234321
    res = 1233999
    但是由于减小了 str[i]str[i] 以后，可能不满足 str[i-1] <= str[i]str[i−1]<=str[i] 了，所以我们在分析下这种情况怎么处理。我们看下这种情况的例子：
    
    n    = 2333332
    res  = 2299999
    下面这段比较啰嗦，其实你看了上面的例子你就知道怎么写了。
    注意到如果减小 str[i]str[i] 以后不满足 str[i-1] <= str[i]str[i−1]<=str[i]，那么肯定有 str[i-1] == str[i]str[i−1]==str[i]，
    此时就需要再 str[i-1] - 1str[i−1]−1，递归地会处理到某个位置 idxidx，我们发现 str[idx] == str[idx + 1] == ... = str[i]str[idx]==str[idx+1]==...=str[i] 。
    然后只要str[idx] - 1str[idx]−1，然后后面都补上 99 即可。
    
    所以代码写起来很简单了。遍历各位数字的时候，求当前最大的数字 max。然后只在 max < arr[i]max<arr[i] 的时候才更新 max 对应的 idx
    （写法类似于查找数组中最大的元素，返回最小的下标）。接着判断是否有 arr[i] > arr[i + 1]arr[i]>arr[i+1]，如果是，那么 idx 位置数字减 11，后面的位置全部置 99 即可。
    """

    def monotoneIncreasingDigits2(self, N):
        arr = list(str(N))
        max_value = -1
        idx = -1
        for i in range(len(arr)-1):
            if max_value < int(arr[i]):
                max_value = int(arr[i])
                idx = i
            if arr[i]>arr[i+1]:
                arr[idx] = str(int(arr[idx])-1)
                for j in range(idx+1,len(arr)):
                    arr[j] ='9'
                break
        print(arr)
        return int(''.join(arr[:]))


    ## 思路：每次从右往左便历，遇到第一处递增就停下，然后将前一位减1，后面所有位置为9；循环往复，直到序列从左到右是递增的。
    def monotoneIncreasingDigits3(self, N):

        N = list(map(int, str(N)))
        i = len(N) - 1
        while i >= 1:
            if N[i - 1] > N[i]:
                N[i - 1] = N[i - 1] - 1
                N[i] = 9
                while i + 1 < len(N):
                    N[i + 1] = 9
                    i = i + 1
                i = len(N) - 1
            else:
                i = i - 1

        return int(''.join(map(str, N)))


if __name__ == '__main__':
    print("start to work")
    aa = Solution()
    print(aa.monotoneIncreasingDigits3(120))

