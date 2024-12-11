#########################################################

#A bird is standing at a specific position in a one-dimensional array Arr. The array represents different locations, each holding a certain number of sticks. The bird needs to collect sticks to build a nest, and the goal is for the bird to collect at least 100 sticks.
#Rules:
#The bird can move left or right from its initial position to collect sticks.
#The bird alternates between moving left and right:
#First, it moves left, then right, and repeats this pattern.
#If the bird moves to a position where the number of sticks is 0, it skips that position and continues moving in the same direction until it finds a non-zero position or moves out of bounds.
#Once the bird reaches a position with sticks, it collects all the sticks from that position and marks the position as "collected" (i.e., the number of sticks at that position becomes 0).
#The bird stops collecting as soon as it gathers at least 100 sticks.

####################################################################

def solution(Arr, bird_pos):
    pls = []  # List to store positions where sticks are collected
    sticks_collected = Arr[bird_pos]  # Initialize with the sticks at the starting position
    
    while sticks_collected < 100:
        l = bird_pos - 1
        r = bird_pos + 1
        
        # Move left until a non-zero position is found or out of bounds
        while l >= 0 and Arr[l] == 0:
            l -= 1
            if l < 0:
                break
        
        if l >= 0 and sticks_collected < 100:  # Ensure `l` is within bounds and we haven't collected 100 sticks
            sticks_collected += Arr[l]  # Collect sticks
            Arr[l] = 0  # Set the position to 0 after collecting
            pls.append(l)  # Record the position

        # Move right until a non-zero position is found or out of bounds
        while r < len(Arr) and Arr[r] == 0:
            r += 1
            if r >= len(Arr):
                break
        
        if r < len(Arr) and sticks_collected < 100:  # Ensure `r` is within bounds and we haven't collected 100 sticks
            sticks_collected += Arr[r]  # Collect sticks
            Arr[r] = 0  # Set the position to 0 after collecting
            pls.append(r)  # Record the position

    return pls
