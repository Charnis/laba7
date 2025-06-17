class Fitness:
    def __init__(self, Id, Year, NumberMonth, Time):
        self.Id = Id
        self.Year = Year
        self.NumberMonth = NumberMonth
        self.Time = Time

    def __str__(self):
        return f"ID: {self.Id}, Год: {self.Year}, Месяц: {self.NumberMonth}, Время: {self.Time} мин"

FitnessHours = [
    Fitness("1", "2023", "05", "60"),
    Fitness("2", "2023", "06", "45"),
    Fitness("3", "2023", "07", "90"),
    Fitness("4", "2022", "03", "120"),
    Fitness("5", "2022", "04", "60"),
    Fitness("6", "2022", "05", "30"),
    Fitness("7", "2023", "08", "45"),
    Fitness("8", "2023", "09", "60"),
    Fitness("9", "2024", "01", "90"),
    Fitness("10", "2024", "02", "120")
]

# Создаем словарь для хранения суммарного времени по годам
yearly_total = {}

# Заполняем словарь суммарными значениями
for session in FitnessHours:
    year = session.Year
    time = int(session.Time)
    if year in yearly_total:
        yearly_total[year] += time
    else:
        yearly_total[year] = time

# Находим максимальное суммарное время
max_time = max(yearly_total.values())

# Находим все года с максимальным временем
max_years = [year for year, total in yearly_total.items() if total == max_time]

# Выбираем наименьший год, если их несколько
best_year = min(max_years) if max_years else None

# Выводим результаты
print("\nВсе занятия:")
for session in FitnessHours:
    print(session)

print("\nСуммарное время по годам:")
for year, total in yearly_total.items():
    print(f"{year} год: {total} мин")

print(f"\nГод с наибольшей суммарной продолжительностью: {best_year}")
print(f"Суммарная продолжительность: {max_time} мин")

# Дополнительно выводим самое короткое и длинное занятие (как в вашем примере)
shorthour = min(FitnessHours, key=lambda x: int(x.Time))
longhour = max(FitnessHours, key=lambda x: int(x.Time))
print(f"\nСамое короткое занятие: {shorthour}")
print(f"Самое длинное занятие: {longhour}")