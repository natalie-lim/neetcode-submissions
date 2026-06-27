class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(position)):
            pos = position[i]
            sp = speed[i]
            d[pos] = sp

        d = dict(reversed(sorted(d.items())))
        s = []

        for (pos, speed) in d.items():
            if not s:
                s.append((pos, speed))
            prev_pos, prev_speed = s.pop()
            time_top = (target - prev_pos) / prev_speed
            time_curr = (target - pos) / speed
            s.append((prev_pos, prev_speed))
            if time_curr > time_top:
                s.append((pos, speed))

        return (len(s))