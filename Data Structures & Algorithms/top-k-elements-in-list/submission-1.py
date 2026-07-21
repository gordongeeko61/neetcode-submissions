from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr=Counter(nums)
        top_k_items = [item for item, count in ctr.most_common(k)]
        return top_k_items
