from datetime import datetime,timedelta

def get_total_downtime(metrics):
    total_time = timedelta()
    for metric in metrics:
        parts = metric["downtime"].split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])

        # Create a timedelta object for the current time
        current_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)

        # Add the current time to the total time
        total_time += current_time
    return total_time

def get_maintenance_cost(metrics):
    cost = 0
    for metric in metrics:
        cost += metric["maintenance_cost"]
    return cost

def get_high_failure_assets(metrics):
    high_failure_assets = {}
    for metric in metrics:
        if metric["failure_rate"] > 40:
            high_failure_assets[metric["asset_id"]] = metric["failure_rate"]
    return high_failure_assets