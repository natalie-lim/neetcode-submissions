class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            sub_d = self.d[key]
            sub_d[timestamp] = value
            self.d[key] = sub_d
        else:
            sub_d = {}
            sub_d[timestamp] = value
            self.d[key] = sub_d
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            sub_d = self.d[key]
        else:
            return ""
        print(sub_d)
        if not timestamp in sub_d:
            for t in reversed(range(timestamp)):
                if t in sub_d:
                    return sub_d[t]
            return ""
        else:
            return (sub_d[timestamp])
        
