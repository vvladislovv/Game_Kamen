import random

# Изменим структуру статистики для хранения побед и поражений
leaderstats = {"wins": 0, "losses": 0, "draws": 0}

def subject_choosing(player_choice, game_mode, player2_choice=None):
    """Определяет результат игры"""
    if game_mode == "PC":
        computer_choice = random.choice(["Камень", "Ножницы", "Бумага"])
        result = determine_winner(player_choice, computer_choice)
        return result, computer_choice
    elif game_mode == "PVP" and player2_choice:
        result = determine_winner(player_choice, player2_choice)
        return result, player2_choice
    return None, None

def determine_winner(player_choice, opponent_choice):
    """Определяет победителя"""
    if player_choice == opponent_choice:
        return "Ничья"
    win_combinations = {
        "Камень": "Ножницы",
        "Ножницы": "Бумага",
        "Бумага": "Камень"
    }
    if win_combinations[player_choice] == opponent_choice:
        return "Игрок выиграл"
    return "Противник выиграл"

def update_stats(result):
    """Обновляет статистику на основе результата игры"""
    if result == "Игрок выиграл":
        leaderstats["wins"] += 1
    elif result == "Противник выиграл":
        leaderstats["losses"] += 1
    elif result == "Ничья":
        leaderstats["draws"] += 1

