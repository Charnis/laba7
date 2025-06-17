class Fitness:

    def __init__(self, Id, Year, NumberMounth, Time):
        self.Id = Id
        self.Year = Year
        self.NumberMounth = NumberMounth
        self.Time = Time

    def __str__(self):
        return f"ID: {self.Id}, Год: {self.Year}, Месяц: {self.NumberMounth}, Время: {self.Time} мин"

FitnessHours = [
    Fitness("1", "2025", "05", "45"),
    Fitness("2", "2024", "12", "30"),
    Fitness("3", "2023", "03", "60"),
    Fitness("4", "2022", "01", "120"),
    Fitness("5", "2021", "09", "90")
]

shorthour = min(FitnessHours, key=lambda x: int(x.Time))
longhour = max(FitnessHours, key=lambda x: int(x.Time))

print(f"Занятие которое заканчивается раньше всех: {shorthour}")
print(f"Занятие которое заканчивается позже всех: {longhour}")

