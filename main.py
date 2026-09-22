# main.py
import random
from exercises import EXERCISES, SPLITS

def generate_workout_plan(days: int):
    if days not in SPLITS:
        print("Поддерживается выбор от 1 до 3 тренировочных дней в неделю.")
        return

    selected_split = SPLITS[days]
    print(f"\n==========================================")
    print(f"   ВАШ ПЛАН ТРЕНИРОВОК НА {days} ДН. В НЕДЕЛЮ   ")
    print(f"==========================================")

    for day_num, muscle_groups in enumerate(selected_split, 1):
        print(f"\n📅 ДЕНЬ {day_num}:")
        for group in muscle_groups:
            available_exercises = EXERCISES.get(group, [])
            if available_exercises:
                # Выбираем 2 случайных упражнения для каждой группы мышц
                count = min(2, len(available_exercises))
                chosen = random.sample(available_exercises, k=count)
                
                group_name_ru = group.upper()
                print(f"  • {group_name_ru}:")
                for ex in chosen:
                    print(f"    - {ex}")

def main():
    print("FitPlanGenerator v1.0")
    try:
        days = int(input("Сколько дней в неделю планируете заниматься (1-3)? "))
        generate_workout_plan(days)
    except ValueError:
        print("Ошибка: введите число от 1 до 3.")

if __name__ == "__main__":
    main()