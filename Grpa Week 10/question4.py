class Time:
    def __init__(self, time):
        self.time = time

    def seconds_to_minutes(self):
        mins = self.time // 60
        secs = self.time % 60
        return f"{mins} min {secs} sec"

    def seconds_to_hours(self):
        hours = self.time // 3600
        remaining_secs = self.time % 3600
        mins = remaining_secs // 60
        secs = remaining_secs % 60
        return f"{hours} hrs {mins} min {secs} sec"

    def seconds_to_days(self):
        days = self.time // 86400  # 24 * 3600
        remaining_secs = self.time % 86400
        hours = remaining_secs // 3600
        remaining_secs %= 3600
        mins = remaining_secs // 60
        secs = remaining_secs % 60
        return f"{days} days {hours} hrs {mins} min {secs} sec"
