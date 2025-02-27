import tkinter as tk
import tkinter.ttk as ttk
from logic_game import leaderstats, subject_choosing, update_stats

# Добавим глобальные переменные для хранения меток результата и статистики
result_label = None
wins_label = None
losses_label = None
draws_label = None
player2_choice = None

def start_app():
    """
    Запускает основной интерфейс с кнопками 
    """
    root = tk.Tk()
    root.title("Game Interface")
    root.geometry("600x600")

    # Create notebook for tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # First tab - Player selection
    player_frame = tk.Frame(notebook)
    notebook.add(player_frame, text="Выбор игрока")

    # Add player selection options
    pc_button = tk.Button(player_frame, text="Играть с ПК", width=20, height=3,
                          command=lambda: show_choice_buttons(player_frame, "PC"))
    pc_button.pack(pady=20)

    pvp_button = tk.Button(player_frame, text="1 на 1", width=20, height=3,
                           command=lambda: show_pvp_screen(player_frame))
    pvp_button.pack(pady=20)

    # Add exit button
    exit_button = tk.Button(player_frame, text="Выйти из игры", width=20, height=3,
                            command=root.destroy)
    exit_button.pack(pady=20)

    # Second tab - Statistics
    stats_frame = tk.Frame(notebook)
    notebook.add(stats_frame, text="Статистика")

    # Add statistics labels
    global wins_label, losses_label, draws_label
    wins_label = tk.Label(stats_frame, text=f"Побед: {leaderstats['wins']}", font=('Arial', 14))
    wins_label.pack(pady=20)

    losses_label = tk.Label(stats_frame, text=f"Поражений: {leaderstats['losses']}", font=('Arial', 14))
    losses_label.pack(pady=20)
    
    draws_label = tk.Label(stats_frame, text=f"Ничьих: {leaderstats['draws']}", font=('Arial', 14))
    draws_label.pack(pady=20)

    # Добавляем обработчик события переключения вкладок для обновления статистики
    notebook.bind("<<NotebookTabChanged>>", lambda event: update_stats_display())

    root.mainloop()

def update_stats_display():
    """Обновляет отображение статистики"""
    global wins_label, losses_label, draws_label
    if wins_label and wins_label.winfo_exists():
        wins_label.config(text=f"Побед: {leaderstats['wins']}")
    if losses_label and losses_label.winfo_exists():
        losses_label.config(text=f"Поражений: {leaderstats['losses']}")
    if draws_label and draws_label.winfo_exists():
        draws_label.config(text=f"Ничьих: {leaderstats['draws']}")

def show_choice_buttons(frame, game_mode):
    """Показывает кнопки выбора предмета"""
    # Очищаем фрейм от предыдущих элементов
    for widget in frame.winfo_children():
        widget.destroy()

    # Создаем кнопки выбора
    rock_button = tk.Button(frame, text="Камень", width=20, height=3,
                            command=lambda: handle_choice("Камень", game_mode, frame))
    rock_button.pack(pady=10)

    scissors_button = tk.Button(frame, text="Ножницы", width=20, height=3,
                                command=lambda: handle_choice("Ножницы", game_mode, frame))
    scissors_button.pack(pady=10)

    paper_button = tk.Button(frame, text="Бумага", width=20, height=3,
                             command=lambda: handle_choice("Бумага", game_mode, frame))
    paper_button.pack(pady=10)

    # Add back button
    back_button = tk.Button(frame, text="Назад", width=20, height=3,
                            command=lambda: show_main_menu(frame))
    back_button.pack(pady=10)

def show_pvp_screen(frame):
    """Показывает экран для игры 1 на 1"""
    # Очищаем фрейм от предыдущих элементов
    for widget in frame.winfo_children():
        widget.destroy()
        
    # Заголовок для первого игрока
    player1_label = tk.Label(frame, text="Игрок 1, выберите:", font=('Arial', 14))
    player1_label.pack(pady=10)
    
    # Кнопки выбора для первого игрока
    rock_button1 = tk.Button(frame, text="Камень", width=20, height=2,
                            command=lambda: show_player2_screen(frame, "Камень"))
    rock_button1.pack(pady=5)

    scissors_button1 = tk.Button(frame, text="Ножницы", width=20, height=2,
                                command=lambda: show_player2_screen(frame, "Ножницы"))
    scissors_button1.pack(pady=5)

    paper_button1 = tk.Button(frame, text="Бумага", width=20, height=2,
                             command=lambda: show_player2_screen(frame, "Бумага"))
    paper_button1.pack(pady=5)
    
    # Кнопка назад
    back_button = tk.Button(frame, text="Назад", width=20, height=2,
                            command=lambda: show_main_menu(frame))
    back_button.pack(pady=10)

