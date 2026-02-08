from collections import defaultdict
import csv

class Stats:
    global_stats = defaultdict(int)
    by_month = defaultdict(lambda: {"images": 0, "videos": 0, "animations": 0})

    @staticmethod
    def update_global(file, special=None):
        Stats.global_stats["total"] += 1

        ext = file.suffix.lower()
        if ext in [".jpg", ".jpeg", ".png"]:
            Stats.global_stats["images"] += 1
        elif ext in [".mp4", ".mov", ".avi", ".mkv"]:
            Stats.global_stats["videos"] += 1
        elif ext == ".gif":
            Stats.global_stats["animations"] += 1
        else:
            Stats.global_stats["others"] += 1

        if special:
            Stats.global_stats[special] += 1

    @staticmethod
    def update_by_month(file, year, month):
        ext = file.suffix.lower()
        key = f"{year}-{month}"

        if ext in [".jpg", ".jpeg", ".png"]:
            Stats.by_month[key]["images"] += 1
        elif ext in [".mp4", ".mov", ".avi", ".mkv"]:
            Stats.by_month[key]["videos"] += 1
        elif ext == ".gif":
            Stats.by_month[key]["animations"] += 1

    @staticmethod
    def write_audit(path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Metric", "Count"])
            for k, v in Stats.global_stats.items():
                writer.writerow([k, v])

            writer.writerow([])
            writer.writerow(["Year-Month", "Images", "Videos", "Animations"])
            for ym, counts in Stats.by_month.items():
                writer.writerow([ym, counts["images"], counts["videos"], counts["animations"]])
