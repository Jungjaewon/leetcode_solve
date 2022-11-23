class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        done, idx, steps = 0, 0, 0
        cur_cap, river = capacity, -1
        while done < len(plants):
            #print(f'done : {done}')
            s_idx, temp_sum = idx, plants[idx]
            while idx + 1 < len(plants) and temp_sum + plants[idx + 1] < cur_cap:
                temp_sum += plants[idx + 1]
                idx += 1
            
            #print(f'- s_idx : {s_idx}, idx : {idx}, temp_sum : {temp_sum}')
            done += abs(idx - s_idx + 1)
            steps += abs(idx - s_idx + 1)
            cur_cap -= temp_sum
            #print(f'- steps : {steps}, each step : {abs(idx - s_idx + 1)}, cur_cap : {cur_cap}')
            
            if idx + 1 < len(plants) and cur_cap < plants[idx + 1]:
                #print("* leak!!!!!")
                steps += abs(idx - river) + abs(idx - river)
                #print(f'* steps : {steps}, each step1 : {abs(idx - river)}, each step2 : {abs(idx - river)}')
                cur_cap = capacity            
            idx += 1
            
        return steps
        
        """
        steps, cur_cap, cur_pos = 0, capacity, -1
        done, target = 0, 0
        while done < len(plants):
            if cur_pos == -1: # river:
                cur_cap = capacity
                #print(f'steps abs(target - cur_pos) : {abs(target - cur_pos)}')
                steps += abs(target - cur_pos)
                cur_pos = target
                target += 1
                cur_cap -= plants[cur_pos]
                done += 1
            elif cur_pos < len(plants) and plants[cur_pos] <= cur_cap:
                cur_pos += 1
                steps += 1
                target += 1
                cur_cap -= plants[cur_pos]
                done += 1
                
            if cur_pos + 1 < len(plants) and cur_cap < plants[cur_pos + 1] and cur_pos != -1: # back to river
                steps += abs(cur_pos - target)
                print(f'steps abs(cur_pos - target) : {abs(cur_pos - target)}')
                cur_pos = -1
            elif cur_pos + 1 < len(plants) and plants[cur_pos + 1] < cur_cap:
                cur_pos += 1
                steps += 1
                print(f'steps : 1')
                target += 2
                print(f'target : {target}')
                cur_cap -= plants[cur_pos]
                done += 1
        return steps
        """