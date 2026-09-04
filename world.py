import random

def trigger_random_event(player_state):
    events = [
        ("Вы нашли чип с данными в темном переулке! (+50 кредитов)", 50),
        ("Вас ограбили местные кибер-бандиты! (-30 кредитов)", -30),
        ("Вы помогли дрону-уборщику. Он отблагодарил вас. (+20 кредитов)", 20)
    ]
    
    text, gold_change = random.choice(events)
    player_state.change_gold(gold_change)
    player_state.show_log(f"[СОБЫТИЕ] {text}")
  
