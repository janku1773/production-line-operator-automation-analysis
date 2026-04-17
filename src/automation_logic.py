import pandas as pd

class AutomationValidator:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.takt_limit = 240  # Maximum seconds allowed

    def calculate_metrics(self):
        total_time = self.df['duration_sec'].sum()
        manual_time = self.df[self.df['type'] == 'Manual']['duration_sec'].sum()
        auto_time = self.df[self.df['type'] == 'Automation']['duration_sec'].sum()
        
        status = "✅ PASS" if total_time <= self.takt_limit else "❌ FAIL"
        
        return {
            "Total Cycle Time": total_time,
            "Manual Effort": manual_time,
            "Automation Support": auto_time,
            "Validation Status": status
        }

if __name__ == "__main__":
    validator = AutomationValidator('data/cycle_time_steps.csv')
    results = validator.calculate_metrics()
    
    print("--- Industrial Automation Validation ---")
    for key, value in results.items():
        print(f"{key}: {value}")