"""
Solution for Marisa's Fence Problem

Problem: Given n wooden boards with beauty values A_i (fence) and B_i (door),
for each k from 1 to n, find the maximum total beauty when selecting k boards
where k-1 boards are used for fence (beauty A_i) and 1 board for door (beauty B_i).

Algorithm:
1. For each k from 1 to n:
   2. Try each board as the door (use B_i value)
   3. From remaining boards, select top k-1 boards for fence (use A_i values)
   4. Calculate total beauty and keep maximum

Time Complexity: O(n^3) due to sorting for each door choice
Space Complexity: O(n) for storing fence values
"""

def solve():
    # Read input
    n = int(input())
    A = list(map(int, input().split()))  # Beauty values for fence
    B = list(map(int, input().split()))  # Beauty values for door
    
    results = []
    
    # For each possible number of boards k
    for k in range(1, n + 1):
        max_beauty = float('-inf')
        
        # Try each board as the door
        for door_idx in range(n):
            door_beauty = B[door_idx]
            
            # Collect fence values from all other boards
            fence_values = []
            for i in range(n):
                if i != door_idx:
                    fence_values.append(A[i])
            
            # Check if we have enough boards for fence
            if len(fence_values) < k - 1:
                continue
            
            # Sort fence values in descending order and take top k-1
            fence_values.sort(reverse=True)
            fence_sum = sum(fence_values[:k-1])
            
            # Calculate total beauty
            total_beauty = door_beauty + fence_sum
            max_beauty = max(max_beauty, total_beauty)
        
        results.append(max_beauty)
    
    # Output results
    print(*results)

if __name__ == "__main__":
    solve()