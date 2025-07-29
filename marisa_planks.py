def solve():
    """
    Marisa's Wooden Planks Problem
    
    For each k from 1 to n, find the maximum beauty when using k planks:
    - k-1 planks for fence (use A_i values)  
    - 1 plank for door (use B_i value)
    """
    n = int(input())
    A = list(map(int, input().split()))  # Beauty values for fence
    B = list(map(int, input().split()))  # Beauty values for door
    
    results = []
    
    for k in range(1, n + 1):
        if k == 1:
            # Only 1 plank, must be used for door
            max_beauty = max(B)
        else:
            # k-1 planks for fence, 1 plank for door
            max_beauty = 0
            
            # Try each plank as the door
            for door_idx in range(n):
                door_beauty = B[door_idx]
                
                # Get all A values except the one used for door
                fence_candidates = [A[i] for i in range(n) if i != door_idx]
                
                # Sort in descending order and take the best k-1
                fence_candidates.sort(reverse=True)
                fence_beauty = sum(fence_candidates[:k-1])
                
                total_beauty = door_beauty + fence_beauty
                max_beauty = max(max_beauty, total_beauty)
        
        results.append(max_beauty)
    
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    solve()