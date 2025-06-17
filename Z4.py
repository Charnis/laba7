class Fitness:

    def __init__(self, DateStart , DateFinish, Description):
        self.DateStart = DateStart
        self.DateFinish = DateFinish
        self.Description = Description

    def display_info(self):
        print(f"Старт: {self.DateStart}")
        print(f"Финиш: {self.DateFinish}")
        print(f"Время забега: {self.Description}")


Tasks = [
    Task("05.09.2025","29.05.2025", "Painting"),
    Task("05.09.2025","30.05.2025","3D modeling"),
    Task("05.09.2025","12.05.2025","Dances"),
    Task("05.09.2025","28.04.2025","Swimming"),
    Task("05.09.2025","1.05.2025","Football")
]

latest_task = max(Tasks, key=lambda x: x.DateFinish)
print(f"Занятие которое заканчивается позже всех: {latest_task.Description}")