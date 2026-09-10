"""schedule"""
def main():
    """schedule"""
    teach, time = map(int, input().split())
    total_min = teach * time
    hour = total_min // 60
    minute = total_min % 60
    
