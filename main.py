from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Импортируем наши модули
import config
from player import PlayerState
from world import WorldManager
from events import trigger_random_event

app = Ursina()

# Инициализируем системы
player_state = PlayerState()
world_manager = WorldManager()

# Создаем физический мир
player = FirstPersonController(position=(0, 1, 0))
ground = Entity(model='plane', scale=(100, 1, 100), color=color.dark_gray, texture='white_cube', collider='box')

# Загружаем первый город
world_manager.load_city(player_state.current_city, player_state)

event_timer = 0

def update():
    global event_timer
    
    # Таймер случайных событий при движении
    if player.speed > 0:
        event_timer += time.dt
        if event_timer > config.EVENT_COOLDOWN:
            trigger_random_event(player_state)
            event_timer = 0
            
    # Проверка близости к сюжетному NPC
    if world_manager.npc_list and distance(player.position, world_manager.npc_list[0].position) < 3:
        if player_state.quest_stage == 0:
            player_state.quest_text.text = "Сюжет: Отправляйтесь в 'Пыльные Доки' через терминал."
            player_state.show_log("Информатор: 'Код доступа спрятан в промзоне. Удачи.'")
            player_state.quest_stage = 1
        elif player_state.quest_stage == 2:
            player_state.quest_text.text = "Сюжет: Финал! Вы спасли Сеть."
            player_state.show_log("Информатор: 'Отличная работа. Мы взломали систему!'")
            player_state.quest_stage = 3

    # Подсказка возле терминала путешествий
    if distance(player.position, Vec3(5, 1, -5)) < 3:
        player_state.show_log("Нажмите [E] для перехода в другой город")

def input(key):
    if key == 'e' or key == 'у':
        # Переход в другой город у золотого терминала
        if distance(player.position, Vec3(5, 1, -5)) < 3:
            cities = list(config.CITIES_DB.keys())
            current_index = cities.index(player_state.current_city)
            next_city = cities[(current_index + 1) % len(cities)]
            
            # Развитие сюжета при путешествии
            if player_state.current_city == "Нью-Аркам" and player_state.quest_stage == 1:
                player_state.quest_stage = 2
                player_state.quest_text.text = "Сюжет: Вернитесь к Информатору в 'Нью-Аркам'."
                
            player.position = (0, 1, 0)
            world_manager.load_city(next_city, player_state)

app.run()
          0time.dtplayer.speed1player_state.quest_text.text23app.runplayer.position