def show_player2_screen(frame, player1_choice):
    """Показывает экран выбора для второго игрока"""
    # Очищаем фрейм от предыдущих элементов
    for widget in frame.winfo_children():
        widget.destroy()
        
    # Заголовок для второго игрока
    player2_label = tk.Label(frame, text="Игрок 2, выберите:", font=('Arial', 14))
    player2_label.pack(pady=10)
    
    # Кнопки выбора для второго игрока
    rock_button2 = tk.Button(frame, text="Камень", width=20, height=2,
                            command=lambda: handle_pvp_result(frame, player1_choice, "Камень"))
    rock_button2.pack(pady=5)

    scissors_button2 = tk.Button(frame, text="Ножницы", width=20, height=2,
                                command=lambda: handle_pvp_result(frame, player1_choice, "Ножницы"))
    scissors_button2.pack(pady=5)

    paper_button2 = tk.Button(frame, text="Бумага", width=20, height=2,
                             command=lambda: handle_pvp_result(frame, player1_choice, "Бумага"))
    paper_button2.pack(pady=5)

def handle_pvp_result(frame, player1_choice, player2_choice):
    """Обрабатывает результат игры 1 на 1"""
    # Очищаем фрейм от предыдущих элементов
    for widget in frame.winfo_children():
        widget.destroy()
        
    # Получаем результат
    result, _ = subject_choosing(player1_choice, "PVP", player2_choice)
    
    # Обновляем статистику
    if result == "Игрок выиграл":
        update_stats("Игрок выиграл")
    elif result == "Противник выиграл":
        update_stats("Противник выиграл")
    else:
        update_stats("Ничья")
    update_stats_display()
    
    # Отображаем выборы игроков и результат
    choices_label = tk.Label(frame, text=f"Игрок 1 выбрал: {player1_choice}\nИгрок 2 выбрал: {player2_choice}", 
                            font=('Arial', 14))
    choices_label.pack(pady=10)
    
    # Исправляем условие для отображения результата
    pvp_result = "Ничья"
    if result == "Игрок выиграл":
        pvp_result = "Игрок 1 выиграл!"
    elif result == "Противник выиграл":
        pvp_result = "Игрок 2 выиграл!"
    
    result_label = tk.Label(frame, text=f"Результат: {pvp_result}", font=('Arial', 16, 'bold'))
    result_label.pack(pady=20)
    
    # Кнопка для возврата в главное меню
    back_button = tk.Button(frame, text="Вернуться в главное меню", width=25, height=2,
                           command=lambda: show_main_menu(frame))
    back_button.pack(pady=20)

def show_main_menu(frame):
    """Показывает главное меню"""
    # Очищаем фрейм от предыдущих элементов
    for widget in frame.winfo_children():
        widget.destroy()

    # Добавляем кнопки выбора режима игры
    pc_button = tk.Button(frame, text="Играть с ПК", width=20, height=3,
                          command=lambda: show_choice_buttons(frame, "PC"))
    pc_button.pack(pady=20)

    pvp_button = tk.Button(frame, text="1 на 1", width=20, height=3,
                           command=lambda: show_pvp_screen(frame))
    pvp_button.pack(pady=20)

    # Добавляем кнопку выхода
    exit_button = tk.Button(frame, text="Выйти из игры", width=20, height=3,
                            command=frame.winfo_toplevel().destroy)
    exit_button.pack(pady=20)

def handle_choice(choice, game_mode, frame):
    """Обрабатывает выбор предмета"""
    global result_label
    result, computer_choice = subject_choosing(choice, game_mode)

    # Очищаем фрейм от предыдущих элементов
    for widget in frame.winfo_children():
        widget.destroy()

    if result:
        # Обновляем интерфейс с результатом
        result_message = f"Вы выбрали: {choice}\nКомпьютер выбрал: {computer_choice}\nРезультат: {result}"
        result_label = tk.Label(frame, text=result_message, font=('Arial', 14))
        result_label.pack(pady=20)
        
        # Обновляем статистику
        update_stats(result)
        update_stats_display()
        
        # Кнопка для новой игры
        new_game_button = tk.Button(frame, text="Новая игра", width=20, height=2,
                                   command=lambda: show_choice_buttons(frame, game_mode))
        new_game_button.pack(pady=10)
        
        # Кнопка для возврата в главное меню
        back_button = tk.Button(frame, text="Вернуться в главное меню", width=20, height=2,
                               command=lambda: show_main_menu(frame))
        back_button.pack(pady=10)
    else:
        error_label = tk.Label(frame, text="Ошибка в режиме игры.", font=('Arial', 14))
        error_label.pack(pady=20)
        
        # Кнопка для возврата в главное меню
        back_button = tk.Button(frame, text="Вернуться в главное меню", width=20, height=2,
                               command=lambda: show_main_menu(frame))
        back_button.pack(pady=10)

